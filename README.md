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
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to build and deploy fastapi backends..batteries included.

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
* **Docker & Docker Compose** integration and optimization for local development. Fast bundles using build stages and Poetry
* **Production ready** Python web server using Uvicorn
* Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a>:
    * **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).
    * **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
    * **Easy**: Designed to be easy to use and learn. Less time reading docs.
    * **Short**: Minimize code duplication. Multiple features from each parameter declaration.
    * **Robust**: Get production-ready code. With automatic interactive documentation.
    * **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> and <a href="http://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.
    * <a href="https://fastapi.tiangolo.com/features/" class="external-link" target="_blank">**Many other features**</a> including automatic validation, serialization, interactive documentation, authentication with OAuth2 JWT tokens, etc.
* **SQLModel** Library for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust
* **Alembic** Lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python
* **CORS** (Cross Origin Resource Sharing).
* **NGINX** High Performance Load Balancer, Web Server, & Reverse Proxy
* **Let's Encrypt** A free, automated, and open certificate authority (CA), provided by the Internet Security Research Group (ISRG)...with automatic cert renewal
* **PostgresSQL** Powerfull open source object-relational database
* **AsyncPG** Database interface library designed specifically for PostgreSQL and Python/asyncio
* **Redis** In-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker
* **Continuous Integration/Deployment** Modular GitHub Actions to lint, build, test, and deploy to DigitalOcean cloud
* **pre-commit** Git hooks to maintain code quality

## Input Variables
The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `project_slug`: The development friendly name of the project. By default, based on the project name
* `project_slug_db`: The database friendly name of the project. By default, based on the project name
* `author_email`: The authors email...used for certbot
* `db_container_name`: The name of the database container. Default `db`
* `backend_container_name`: The name of the backend container. Default `backend`
* `nginx_container_name`: The name of the nginx web server container. Default `nginx`
* `doctl_version`: The version name of [DigitalOcean Command Line Interface](https://docs.digitalocean.com/reference/doctl/) to use. Default `1.92.0`
* `github_username`: The username of the GitHub user. Used for badge display in generated project `README.md`
* `include_example_api`: Include example API, models, schemas, and script to init db data. Options are `y` or `n`
* `deployments`: Include `docker-compose` files needed for deployment step in GitHub Action. Options are `y` or `n`


## More Details
After using this generator, your new project (the directory created) will contain an extensive `README.md` with instructions for development, deployment, etc. You can view it [here](/%7B%7B%20cookiecutter.project_slug%20%7D%7D/README.md)

## Development
This project uses [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) to manage dev environment.  Once installed:
1. install packages with `poetry install`
2. run tests with `poetry run pytest tests`

## Acknowledgements
- [tiangolo](https://github.com/tiangolo/full-stack-fastapi-postgresql) for the FastAPI project
- [jonra](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async) for the Alembic/SQLModel knowledge
- [nemd](https://github.com/nemd/) / [ironhalik](https://github.com/ironhalik/) for the inspiration and Docker hax
