# aws-sso-cli

A program to simplify logging in and setting credentials using AWS
SSO.

## Installation

This can be installed via `pip`:

```
pip install aws-sso-cli
```

You can also find wheels from the [releases page on
gitlab](https://gitlab.com/pdebelak/aws-sso-cli/-/releases).

## Usage

Running `aws-sso-cli` with no arguments will check if you are logged
in, and log in with `aws sso login` if you are not. It will
additionally create or update your credentials file (in either
`$AWS_SHARED_CREDENTIALS_FILE` if defined or defaulting to
`$HOME/.aws/credentials`) after logging in and will attempt to log you
into AWS ECR if docker is running.

You can use a different profile than `default` or the normal
`AWS_PROFILE` environment variable by using the `--profile` flag.

If you want to log in even if you are already logged in, pass the
`--force` flag.

If you want to log into AWS ECR only, pass the `--docker-force` flag.
This is useful if you start the docker daemon after already running
`aws-sso-cli`.

## Requirements

Actually signing in to AWS requires the
[aws-cli](https://github.com/aws/aws-cli) program. This also requires
Python to be installed and the boto3 library.

## Development

Run `make test` to generate a virtual environment and run tests.
