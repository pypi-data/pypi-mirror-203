import pytest


def test_authenticate_api_calls_returns_200_for_non_api_path(client, api_path):
    response = client.get("/#/experiments/0")

    assert response.status_code == 200


@pytest.mark.parametrize(
    ("headers", "expected"),
    [
        ({}, 401),
        (
            {"Authorization": "test-invalid-token"},
            401,
        ),
        (
            {"Authorization": "Bearer test-invalid-token"},
            401,
        ),
        (
            {"Authorization": "test-valid-token"},
            200,
        ),
        (
            {"Authorization": "Bearer test-valid-token"},
            200,
        ),
    ],
)
def test_authenticate_api_calls(client, api_path, headers, expected):
    response = client.get(
        f"{api_path}/experiments/get",
        headers=headers,
        json={"experiment_id": 0},
    )

    assert response.status_code == expected
