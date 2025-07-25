import os
import re
import sys
from typing import Dict, List

import pytest
from binaryornot.check import is_binary
from cookiecutter.exceptions import FailedHookException

try:
    import sh
except (ImportError, ModuleNotFoundError):
    sh = None  # sh doesn't support Windows

if sys.platform.startswith("win"):
    pytest.skip("sh doesn't support windows", allow_module_level=True)
# elif sys.platform.startswith("darwin") and os.getenv("CI"):
#     # "CI" env var is provided by GHA runner
#     pytest.skip("skipping slow macOS tests on CI", allow_module_level=True)

SUPPORTED_COMBINATIONS = [
    {"deployments": "none"},
    {"deployments": "render"},
    {"deployments": "digitalocean"},
    {"use_celery": "no", "periodic_tasks": "no"},
    {"use_celery": "yes", "periodic_tasks": "no"},
    {"use_celery": "yes", "periodic_tasks": "yes"},
    {"py_version": "3.9"},
    {"py_version": "3.10"},
    {"py_version": "3.11"},
    {"use_sentry": "no"},
    {"use_sentry": "yes"},
]
UNSUPPORTED_COMBINATIONS = [
    {"use_celery": "no", "periodic_tasks": "yes"},
]
PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context() -> Dict:
    return {
        "project_name": "Goblet of Fire",
        "__project_slug": "goblet-of-fire",
        "__project_slug_db": "gobletoffire",
        "author_email": "harry@hogwarts.com",
        "py_version": "3.10",
        "db_container_name": "db",
        "backend_container_name": "backend",
        "github_username": "yer.a.wizard",
    }


def build_files_list(base_dir) -> List[str]:
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(base_dir)
        for file_path in files
    ]


def check_paths(paths) -> None:
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path):
            match = RE_OBJ.search(line)
            assert match is None, f"cookiecutter variable not replaced in {path}"


def _fixture_id(ctx) -> str:
    """Helper to get a user-friendly test name from the parametrized context."""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies, context, context_override) -> None:
    """Test that project is generated and fully rendered."""

    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["__project_slug"]
    assert result.project_path.is_dir()

    paths = build_files_list(str(result.project_path))
    assert paths
    check_paths(paths)


@pytest.mark.parametrize("slug", ["project slug", "Project_Slug"])
def test_invalid_slug(cookies, context, slug):
    """Invalid slug should fail pre-generation hook."""
    context.update({"__project_slug": slug})

    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize("invalid_context", UNSUPPORTED_COMBINATIONS)
def test_error_if_incompatible(cookies, context, invalid_context):
    """It should not generate project an incompatible combination is selected."""
    context.update(invalid_context)
    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_pre_commit_hooks(cookies, context_override) -> None:
    """Generated project pre-commit hooks run successfully."""
    _ = cookies.bake(extra_context=context_override)

    try:
        if os.getenv("CI"):  # so pre-commit has files to run against
            sh.git("init")
        sh.uv("run", "pre-commit", "run", "--all-files")
    except sh.ErrorReturnCode as e:
        pytest.fail(e.stdout.decode())
