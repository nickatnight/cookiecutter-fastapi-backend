import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
BASE_BACKEND_SRC_PATH = "{{ cookiecutter.backend_container_name }}/src/"
MEME_FILE_PATHS = [
    "%smodels/meme.py" % BASE_BACKEND_SRC_PATH,
    "%sschemas/meme.py" % BASE_BACKEND_SRC_PATH,
    "%sapi/v1/meme.py" % BASE_BACKEND_SRC_PATH,
    "%srepositories/meme.py" % BASE_BACKEND_SRC_PATH,
    "%sdb/init_db.py" % BASE_BACKEND_SRC_PATH,
]
DEPLOYMENT_FILES = [
    "ops/docker-compose.prod.yml",
    "ops/docker-compose.staging.yml",
    ".github/workflows/build.yml",
]


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def rename_file(old: str, new: str):
    in_ = os.path.join(PROJECT_DIRECTORY, old)
    out_ = os.path.join(PROJECT_DIRECTORY, new)
    os.rename(in_, out_)


if "{{ cookiecutter.include_example_api}}" == "no":
    print("Removing example api files...")
    for p in MEME_FILE_PATHS:
        remove_file(p)


if "{{ cookiecutter.deployments }}" == "no":
    print("Removing deployment files...")
    for p in DEPLOYMENT_FILES:
        remove_file(p)


rename_file(".env_example", ".env")
