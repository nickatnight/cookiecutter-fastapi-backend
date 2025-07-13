<p align="center">
    <a href="https://github.com/nickatnight/cookiecutter-fastapi-backend/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/cookiecutter-fastapi-backend/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://pypi.org/project/cookiecutter-fastapi-backend/">
        <img alt="PyPi Shield" src="https://img.shields.io/pypi/v/cookiecutter-fastapi-backend">
    </a>
    <a href="https://github.com/nickatnight/cookiecutter-fastapi-backend/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/cookiecutter-fastapi-backend">
    </a>
    <a href="https://docs.astral.sh/uv/">
        <img alt="uv version" src="https://img.shields.io/badge/uv-0.7.18+-purple">
    </a>
    <a href="https://cookiecutter-fastapi-backend.readthedocs.io/en/latest/"><img alt="Read The Docs Badge" src="https://img.shields.io/readthedocs/cookiecutter-fastapi-backend"></a>
</p>

# :cookie: cookiecutter-fastapi-backend
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to build and deploy fastapi backends to your favorite PaaS..batteries included.

Supported PaaS's:
- Render
- Platform.sh (Coming soon)
- Porter (Coming soon)
- Fly.io (Coming soon)
- DigitalOcean (Coming soon)

## Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):
```sh
pip install cookiecutter
```

Generate project from GitHub template:

```sh
$ cookiecutter gh:nickatnight/cookiecutter-fastapi-backend.git
```

Or from Python code:

```python
from cookiecutter.main import cookiecutter

cookiecutter("gh:nickatnight/cookiecutter-fastapi-backend.git")
```

## Features
* :whale: **Docker & Docker Compose** integration and optimization for [local development](https://docs.docker.com/compose/). Fast bundles using build stages and [uv](https://docs.astral.sh/uv/)
* :computer: **Production ready** Python web server using [FastAPI](https://fastapi.tiangolo.com/)
* :pencil2: **SQLModel** [Library](https://sqlmodel.tiangolo.com/) for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust
* :light_rail: **Alembic** Lightweight database migration tool for usage with the [SQLAlchemy](https://alembic.sqlalchemy.org/en/latest/) Database Toolkit for Python
* :floppy_disk: **postgresql** Powerful open source [object-relational](https://www.postgresql.org/) database
* :convenience_store: **Redis** In-memory data structure [store](https://redis.io/), used as a distributed, in-memory key–value database, cache and message broker
* :gear: **Common** Base models and repository classes for common CRUD operations and database schemas.
* :seedling: **Celery** [Asynchronous](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) task or job queue
* :inbox_tray: **Continuous Integration/Deployment** Modular [GitHub Actions](https://github.com/features/actions) to lint, test, and deploy to your favorite platform. Automatically includes [Codecov](https://about.codecov.io/) reporting.
* :leftwards_arrow_with_hook: **pre-commit** [Git hooks](https://pre-commit.com/) to maintain code quality using modern tooling (ruff, black, isort)

## Input Variables
The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name
* `project_slug_db`: The database friendly name of the project. By default, based on the project name
* `author_email`: The authors email...for maintainer info in `pyproject.toml`
* `py_version`: The version of Python to install. Options are `3.9`, `3.10`, and `3.11`
* `db_container_name`: The name of the database container. Default `db`
* `backend_container_name`: The name of the backend container. Default `backend`
* `use_celery`: Whether to use Celery/Beat and Redis for asynchronous/scheduled tasks. Default `no`
* `github_username`: The username of the GitHub user. Used for badge display in generated project `README.md`
* `deployments`: Deploy to your favorite platform, Render.com (and more to come). Default `none`

## Documentation
See full documentation [here](https://cookiecutter-fastapi-backend.readthedocs.io/en/latest/).
