import itertools
import json
import os
import re
import uuid

import requests
import sys
import threading
import time
import zipfile
from pathlib import Path
scripts_dir_path = Path(__file__).parents[1]
sys.path.insert(0, str(scripts_dir_path))
from pathlib import Path
from EVMVerifier.certoraJobList import JobList
from Shared.certoraUtils import flush_stdout, get_package_and_version, check_results, remove_file, write_json_file
from Shared.certoraUtils import get_certora_build_file, get_certora_verify_file, get_certora_config_dir
from Shared.certoraUtils import print_completion_message, get_certora_metadata_file, get_certora_sources_dir
from Shared.certoraUtils import PRODUCTION_PACKAGE_NAME, get_debug_log_file
from Shared.certoraUtils import Mode, CertoraUserInputError, PACKAGE_FILE
from Shared.certoraUtils import get_certora_internal_dir, is_new_api, DASHBOARD_URL
from EVMVerifier.certoraContextClass import CertoraContext
import EVMVerifier.certoraContextAttribute as Attr

from typing import Optional, Dict, Any, List, Union, cast
from tqdm import tqdm

import logging


cloud_logger = logging.getLogger("cloud")

MAX_FILE_SIZE = 25 * 1024 * 1024
NO_OUTPUT_LIMIT_MINUTES = 15
MAX_POLLING_TIME_MINUTES = 120
LOG_READ_FREQUENCY = 10
MAX_ATTEMPTS_TO_FETCH_OUTPUT = 3
DELAY_FETCH_OUTPUT_SECONDS = 10

# error messages
CONNECTION_ERR_PREFIX = "Connection error:"
GENERAL_ERR_PREFIX = "An error occurred:"
SERVER_ERR_PREFIX = "Server Error:"
STATUS_ERR_PREFIX = "Error Status:"
TIMEOUT_MSG_PREFIX = "Request timed out."
VAAS_ERR_PREFIX = "Server reported an error:"

CONTACT_CERTORA_MSG = "please contact Certora on https://www.certora.com"

Response = requests.models.Response

FEATURES_REPORT_FILE = Path("featuresReport.json")


class TimeError(Exception):
    """A custom exception used to report on time elapsed errors"""


def validate_version_and_branch(branch: Optional[str], commit_sha1: Optional[str]) -> None:
    """
    Gets the latest package version and compares to the local package version.
    If the major version is different - i.e. there is new breaking syntax, will raise an error.
    If a minor version is different, it just warns the user and recommends him to upgrade the package.

    If the Python package is a dev package (not the production package), checks if the user provided a branch or a
    commit sha, and if not raises an appropriate error.

    If there are problems when performing this check, skips it with a warning. Possible reasons:
    1. Connectivity problems
    2. A Certora installed package is not found
    3. Unexpected version format, either for the local package or the remote
    4. If the local version is more advanced than the remote version

    :param branch: The name of the branch. If None or an empty string, no branch name was provided by the user.
    :param commit_sha1: The sha1 hash of a git commit
    :raises:
        CertoraUserInputError if:
         - The local package version is not compatible with the latest package version.
         - The local package is a dev package and no branch name was given
    """
    package_name, version = get_package_and_version()
    if not re.search(r"^\d+\.\d+\.\d+$", version):  # Version should be a string in X.Y.Z format
        """
        If the local version was not found, the value of `version` is an error message. prints it
        """
        cloud_logger.warning(f"{package_name}")
        return
    try:
        distribution_url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(distribution_url, timeout=10)
        out = response.json()  # raises ValueError: No JSON object could be decoded
        latest = out['info']['version']
        if "." in latest and "." in version:
            # below lines raise ValueError: invalid literal for int() with base 10
            remote_main, remote_sub, remote_patch = [int(x) for x in latest.split(".")]
            local_main, local_sub, local_patch = [int(x) for x in version.split(".")]

            installation_cmd = f"pip install {package_name} --upgrade\n"\
                               f"or\n"\
                               f"pip3 install {package_name} --upgrade"

            must_upgrade_msg = \
                f"Incompatible package {package_name} version {version} with the latest version {latest}."\
                f" Please upgrade by running:\n"\
                f"{installation_cmd}"

            recommended_upgrade_msg = \
                f"You are using {package_name} version {version}; however, version {latest} is available."\
                f" It is recommended to upgrade by running: {installation_cmd}"

            if remote_main > local_main:
                if package_name == PRODUCTION_PACKAGE_NAME:
                    raise CertoraUserInputError(must_upgrade_msg)
                cloud_logger.warning(recommended_upgrade_msg)

            elif remote_main == local_main and \
                    (remote_sub > local_sub or
                     (remote_sub == local_sub and remote_patch > local_patch)):
                """
                The main version number is the same, but one of the minor versions are not.
                Therefore, it is only a recommendation/warning.
                """
                cloud_logger.warning(recommended_upgrade_msg)

            if package_name != PRODUCTION_PACKAGE_NAME:
                # it is guaranteed to be a Certora dev package by the previous call to get_package_and_version()

                if not (branch or commit_sha1):  # if it is None or the empty string
                    raise CertoraUserInputError(
                        f"You must use the package {package_name} with either --cloud BRANCH or --staging BRANCH,"
                        "or provide a specific --commit_sha1.")
    except (requests.exceptions.RequestException, ValueError) as e:
        if isinstance(e, CertoraUserInputError):
            raise e
        cloud_logger.warning(f"Failed to find the latest package version of {package_name}. Local version is {version}")
        cloud_logger.debug("When trying to find the latest package version, got the following exception:", exc_info=e)


