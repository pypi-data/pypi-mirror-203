import datetime
import os
import typing as t

import pytest

import mantik.mlflow_server.flask.api as _api
import mantik.testing as testing
import mantik.tracking._server as _server
import mantik.tracking._server._credentials as _credentials
import mantik.utils as utils

EXPIRES_AT = datetime.datetime(2022, 1, 1)


@pytest.fixture()
def credentials() -> _credentials.Credentials:
    return _credentials.Credentials(
        username="test-user",
        password="test-password",
    )


@pytest.mark.parametrize(
    ("mlflow_tracking_uri", "expected"),
    [
        (
            "https://test-url.com",
            _server.tokens.Tokens(
                access_token="test-access-token",
                refresh_token="test-refresh-token",
                expires_at=EXPIRES_AT,
            ),
        ),
        (None, NameError()),
    ],
)
def test_create_tokens(
    requests_mock, credentials, mlflow_tracking_uri, expected
):
    _set_mlflow_tracking_uri_env_var(mlflow_tracking_uri)
    requests_mock.post(
        url=f"{mlflow_tracking_uri}{_api.tokens.CREATE_TOKEN_API_PATH}",
        json={
            "AccessToken": "test-access-token",
            "RefreshToken": "test-refresh-token",
            "ExpiresAt": EXPIRES_AT.isoformat(),
        },
    )

    with testing.contexts.expect_raise_if_exception(expected):
        result = _server.api.create_tokens(credentials=credentials)

        assert result == expected


@pytest.mark.parametrize(
    ("mlflow_tracking_uri", "expected"),
    [
        (
            "https://test-url.com",
            _server.tokens.Tokens(
                access_token="test-refreshed-access-token",
                refresh_token="test-refresh-token",
                expires_at=EXPIRES_AT,
            ),
        ),
        (None, NameError()),
    ],
)
def test_refresh_tokens(
    requests_mock, credentials, mlflow_tracking_uri, expected
):
    _set_mlflow_tracking_uri_env_var(mlflow_tracking_uri)
    requests_mock.post(
        url=f"{mlflow_tracking_uri}{_api.tokens.REFRESH_TOKEN_API_PATH}",
        json={
            "AccessToken": "test-refreshed-access-token",
            "ExpiresAt": EXPIRES_AT.isoformat(),
        },
    )

    tokens = _server.tokens.Tokens(
        access_token="test-access-token",
        refresh_token="test-refresh-token",
        expires_at=datetime.datetime(2000, 1, 1),
    )

    with testing.contexts.expect_raise_if_exception(expected):
        result = _server.api.refresh_tokens(
            credentials=credentials,
            tokens=tokens,
        )

        assert result == expected


def test_create_api_url():
    mlflow_tracking_uri = "http://test-uri.com"
    _set_mlflow_tracking_uri_env_var(mlflow_tracking_uri)
    endpoint = "/endpoint/path"

    expected = "https://test-uri.com/endpoint/path"

    result = _server.api._create_api_url(endpoint)

    assert result == expected


def _set_mlflow_tracking_uri_env_var(value: t.Optional[str]) -> None:
    if value is None:
        os.environ.pop(utils.mlflow.TRACKING_URI_ENV_VAR)
        return
    os.environ[utils.mlflow.TRACKING_URI_ENV_VAR] = value
