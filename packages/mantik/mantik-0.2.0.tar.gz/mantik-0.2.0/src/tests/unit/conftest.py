import datetime
import os
import pathlib
import typing as t

import pytest

import mantik.tracking._server._credentials as _credentials
import mantik.tracking.track as track
import mantik.unicore.config.environment
import mantik.utils as utils


@pytest.fixture()
def mlflow_tracking_uri() -> str:
    return "https://test-uri.com"


@pytest.fixture()
def required_env_vars(mlflow_tracking_uri) -> t.Dict[str, str]:
    return {
        _credentials._MANTIK_USERNAME_ENV_VAR: "test-user",
        _credentials._MANTIK_PASSWORD_ENV_VAR: "test-password",
        utils.mlflow.TRACKING_URI_ENV_VAR: mlflow_tracking_uri,
        # If the env vars for MLflow user/password are set, these are
        # prioritized by MLflow over the token. This leads to an
        # `Unauthorized` error.
        utils.mlflow.TRACKING_USERNAME_ENV_VAR: "must-be-unset",
        utils.mlflow.TRACKING_PASSWORD_ENV_VAR: "must-be-unset",
    }


@pytest.fixture()
def token_expiration_date() -> datetime.datetime:
    return datetime.datetime(2022, 1, 1)


@pytest.fixture()
def tmp_dir_as_test_mantik_folder(tmp_path):
    track._MANTIK_FOLDER = pathlib.Path(tmp_path)
    track._MANTIK_TOKEN_FILE = track._MANTIK_FOLDER / "tokens.json"
    return tmp_path


def pytest_configure(config):
    """Remove all MLFLOW_ related environment variables before running any
    test to simplify tests setup."""
    for env in mantik.unicore.config.environment._get_mlflow_env_vars():
        del os.environ[env]
