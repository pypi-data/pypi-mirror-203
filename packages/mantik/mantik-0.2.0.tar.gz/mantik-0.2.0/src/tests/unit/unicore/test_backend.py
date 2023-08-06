import functools
import json
import os
import pathlib

import mlflow.projects as projects
import pyunicore.client

import mantik.testing as testing
import mantik.unicore.backend as backend
import mantik.unicore.client as client_wrapper
import mantik.unicore.config.core as core
import mantik.utils as utils

FILE_PATH = pathlib.Path(__file__).parent

ALL_ENV_VARS = [
    core._USERNAME_ENV_VAR,
    core._PASSWORD_ENV_VAR,
    core._PROJECT_ENV_VAR,
]


class FakeProject:
    pass


class TestUnicoreBackend:
    def test_run(self, monkeypatch, example_project_path, tmpdir):
        monkeypatch.setattr(
            pyunicore.client,
            "Transport",
            testing.pyunicore.FakeTransport,
        )
        fake_client_with_successful_login = functools.partial(
            testing.pyunicore.FakeClient,
            login_successful=True,
        )
        monkeypatch.setattr(
            pyunicore.client,
            "Client",
            fake_client_with_successful_login,
        )
        backend_config_path = example_project_path / "unicore-config.json"
        with open(backend_config_path) as infile:
            backend_config = json.load(infile)

        # Following env vars are set by MLflow before running a project.
        backend_config[
            projects.PROJECT_STORAGE_DIR
        ] = example_project_path.as_posix()

        # Following env vars must be set for the config.
        for key in ALL_ENV_VARS:
            os.environ[key] = "test-val"

        # Point MLFLOW_TRACKING_URI to a temporary directory
        tracking_uri = tmpdir / "mlruns"
        os.environ[utils.mlflow.TRACKING_URI_ENV_VAR] = f"file://{tracking_uri}"

        submitted_run = backend.UnicoreBackend().run(
            project_uri=example_project_path.as_posix(),
            entry_point="main",
            params={"print": "test"},
            version=None,
            backend_config=backend_config,
            tracking_uri=None,
            experiment_id=None,
        )

        utils.env.unset_env_vars({utils.mlflow.TRACKING_URI_ENV_VAR})
        assert submitted_run._job._job.started


def test_submit_job_in_staging_in_and_upload_input_files(
    example_project_path, example_project, example_config
):
    client = testing.pyunicore.FakeClient()
    entry_point = example_project.get_entry_point("main")
    parameters = {"print": "test"}
    singularity_image = example_project_path / "mantik-test.sif"
    client = client_wrapper.Client(client)
    backend._submit_job_in_staging_in_and_upload_input_files(
        client=client,
        entry_point=entry_point,
        parameters=parameters,
        storage_dir="",
        input_files=[singularity_image],
        config=example_config,
        run_id="example_run_id",
    )


def test_create_job_description(
    example_project_path, example_project, example_config
):
    entry_point = example_project.get_entry_point("main")
    parameters = {"print": "whatever"}
    storage_dir = "test-dir"
    expected = {
        "Executable": (
            "srun singularity run "
            "--cleanenv "
            "--env MLFLOW_TRACKING_URI="
            "${MLFLOW_TRACKING_URI:-file://$PWD/mlruns} "
            "${MLFLOW_TRACKING_TOKEN:"
            "+--env MLFLOW_TRACKING_TOKEN=$MLFLOW_TRACKING_TOKEN} "
            "${MLFLOW_EXPERIMENT_NAME:"
            "+--env MLFLOW_EXPERIMENT_NAME=$MLFLOW_EXPERIMENT_NAME} "
            "${MLFLOW_EXPERIMENT_ID:"
            "+--env MLFLOW_EXPERIMENT_ID=$MLFLOW_EXPERIMENT_ID} "
            "mantik-test.sif"
        ),
        "Arguments": [
            "python",
            "main.py",
            "whatever",
            "&>>mantik.log",
            "2>&1",
        ],
        "Project": "test-project",
        "Resources": {"Queue": "batch"},
        "RunUserPrecommandOnLoginNode": "false",
    }
    result = backend.create_job_description(
        entry_point=entry_point,
        parameters=parameters,
        storage_dir=storage_dir,
        config=example_config,
    )
    # The config reads `MLFLOW_` env vars. This is not the scope
    # of this test here and they depend on the execution environment.
    try:
        result.pop("Environment")
    except KeyError:
        pass

    assert result == expected
