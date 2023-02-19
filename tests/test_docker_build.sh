#!/bin/sh
# this is a very simple script that tests the docker configuration for cookiecutter-fastapi-backend
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_docker_build.sh

set -o errexit
set -x

# create a cache directory
mkdir -p .cache/docker
cd .cache/docker

# create the project using the default settings in cookiecutter.json
poetry run cookiecutter ../../ --no-input --overwrite-if-exists "$@"
cd fastapi-backend

# Lint by running pre-commit on all files
# Needs a git repo to find the project root
# We don't have git inside Docker, so run it outside
git init
git add .
poetry run pre-commit run --show-diff-on-failure --all-files

# bring up project
docker-compose up

# run the project's type checks
docker-compose run --rm backend mypy src/

# run the project's tests
docker-compose run --rm backend pytest tests/

# test health endpoint
RESPONSE=$(curl -o /dev/null --silent --head --write-out '%{http_code}\n' -X GET localhost:8666/v1/ping)
if [[ $response != "200" ]]; then
    echo "Unhealthy endpoint"
    exit 1
fi

# return non-zero status code if there are migrations that have not been created
# docker-compose run backend alembic --dry-run --check || { echo "ERROR: there were changes in the models, but migration listed above have not been created and are not saved in version control"; exit 1; }

# clean up
docker-compose down -v
