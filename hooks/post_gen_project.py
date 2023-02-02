import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
BASE_BACKEND_SRC_PATH = "{{ cookiecutter.backend_container_name }}/src/"
MEME_FILE_PATHS = [
    "%smodels/meme.py" % BASE_BACKEND_SRC_PATH,
    "%sschemas/meme.py" % BASE_BACKEND_SRC_PATH,
    "%sapi/v1/meme.py" % BASE_BACKEND_SRC_PATH,
    "%score/utils.py" % BASE_BACKEND_SRC_PATH,
    "%smigrations/versions/3577cec8a2bb_init.py" % BASE_BACKEND_SRC_PATH,
]
DEPLOYMENT_FILES = [
    "ops/docker-compose.prod.yml",
    "ops/docker-compose.staging.yml",
    ".github/workflows/build.yml"
]

def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if "{{ cookiecutter.include_example_api}}" == "no":
    print("Removing example api files...")
    for p in MEME_FILE_PATHS:
        remove_file(p)
    shutil.rmtree("%s/db/clients/" % BASE_BACKEND_SRC_PATH)


if "{{ cookiecutter.deployments }}" == "no":
    print("Removing deployment files...")
    for p in DEPLOYMENT_FILES:
        remove_file(p)
