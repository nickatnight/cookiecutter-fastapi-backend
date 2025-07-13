import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
BASE_BACKEND_SRC_PATH = "{{ cookiecutter.backend_container_name }}/src/"
CELERY_FILE_PATHS = [
    "%sworker.py" % BASE_BACKEND_SRC_PATH,
    "%sapi/deps.py" % BASE_BACKEND_SRC_PATH,
    "%s__init__.py" % BASE_BACKEND_SRC_PATH,
    "%score/tasks.py" % BASE_BACKEND_SRC_PATH,
]
DEPLOYMENT_FILES = [
    "render.yaml",
]


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def create_file(filepath: str):
    open(os.path.join(PROJECT_DIRECTORY, filepath), "w").close()


def rename_file(old: str, new: str):
    in_ = os.path.join(PROJECT_DIRECTORY, old)
    out_ = os.path.join(PROJECT_DIRECTORY, new)
    os.rename(in_, out_)


if "{{ cookiecutter.deployments }}" == "none":
    print("Removing deployment files...")
    for p in DEPLOYMENT_FILES:
        remove_file(p)

if "{{ cookiecutter.use_celery }}" == "no":
    print("Removing celery files...")
    for p in CELERY_FILE_PATHS:
        remove_file(p)

    # deleting and creating new __init__.py file because formatting with pre-commit is difficult with if conditions in potentially empty file
    print("Creating empty __init__.py file")
    create_file(os.path.join(BASE_BACKEND_SRC_PATH, "__init__.py"))


rename_file(".env_example", ".env")