def progress_bar(total: int = 70, describe: str = "Initializing verification") -> None:
    for _ in tqdm(range(total),
                  bar_format="{l_bar}{bar}| [remaining-{remaining}]",
                  ncols=70, desc=describe, ascii=".#"):
        time.sleep(1)


def parse_json(response: Response) -> Dict[str, Any]:
    try:
        json_response = response.json()
    except ValueError:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX} Could not parse JSON response")
        print(response.text)  # Should we print the whole response here?
        return {}
    return json_response


def compress_files(zip_file_name: str, *resource_paths: Path, short_output: bool = False) -> bool:
    zip_obj = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    total_files = 0
    for path in resource_paths:
        if path.is_dir():
            total_dir_files = get_total_files(path)
            if total_dir_files == 0:
                cloud_logger.error(f"{GENERAL_ERR_PREFIX} Provided directory - '{path}' is empty.")
                return False
            elif total_dir_files > 0:
                total_files += total_dir_files
        elif path.is_file():
            total_files += 1
        else:
            cloud_logger.error(f"{GENERAL_ERR_PREFIX} Provided file - '{path}' does not exist.")
            return False
    if total_files < 1:
        if len(resource_paths) == 0:
            cloud_logger.error(f"{GENERAL_ERR_PREFIX} No file was provided. {CONTACT_CERTORA_MSG}")
        else:
            cloud_logger.error(f"{GENERAL_ERR_PREFIX} Provided file(s) - "
                               f"{', '.join([str(file) for file in resource_paths])} do(es) not exist.")
        return False

    i = 0

    for path in resource_paths:
        if path.is_dir():
            try:
                # traverse the directory recursively for all files
                for file_path in Path(path).rglob("*"):
                    if file_path.is_file():
                        posix_path = file_path.as_posix()
                        zip_obj.write(posix_path, os.path.relpath(posix_path, get_certora_internal_dir()))
                        if not short_output:
                            i += 1
                            cloud_logger.debug(f"Compressing ({i}/{total_files}) - {file_path}")
            except OSError:
                flush_stdout()
                cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  f"Could not compress a directory - {path}")
                return False
        else:  # zip file
            try:
                """
                Why do we use the base name? Otherwise, when we provide a relative path dir_a/dir_b/file.tac,
                the zip function will create a directory dir_a, inside it a directory dir_b and inside that file.tac
                """

                zip_obj.write(path, os.path.relpath(path, get_certora_internal_dir()))
                if not short_output:
                    i += 1
                    cloud_logger.debug(f"Compressing ({i}/{total_files}) - {path}")
            except OSError:
                flush_stdout()
                cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  f"Could not compress {path}")
                return False
    zip_obj.close()

    if os.path.getsize(zip_file_name) > MAX_FILE_SIZE:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX} Max 25MB file size exceeded.")
        return False

    return True


def get_total_files(directory: Path) -> int:
    try:
        total_files = len([path for path in directory.rglob('*') if path.is_file()])
        return total_files
    except OSError:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX} Could not traverse {directory}")
        return -1


