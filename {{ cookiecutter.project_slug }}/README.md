<p align="center">
    <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions">
        <img alt="GitHub Actions status" src="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases"><img alt="Release Status" src="https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"></a>
</p>

# {{ cookiecutter.project_slug }}

## Usage
1. `make up`
2. visit `http://localhost:8666/v1/ping` for uvicorn server
3. Backend, JSON based web API based on OpenAPI: `http://localhost/v1/`
4. Automatic interactive documentation with Swagger UI (from the OpenAPI backend): `http://localhost/docs`

## Backend local development, additional details

Initialize first migration (project must be up with docker compose up and contain no 'version' files)
```shell
$ make alembic-init
```

Create new migration file
```shell
$ docker compose exec {{ cookiecutter.backend_container_name }} alembic revision --autogenerate -m "some cool comment"
```

Apply migrations
```shell
$ make alembic-migrate
```

### Migrations
Every migration after that, you can create new migrations and apply them with
```console
$ make alembic-make-migrations "cool comment dude"
$ make alembic-migrate
```

### General workflow
See the [Makefile](/Makefile) to view available commands.

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

From `./{{ cookiecutter.backend_container_name }}/` you can install all the dependencies with:

```console
$ poetry install
```

### pre-commit hooks
If you haven't already done so, download [pre-commit](https://pre-commit.com/) system package and install. Once done, install the git hooks with
```console
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

### Deployments
{%- if cookiecutter.cloud_provider == "Fly.io" %}
#### Fly.io
GitHub Actions are responsible for deploying the fly. Be sure to set `FLY_API_TOKEN` as a Actions repostiroy secret. View ./.github/workflows/deploy.yml for more details, or read the [Fly.io](https://fly.io/docs/python/frameworks/fastapi/)
{%- endif %}
