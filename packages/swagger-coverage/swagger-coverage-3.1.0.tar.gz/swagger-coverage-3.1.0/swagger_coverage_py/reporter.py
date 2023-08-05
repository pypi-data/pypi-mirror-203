import os
import platform
import re
import shutil
import subprocess
from pathlib import Path

import requests

from swagger_coverage_py.configs import API_DOCS_FORMAT, DEBUG_MODE
from swagger_coverage_py.docs_writers.api_doc_writer import write_api_doc_to_file


class CoverageReporter:
    def __init__(self, api_name: str, host: str, verify: bool = True):
        self.host = host
        self.verify = verify
        self.swagger_doc_file = f"swagger-doc-{api_name}.{API_DOCS_FORMAT}"
        self.output_dir = self.__get_output_dir()
        self.ignore_requests = []
        self.swagger_coverage_config = f"swagger-coverage-config-{api_name}.json"

    def __get_output_dir(self):
        output_dir = "swagger-coverage-output"
        subdir = re.match(r"(^\w*)://(.*)", self.host).group(2)
        return f"{output_dir}/{subdir}"

    def setup(
        self, path_to_swagger_json: str, auth: object = None, cookies: dict = None
    ):
        """Setup all required attributes to generate report

        :param path_to_swagger_json: The relative URL path to the swagger.json (example: "/docs/api")
        :param auth: Authentication object acceptable by "requests" library
        :param cookies: Cookies dictionary. (Usage example: set this to bypass Okta auth locally)

        """
        link_to_swagger_json = f"{self.host}{path_to_swagger_json}"

        response = requests.get(link_to_swagger_json, auth=auth, cookies=cookies, verify=self.verify)
        assert response.ok, (
            f"Swagger doc is not pulled. See details: "
            f"{response.status_code} {response.request.url}"
            f"{response.content}\n{response.content}"
        )

        write_api_doc_to_file(self.swagger_doc_file, response)

    def generate_report(self):
        inner_location = "swagger-coverage-commandline/bin/swagger-coverage-commandline"

        cmd_path = os.path.join(os.path.dirname(__file__), inner_location)
        assert Path(
            cmd_path
        ).exists(), (
            f"No commandline tools is found in following locations:\n{cmd_path}\n"
        )

        if self.swagger_coverage_config:
            command = f"{cmd_path} -s {self.swagger_doc_file} -i {self.output_dir} -c {self.swagger_coverage_config}"
        else:
            command = f"{cmd_path} -s {self.swagger_doc_file} -i {self.output_dir}"

        command = (
            command if platform.system() != "Windows" else command.replace("/", "\\")
        )

        # Suppress all output if not in debug mode
        command = command + " > /dev/null 2>&1" if not DEBUG_MODE else command

        subprocess.run(command, shell=True)

    def cleanup_input_files(self):
        shutil.rmtree(self.output_dir, ignore_errors=True)
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