def output_error_response(response: Response) -> None:
    cloud_logger.error(f"{STATUS_ERR_PREFIX}: {response.status_code}")
    if response.status_code == 500:
        cloud_logger.error(f"{SERVER_ERR_PREFIX} {CONTACT_CERTORA_MSG}")
        return
    try:
        error_response = response.json()
        if "errorString" in error_response:
            cloud_logger.error(f"{VAAS_ERR_PREFIX} {error_response['errorString']}")
        elif "message" in error_response:
            cloud_logger.error(f"{VAAS_ERR_PREFIX} {error_response['message']}")
    except Exception as e:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX}: request failed", exc_info=e)
        print(response.text)


def is_success_response(json_response: Dict[str, Any], status_url: str = "") -> bool:
    """
    @param json_response:
    @param status_url:
    @return: False when the server response missing the success field or success value False
    """
    if "success" not in json_response:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  "The server returned an unexpected response:")
        print(json_response)
        print(CONTACT_CERTORA_MSG)
        return False
    if not json_response["success"]:
        if "errorString" in json_response:
            cloud_logger.error(f'{json_response["errorString"]} {status_url}')
        else:
            cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  "The server returned an error with no message:")
            print(json_response)
            print(CONTACT_CERTORA_MSG)
        return False
    return True


def print_conn_error() -> None:
    cloud_logger.error(f"{CONNECTION_ERR_PREFIX}: Server is currently unavailable. Please try again later.")
    print(f"For further information, {CONTACT_CERTORA_MSG}", flush=True)


def look_for_path(path: str) -> Optional[Response]:
    try:
        r = requests.get(path, timeout=10)
        if r.status_code == requests.codes.ok:
            return r
    except (requests.exceptions.Timeout, requests.exceptions.RequestException, ConnectionError):
        print_conn_error()
    return None


def fetch_results_from_web(output_url: str, max_attempts: int, delay_between_attempts_seconds: int) -> \
        Optional[Union[Dict[str, Any], List[Dict[str, Any]]]]:
    attempts = 0
    actual = None
    while actual is None and attempts < max_attempts:
        attempts += 1
        response = look_for_path(output_url)
        try:  # read as json
            if response is not None:
                actual = response.json()
        except json.decoder.JSONDecodeError:
            # when '' is returned
            pass
        if actual is None and attempts < max_attempts:
            time.sleep(delay_between_attempts_seconds)
    return actual


def check_results_from_web(output_url: str,
                           max_attempts: int,
                           delay_between_attempts_seconds: int,
                           expected_filename: str,
                           report_url: str) -> bool:
    """
    Returns true if the actual results match the expected results.
    @param output_url - URL of output.json
    @param max_attempts - max number of attempts to get output.json
    @param delay_between_attempts_seconds - delay in seconds between attempts to get output.json
    @param expected_filename - name of the expected file to compare output.json to. If the expected file
                                does not exist, will require all rules to succeed
    @param report_url - a full report URL to refer the user to in case output.json does not exist
    """
    actual = fetch_results_from_web(output_url, max_attempts, delay_between_attempts_seconds)
    if actual is None:
        # Could not find actual results file output.json... print report URL for more details
        cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  f"Could not find job results, please refer to {report_url} for"
                           f" additional information")
        return False
    return check_results(cast(dict, actual), expected_filename)


def save_features_json_from_web(output_url: str, max_attempts: int, delay_between_attempts_seconds: int) -> None:
    features_json_content = fetch_results_from_web(output_url, max_attempts, delay_between_attempts_seconds)
    if features_json_content is None:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  f"Could not download features report file ({FEATURES_REPORT_FILE})")
        return
    try:
        write_json_file(features_json_content, FEATURES_REPORT_FILE)
    except (ValueError, OSError) as e:
        cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  f"Error occurred when saving json data: {e}")
        return
    print_completion_message(f"{FEATURES_REPORT_FILE} was successfully created")


def send_get_request(session: requests.Session, url: str, data: Dict[str, str], lim: int = 60) -> \
        Optional[Dict[str, Any]]:
    """
    Sends a get request to the supplied url with the data as a query parameters and returns the response as a dictionary
    It's important to know that we expect to get a JSON format response (that's why we call the `parse_json` function)
    @param session: requests session object
    @param url: a string
    @param data: a dictionary of parameters to be sent in the query string
    @param lim: a number of seconds to wait for a server response
    @return: a server response as a dictionary, or None on 502 status code
    @raise requests.exceptions.RequestException: on 4XX/5XX status code
    @raise requests.exceptions.Timeout:  if no bytes have been received for `lim` seconds

    * we treat the 502 error differently as it is usually resolved relatively quickly
    """
    response = session.get(url, params=data, timeout=lim)
    if response.status_code != requests.codes.ok:
        if response.status_code != 502:
            output_error_response(response)
            raise requests.exceptions.RequestException
        else:
            cloud_logger.debug("502 Bad Gateway")
            return None
    else:
        return parse_json(response)


