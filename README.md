<p align="center">
    <a href="https://github.com/nickatnight/cookiecutter-fastapi-backend/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/cookiecutter-fastapi-backend/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://github.com/nickatnight/cookiecutter-fastapi-backend/releases"><img alt="Release Status" src="https://img.shields.io/github/v/release/nickatnight/cookiecutter-fastapi-backend"></a>
    <a href="https://github.com/nickatnight/cookiecutter-fastapi-backend/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/cookiecutter-fastapi-backend">
    </a>
</p>

# cookiecutter-fastapi-backend
:cookie: [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to build and deploy fastapi backends..batteries included.

## Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):
```sh
pip install cookiecutter
```

Generate project:
```sh
cookiecutter https://github.com/nickatnight/cookiecutter-fastapi-backend.git
```

## Features
* :whale: **Docker & Docker Compose** integration and optimization for [local development](https://docs.docker.com/compose/). Fast bundles using build stages and [Poetry](https://python-poetry.org/)
* :computer: **Production ready** Python web server using [FastAPI](https://fastapi.tiangolo.com/)
* :pencil2: **SQLModel** [Library](https://sqlmodel.tiangolo.com/) for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust
* :light_rail: **Alembic** Lightweight database migration tool for usage with the [SQLAlchemy](https://alembic.sqlalchemy.org/en/latest/) Database Toolkit for Python
* :globe_with_meridians: **NGINX** High Performance Load Balancer, [Web Server](https://www.nginx.com/), & Reverse Proxy
* :lock: **Let's Encrypt** A free, automated, and open [certificate authority](https://letsencrypt.org/) (CA), provided by the Internet Security Research Group (ISRG)...with automatic cert renewal
* :floppy_disk: **postgresql** Powerful open source [object-relational](https://www.postgresql.org/) database
* :convenience_store: **Redis** In-memory data structure [store](https://redis.io/), used as a distributed, in-memory key–value database, cache and message broker
* :seedling: **Celery** [Asynchronous](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) task or job queue
* :inbox_tray: **Continuous Integration/Deployment** Modular [GitHub Actions](https://github.com/features/actions) to lint, build, test, and deploy to DigitalOcean cloud
* :leftwards_arrow_with_hook: **pre-commit** [Git hooks](https://pre-commit.com/) to maintain code quality using modern tooling (ruff, black, isort)

## Input Variables
The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name
* `project_slug_db`: The database friendly name of the project. By default, based on the project name
* `author_email`: The authors email...used for certbot
* `py_version`: The version of Python to install. Options are `3.9`, `3.10`, and `3.11`
* `db_container_name`: The name of the database container. Default `db`
* `backend_container_name`: The name of the backend container. Default `backend`
* `use_celery`: Whether to use Celery/Beat for asynchronous/scheduled tasks.
* `nginx_container_name`: The name of the nginx web server container. Default `nginx`
* `doctl_version`: The version name of [DigitalOcean Command Line Interface](https://docs.digitalocean.com/reference/doctl/) to use. Default `1.92.0`
* `github_username`: The username of the GitHub user. Used for badge display in generated project `README.md`
* `deployments`: Include `docker-compose` files needed for deployment step in GitHub Action. Options are `y` or `n`


## More Details
After using this generator, your new project (the directory created) will contain an extensive `README.md` with instructions for development, deployment, etc. You can view it [here](/%7B%7B%20cookiecutter.project_slug%20%7D%7D/README.md)

## Development
This project uses [uv](https://github.com/astral-sh/uv) to manage dependencies. To set up the development environment:

1. Install uv: `pip install uv`
2. Install dependencies:    ```sh
   uv pip install -r requirements-dev.txt   ```
3. Run tests: `pytest tests`

Pre-commit:
1. Install pre-commit hooks with `pre-commit install`
2. Run hooks with `pre-commit run --all-files`

## Acknowledgements
- [tiangolo](https://github.com/tiangolo/full-stack-fastapi-postgresql) for the FastAPI project
- [jonra](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async) for the Alembic/SQLModel knowledge
- [nemd](https://github.com/nemd/) / [ironhalik](https://github.com/ironhalik/) for the inspiration and Docker hacks
- [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) for cookiecutter testing patterns
