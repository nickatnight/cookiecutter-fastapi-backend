import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
BASE_BACKEND_SRC_PATH = "{{ cookiecutter.backend_container_name }}/src/"
CELERY_FILE_PATHS = [
    "%sworker.py" % BASE_BACKEND_SRC_PATH,
]
DEPLOYMENT_FILES = [
    ".github/workflows/deploy.yml",
    "{{ cookiecutter.backend_container_name }}/fly.toml",
]


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def rename_file(old: str, new: str):
    in_ = os.path.join(PROJECT_DIRECTORY, old)
    out_ = os.path.join(PROJECT_DIRECTORY, new)
    os.rename(in_, out_)


if "{{ cookiecutter.cloud_provider }}" == "none":
    print("Removing deployment files...")
    for p in DEPLOYMENT_FILES:
        remove_file(p)

if "{{ cookiecutter.use_celery }}" == "no":
    print("Removing celery files...")
    for p in CELERY_FILE_PATHS:
        remove_file(p)

rename_file(".env_example", ".env")
