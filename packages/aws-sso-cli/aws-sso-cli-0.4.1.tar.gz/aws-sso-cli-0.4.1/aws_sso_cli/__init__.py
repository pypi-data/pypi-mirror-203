# MIT License

# Copyright (c) 2023 Peter Debelak

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
A program to log into AWS SSO if not already logged in.

It also sets the appropriate values in the shared credentials file
after login and logs into any ecr repos if docker is running.
"""
import argparse
import os
import subprocess
import sys
from base64 import b64decode
from configparser import ConfigParser
from pathlib import Path
from typing import Dict, Optional

import boto3
import botocore.exceptions

__version__ = "0.4.1"


def main(cli_args=None):
    parser = build_parser()
    arguments = parser.parse_args(cli_args)
    session = boto3.Session(profile_name=arguments.profile)
    sso = AwsSsoLogin(arguments.profile, session)

    if arguments.force or not sso.is_logged_in():
        sso.login()
        AwsCredentials().set_from(session)
        if not arguments.docker_force:
            AwsDocker().safe_login_from(session)
    if arguments.docker_force:
        AwsDocker().login_from(session)


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-p", "--profile", help="The profile to use")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Log in even if already logged in.",
    )
    parser.add_argument(
        "--docker-force",
        action="store_true",
        help="Log into docker using ECR credentials even if already authenticated with AWS.",
    )
    return parser


class AwsSsoLogin:
    def __init__(self, profile: Optional[str], session: boto3.Session):
        self.profile = profile
        self._sts = session.client("sts")

    def is_logged_in(self) -> bool:
        try:
            self._sts.get_caller_identity()
            return True
        except (
            botocore.exceptions.UnauthorizedSSOTokenError,
            botocore.exceptions.SSOTokenLoadError,
        ):
            return False

    def login(self):
        args = ["aws", "sso", "login"]
        if self.profile is not None:
            args.extend(["--profile", self.profile])
        subprocess.run(args, check=True)


class AwsCredentials:
    def __init__(self):
        self._config = ConfigParser()
        if os.getenv("AWS_SHARED_CREDENTIALS_FILE"):
            self._credentials_file = Path(os.environ["AWS_SHARED_CREDENTIALS_FILE"])
        else:
            self._credentials_file = (
                Path(os.path.expanduser("~")) / ".aws" / "credentials"
            )
        if not self._credentials_file.exists():
            with self._credentials_file.open("w"):
                # create
                pass
        self._config.read(self._credentials_file)

    def update_section(self, section: str, values: Dict[str, str]):
        if self._config.has_section(section):
            new_values = self._config[section]
        else:
            self._config.add_section(section)
            new_values = {}
        for key, value in values.items():
            new_values[key] = value
        self._config[section] = new_values
        with self._credentials_file.open("w") as f:
            self._config.write(f)

    def set_from(self, session: boto3.Session):
        credentials = session.get_credentials()
        profile_config = {
            "aws_access_key_id": credentials.access_key,
            "aws_secret_access_key": credentials.secret_key,
        }
        if credentials.token:
            profile_config["aws_session_token"] = credentials.token
        self.update_section(session.profile_name, profile_config)


class AwsDocker:
    timeout_seconds = 2

    def docker_running(self):
        try:
            subprocess.run(
                ["docker", "ps"],
                capture_output=True,
                check=True,
                timeout=self.timeout_seconds,
            )
            return True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return False

    def safe_login_from(self, session: boto3.Session):
        if not self.docker_running():
            print(
                "Docker does not appear to be running. Not logging into ECR.",
                file=sys.stderr,
            )
            return
        try:
            self.login_from(session)
        except botocore.exceptions.ClientError as e:
            print(
                f"Got error fetching ECR credentials from AWS: {e}",
                file=sys.stderr,
            )

    def login_from(self, session: boto3.Session):
        token_resp = session.client("ecr").get_authorization_token()
        for endpoint in token_resp["authorizationData"]:
            username, password = (
                b64decode(endpoint["authorizationToken"].encode("utf-8"))
                .decode("utf-8")
                .split(":")
            )
            subprocess.run(
                [
                    "docker",
                    "login",
                    "--username",
                    username,
                    "--password-stdin",
                    endpoint["proxyEndpoint"],
                ],
                input=password.encode("utf-8"),
                check=True,
            )