class CloudVerification:
    """Represents an AWS Cloud verification"""

    def __init__(self, context: CertoraContext, timings: Optional[Dict[str, float]] = None) -> None:
        self.context = context
        self.queue_wait_minutes = NO_OUTPUT_LIMIT_MINUTES
        self.max_poll_minutes = MAX_POLLING_TIME_MINUTES
        self.log_query_frequency_seconds = LOG_READ_FREQUENCY
        self.max_attempts_to_fetch_output = MAX_ATTEMPTS_TO_FETCH_OUTPUT
        self.delay_fetch_output_seconds = DELAY_FETCH_OUTPUT_SECONDS
        self.max_poll_error_msg = f"The contract is being processed for more than {self.max_poll_minutes} minutes"
        self.max_no_output_error_msg = f"There was no output for {self.queue_wait_minutes} minutes."
        self.timings = timings
        self.sleep_seconds = 2

        for timer in ['queue_wait_minutes', 'max_poll_minutes', 'log_query_frequency_seconds',
                      'max_attempts_to_fetch_output', 'delay_fetch_output_seconds']:
            val = getattr(self.context, timer)
            if val is not None:
                setattr(self, timer, val)

        self.runName = uuid.uuid4().hex
        self.ZipFileName = self.runName + ".zip"
        self.logZipFileName = self.runName + "_cli_debug_log.zip"
        self.url = ""
        self.checkUrl = ""
        self.jsonOutputUrl = ""
        self.logUrl = ""
        self.statusUrl = ""
        self.reportUrl = ""
        self.zipOutputUrl = ""
        self.jobDataUrl = ""
        self.featuresResults = ""
        if not self.context.short_output:
            self.anim_thread = threading.Thread(target=self.animate)
        self.done = False
        self.triggered = False

        self.anonymousKey = ""
        self.presigned_url = ""
        self.userId = -1
        self.msg = ""
        self.user_defined_cache = context.user_defined_cache
        self.expected_filename = context.expected_file

        self.set_protocol_name_and_author(context)

    def __set_url(self, url_attr: str, index: str, user_id: int, current_job_anonymous_key: str,
                  requested_resource: Optional[str] = None) -> None:
        """
        DO NOT USE THIS, use set_output_url() etc. instead.
        This function is intended for internal use by the aforementioned functions. We DO NOT check that the url_attr is
        defined!
        @param url_attr: name of the attribute we want to set in self. For example, if url_attr == "logUrl",
                         then self.logUrl will be set.
        @param index: name of the url index of this request
        @param user_id: id number of the user sending the request
        @param current_job_anonymous_key: user's anonymous key
        """
        if self.url == "":
            cloud_logger.debug(f"setting {url_attr}: url is not defined.")
        elif self.runName == "":
            cloud_logger.debug(f"setting {url_attr}: runName is not defined.")
        else:
            resource_req = f"{'/' + requested_resource if requested_resource is not None else ''}"
            url = f"{self.url}/{index}/{user_id}/{self.runName}{resource_req}?anonymousKey={current_job_anonymous_key}"
            setattr(self, url_attr, url)

    def set_protocol_name_and_author(self, context: CertoraContext) -> None:
        """
        Sets the `protocol_name` and `protocol_author` attributes of the `self` object based on the `context` argument.
        If these attributes are not specified in the `context` argument, the function attempts to read the data from the
        `package.json` file and set the attributes based on the values found in the file.

        :param context: An instance of the `CertoraContext` class that contains the `protocol_name` and
                        `protocol_author` attributes.
        """
        self.protocol_name = context.protocol_name
        self.protocol_author = context.protocol_author

        if not self.protocol_name or not self.protocol_author:
            if PACKAGE_FILE.is_file():
                # Try to read the data from package.json
                with open(PACKAGE_FILE) as package_file:
                    package_data = json.load(package_file)

                if not self.protocol_name:
                    self.protocol_name = package_data.get("name")

                if not self.protocol_author:
                    self.protocol_author = package_data.get("author")

    def print_error_and_status_url(self, err_msg: str, status_url: Union[str, None] = None) -> None:
        if status_url is None:
            status_url = self.statusUrl
        self.stop_animation()
        cloud_logger.error(f"{GENERAL_ERR_PREFIX} {err_msg}")
        if status_url:
            print("For further details visit", status_url)
        print("Closing connection...", flush=True)

    def check_polling_timeout(self, start: float, max_duration_in_minutes: int, error_msg: str) -> None:
        stop = time.perf_counter()
        if stop - start > max_duration_in_minutes * 60:  # polling time in seconds
            self.print_error_and_status_url(error_msg, '')
            raise TimeError()

    # jar output (logs) url
    def set_output_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("logUrl", "job", user_id, anonymous_key)

    # index report url
    def set_report_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("reportUrl", "output", user_id, anonymous_key)

    # index report url
    def set_requested_resource_url(self, user_id: int, resource_name: str, resource_file: str, anonymous_key: str) \
            -> None:
        self.__set_url(resource_name, "output", user_id, anonymous_key, requested_resource=resource_file)

    # status page url
    def set_status_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("statusUrl", "jobStatus", user_id, anonymous_key)

    # compressed output folder url
    def set_zip_output_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("zipOutputUrl", "zipOutput", user_id, anonymous_key)

    # json output url
    def set_json_output_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("jsonOutputUrl", "jsonOutput", user_id, anonymous_key)

    def set_check_file_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("checkUrl", "exists", user_id, anonymous_key)

    def set_job_data_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("jobDataUrl", "jobData", user_id, anonymous_key)

    def prepare_auth_data(self, cl_args: str) -> Optional[Dict[str, Any]]:
        """
        :param cl_args: A string that can be copied to and run by the shell to recreate this run.
        @return: An authentication data dictionary to send to server
        """

        auth_data = {
            "certoraKey": self.context.key,
            "process": self.context.process,
            "runName": self.runName,
            "run_source": self.context.run_source
        }  # type: Dict[str, Any]

        """
        Earlier checks guarantee that we cannot get both cloud and staging as not None
        Note: the attributes are evaluated as True if they are both:
        1. Not None (say, --cloud was not used)
        2. Not the empty string (--cloud without an argument)
        """
        if self.context.staging:
            auth_data["branch"] = self.context.staging
        elif self.context.cloud:
            auth_data["branch"] = self.context.cloud
        elif self.context.commit_sha1:
            auth_data["git_hash"] = self.context.commit_sha1

        _, version = get_package_and_version()
        auth_data["version"] = version

        ext_args = self.context.prover_ext if is_new_api() else self.context.settings
        if ext_args is not None:
            jar_settings = []  # type: List[str]
            for settings_exp in ext_args:  # It is in standard form
                jar_settings.extend(settings_exp.split("="))

            auth_data["jarSettings"] = jar_settings

        if self.context.coinbaseMode:
            if "jarSettings" not in auth_data:
                auth_data["jarSettings"] = [Attr.ContextAttribute.COINBASE_MODE.value.jar_flag]
            else:
                auth_data["jarSettings"].append(Attr.ContextAttribute.COINBASE_MODE.value.jar_flag)

        if self.context.java_args is not None:
            auth_data["javaArgs"] = self.context.java_args

        if self.context.cache is not None:
            auth_data["toolSceneCacheKey"] = self.context.cache

        if self.context.msg is not None:
            auth_data["msg"] = self.context.msg

        if self.timings is not None:
            auth_data.update(self.timings)

        auth_data["buildArgs"] = cl_args

        if self.protocol_name:
            auth_data["protocolName"] = self.protocol_name

        if self.protocol_author:
            auth_data["protocolAuthor"] = self.protocol_author

        cloud_logger.debug(f'authdata = {auth_data}')
        return auth_data

    def print_output_links(self) -> None:
        print(f"Follow your job at {DASHBOARD_URL}")
        print(f"Once the job is completed, the results will be available at {self.reportUrl}")

    def print_verification_summary(self) -> None:
        report_exists = self.check_file_exists(params={"filename": "index.html", "certoraKey": self.context.key})
        if report_exists:
            print(f"Job is completed! View the results at {self.reportUrl}")
        print("Finished verification request", flush=True)

    def __send_verification_request(self, cl_args: str) -> bool:
        """
        Sends an authentication request to the server.
        Sets the user id, anonymous key, presigned url and message parameters of this CloudVerification
        :param cl_args: A string that can be copied to and run by the shell to recreate this run.
        :return: True if there were no errors
        """
        auth_data = self.prepare_auth_data(cl_args)
        if auth_data is None:
            return False

        resp = self.verification_request(auth_data)  # send post request to /cli/verify

        if resp is None:  # on error
            return False

        json_response = parse_json(resp)
        if not json_response:
            return False

        if not is_success_response(json_response):
            return False

        try:
            self.anonymousKey = json_response["anonymousKey"]
            self.presigned_url = json_response["presigned_url"]
            self.userId = json_response["userId"]
            self.msg = auth_data.get("msg", "")
            return True
        except Exception as e:  # (Json) ValueError
            cloud_logger.error(f"{GENERAL_ERR_PREFIX}"  f"Unexpected response {e}")
            return False

    def __compress_and_upload_zip_files(self) -> bool:
        """
        compresses all files to a zip file and uploads it to the server
        :return: True if there were no errors in compressing or uploading
        """
        cloud_logger.debug("Compressing the files")
        # remove previous zip file
        remove_file(self.ZipFileName)

        # create new zip file
        if self.context.mode == Mode.TAC:
            # We zip the tac file itself
            result = compress_files(self.ZipFileName, self.context.files[0], short_output=self.context.short_output)
        elif self.context.mode == Mode.BYTECODE:
            # We zip the bytecode jsons and the spec
            paths = []
            for bytecode_json in self.context.bytecode_jsons:
                paths.append(Path(bytecode_json))
            paths.append(Path(self.context.bytecode_spec))
            result = compress_files(self.ZipFileName, *paths,
                                    short_output=self.context.short_output)
        else:
            # Zip the log file first separately and again with the rest of the files, so it will not be decompressed
            # on each run in order to save space
            result = compress_files(self.logZipFileName, get_debug_log_file(),
                                    short_output=self.context.short_output)

            if not result:
                return False
            files_list = [get_certora_build_file(), get_certora_verify_file(), get_certora_config_dir(),
                          get_certora_metadata_file(), Path(self.logZipFileName)]
            if get_certora_sources_dir().exists():
                files_list.append(get_certora_sources_dir())
            result = compress_files(self.ZipFileName, *files_list, short_output=self.context.short_output)

        flush_stdout()
        if not result:
            return False

        cloud_logger.debug("Uploading files...")
        if self.upload(self.presigned_url, self.ZipFileName):
            print_completion_message("Job submitted to server")
            print()
        else:  # upload error
            return False

        self.set_status_url(self.userId, self.anonymousKey)

        return True

    def cli_verify_and_report(self, cl_args: str, send_only: bool = False) -> bool:
        """
        Sends a verification request to HTTP Handler, uploads a zip file, and outputs the results.
        :param send_only: If True, we will not wait for the results of the verification.
        :param cl_args: A string that can be copied to and run by the shell to recreate this run.
        @returns If compareToExpected is True, returns True when the expected output equals the actual results.
                 Otherwise, returns False if there was at least one violated rule.
        """
        self.url = self.context.domain

        post_result = self.__send_verification_request(cl_args)
        if not post_result:
            return False

        file_upload_success = self.__compress_and_upload_zip_files()
        if not file_upload_success:
            return False

        # set results urls. They are all functions of the form: self.set_output_url(self.userId, self.anonymousKey)
        for func_name in ["set_output_url", "set_report_url", "set_zip_output_url", "set_json_output_url",
                          "set_check_file_url", "set_status_url", "set_job_data_url"]:
            func = getattr(self, func_name)
            func(self.userId, self.anonymousKey)

        if self.context.coinbaseMode:
            self.set_requested_resource_url(self.userId, 'featuresResults', 'featuresResults.json', self.anonymousKey)

        # update jobs list
        job_list = JobList()
        job_list.add_job(
            self.runName, self.reportUrl, self.msg, self.url, str(self.userId), self.anonymousKey)

        if send_only:  # do not wait for results
            job_list.save_data()
            job_list.save_recent_jobs_to_path()
            self.print_output_links()
            return True

        else:  # We wait for the results then print them
            print(f"Follow your job at {DASHBOARD_URL}")

            if self.logUrl == "":  # on error
                return False

            thread = threading.Thread(target=job_list.save_data)
            thread.start()

            try:  # print the logs unless the short_output flag is set to True
                if self.context.short_output:
                    self.poll_job_status()
                else:
                    print("Output:", flush=True)
                    self.poll_log()
                self.stop_animation()
                thread.join()
            except (Exception, KeyboardInterrupt):
                try:
                    self.stop_animation()
                    thread.join()
                    raise
                except KeyboardInterrupt:
                    print("You were disconnected from server, but your request is still being processed.")
                    self.print_output_links()
                except requests.exceptions.RequestException:
                    # other requests exceptions
                    print_conn_error()
                except TimeError:
                    self.print_output_links()
                except Exception as e:
                    print("Encountered an error: ", e)
                finally:
                    return False

            # Record the URL of the zip file for use by the mutation testing tool.
            with open('.zip-output-url.txt', 'w') as url_file:
                _ = url_file.write("{}\n".format(self.zipOutputUrl))

            print()
            self.print_verification_summary()

            if self.context.no_compare:
                return True

            result_check_success = check_results_from_web(self.jsonOutputUrl,
                                                          self.max_attempts_to_fetch_output,
                                                          self.delay_fetch_output_seconds,
                                                          self.expected_filename,
                                                          self.reportUrl)
            if self.context.coinbaseMode:
                save_features_json_from_web(self.featuresResults, self.max_attempts_to_fetch_output,
                                            self.delay_fetch_output_seconds)

            return result_check_success

    def verification_request(self, auth_data: Dict[str, Any]) -> Optional[Response]:
        verify_url = self.url + "/cli/verify"
        response = None
        print("\nConnecting to server...")
        cloud_logger.debug(f"requesting verification from {verify_url}")
        # retry on request timeout or 502 (must take no more than 3 minutes)
        # print error message on the 3rd exception and return
        for i in range(3):
            try:
                response = requests.post(verify_url, data=auth_data, timeout=60)
                if response is None:
                    break
                status = response.status_code
                if status == requests.codes.ok:  # 200
                    break
                if status == 403:
                    print("You have no permission. Please, make sure you entered a valid key.")
                    return None
                elif status == 502:
                    cloud_logger.debug("502 Bad Gateway")
                    if i < 2:
                        print("Received an invalid response. Retry...")
                    else:
                        print("Oops, an error occurred when sending your request. Please try again later")
                        return None
                else:  # status != 200, 403, 502
                    output_error_response(response)
                    return None
            except requests.exceptions.Timeout:
                if i < 2:
                    print("Request timeout. Retry...")
                else:
                    cloud_logger.error(f"{TIMEOUT_MSG_PREFIX} {CONTACT_CERTORA_MSG}")
                    return None
            except (requests.exceptions.RequestException, ConnectionError):
                print_conn_error()
                break
        return response

    def poll_log(self) -> None:
        has_output = True
        params = {}
        next_token = ""
        start_poll_t = time.perf_counter()

        self.start_animation()
        s = requests.Session()

        while True:
            try:
                if next_token:  # used for retrieving the logs in chunks
                    params = {"nextToken": next_token}

                json_response = send_get_request(s, self.logUrl, params)
                if json_response is None:  # currently, it's set to None when response status code is 502
                    all_output = None
                    new_token = next_token  # keep the same token
                    status = "PROCESSED"
                elif not json_response:  # Error parsing json
                    self.print_error_and_status_url("Failed to parse response. For more information visit")
                    break
                elif not is_success_response(json_response, self.statusUrl):  # look for execution exceptions
                    break
                else:
                    status = json_response.get("status")  # type: ignore[assignment]
                    if status is None or "nextToken" not in json_response:
                        self.print_error_and_status_url(
                            f"got an unexpected response: status-{status}; token-{new_token}")
                        break

                    new_token = json_response["nextToken"]  # type: ignore[assignment]

                    if "logEventsList" not in json_response:  # response does not include `logEventsList`
                        self.print_error_and_status_url("No output is available.")
                        break
                    all_output = json_response["logEventsList"]

                if all_output:
                    has_output = True
                    self.stop_animation()
                    for outputLog in all_output:
                        msg = outputLog.get("message", "")
                        print(msg, flush=True)
                elif has_output:  # first missing output
                    has_output = False
                    first_miss_out = time.perf_counter()  # start a timer
                else:  # missing output
                    self.check_polling_timeout(first_miss_out, self.queue_wait_minutes, self.max_no_output_error_msg)
                if new_token == next_token and next_token != "":
                    if status == "SUCCEEDED" or status == "FAILED":
                        # When finished it returns the same token you passed in
                        break
                    else:  # the job is still being processed
                        time.sleep(self.log_query_frequency_seconds)
                else:
                    next_token = new_token
                    time.sleep(self.sleep_seconds)
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                # catch timeout and connectionError and resend the request
                time.sleep(self.sleep_seconds)
            self.check_polling_timeout(start_poll_t, self.max_poll_minutes, self.max_poll_error_msg)

    def poll_job_status(self) -> None:
        has_output = True
        job_status = "jobStatus"
        attribute = {"attr": job_status}
        status = None
        start_poll_t = time.perf_counter()
        s = requests.Session()

        while True:
            try:
                json_response = send_get_request(s, self.jobDataUrl, attribute)
                if json_response is None:  # e.g., when response.status_code is 502
                    status = None  # make sure we remove the previous status
                elif not json_response:  # Error parsing json - empty json object is returned
                    self.print_error_and_status_url("Failed to parse response. For more information visit")
                    break
                else:  # json_response is not empty
                    try:
                        status = json_response.get(job_status, None)
                    except AttributeError:  # in case we get an array
                        cloud_logger.error(f"couldn't retrieve '{job_status}' from {json_response}")
                if status == "SUCCEEDED" or status == "FAILED":
                    break
                else:  # the job is still being processed
                    if status:
                        has_output = True
                    elif has_output:  # first miss
                        has_output = False
                        first_miss = time.perf_counter()  # start a timer
                    else:  # sequential miss
                        self.check_polling_timeout(first_miss, self.queue_wait_minutes, self.max_no_output_error_msg)
                    time.sleep(self.log_query_frequency_seconds)
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                # catch timeout and connectionError and resend the request
                time.sleep(self.sleep_seconds)
            self.check_polling_timeout(start_poll_t, self.max_poll_minutes, self.max_poll_error_msg)

    @staticmethod
    def upload(presigned_url: str, file_to_upload: str) -> Optional[Response]:
        """
        Uploads user contract/s as a zip file to S3

        Parameters
        ----------
        presigned_url : str
            S3 presigned url
        file_to_upload : str
            zip file name

        Returns
        -------
        Response
            S3 response - can be handled as a json object
        """
        upload_fail_msg = f"couldn't upload file - {file_to_upload}"
        try:
            with open(file_to_upload, "rb") as my_file:
                http_response = requests.put(presigned_url, data=my_file, headers={"content-type": "application/zip"})
        except ConnectionError as e:
            cloud_logger.error(f"{CONNECTION_ERR_PREFIX} {upload_fail_msg}", exc_info=e)
        except requests.exceptions.Timeout as e:
            cloud_logger.error(f"{TIMEOUT_MSG_PREFIX} {upload_fail_msg}", exc_info=e)
        except requests.exceptions.RequestException as e:
            cloud_logger.error(f"{GENERAL_ERR_PREFIX} {upload_fail_msg}", exc_info=e)
            return None
        except OSError as e:
            cloud_logger.error(f"OSError: {upload_fail_msg}", exc_info=e)

        return http_response

    def check_file_exists(self, params: Dict[str, Any]) -> bool:
        try:
            r = requests.get(self.checkUrl, params=params, timeout=10)
            if r.status_code == requests.codes.ok:
                return True
        except (requests.exceptions.Timeout, requests.exceptions.RequestException, ConnectionError) as e:
            cloud_logger.error(f"{GENERAL_ERR_PREFIX} request failed", exc_info=e)
        return False

    def animate(self, status: str = "processing") -> None:
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self.done:
                break
            sys.stdout.write(f'\r{status} ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r')

    def start_animation(self) -> None:
        if hasattr(self, "anim_thread"):
            if not self.triggered:  # make sure we run the start function once
                self.triggered = True
                self.anim_thread.start()

    def stop_animation(self) -> None:
        if not self.done:
            self.done = True  # used for stopping the animation
            if hasattr(self, "anim_thread"):
                self.anim_thread.join()  # wait for the animation thread

    def __del__(self) -> None:
        remove_file(self.ZipFileName)
        remove_file(self.logZipFileName)
