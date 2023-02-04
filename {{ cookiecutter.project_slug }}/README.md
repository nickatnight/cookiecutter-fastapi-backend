<p align="center">
    <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions">
        <img alt="GitHub Actions status" src="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/releases"><img alt="Release Status" src="https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"></a>
</p>


# {{ cookiecutter.project_slug }}

## Architecture
<p align="center">
    <a href="#">
        <img alt="Architecture Workflow" src="https://i.imgur.com/8TEpVZk.png">
    </a>
</p>

## Usage
1. `make up`
2. visit `http://localhost:8666/v1/ping` for uvicorn server, or `http://localhost` for nginx server
3. Backend, JSON based web API based on OpenAPI: `http://localhost/v1/`
4. Automatic interactive documentation with Swagger UI (from the OpenAPI backend): `http://localhost/docs`

## Backend local development, additional details

### Migrations

{%- if cookiecutter.include_example_api == "yes" %}
Run the alembic `migrate` command to apply schema to your newly created database (at `{{ cookiecutter.db_container_name }}:5432`)
```console
$ make alembic-migrate
```

### Example script to pull data for API
The example API includes:
- [models](/src/models/meme.py)
- [schemas](/src/schemas/meme.py)
- [routes](/src/api/v1/meme.py)
- [utility](/src/core/utils.py) script to populate your local database. You will need to will need to fetch a client id and secret to use the example Reddit api. Details can be found [here](https://www.reddit.com/r/RequestABot/comments/cyll80/a_comprehensive_guide_to_running_your_reddit_bot/)
{%- elif cookiecutter.include_example_api == "no" %}

After adding some models in `src/model/`, you can run the initial making of the migrations
```console
$ make alembic-init
$ make alembic-migrate
```
Every migration after that, you can create new migrations and apply them with
```console
$ make alembic-make-migrations "cool comment dude"
$ make alembic-migrate
```
{%- endif %}

### General workflow
See the [Makefile](/Makefile) to view available commands.

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

From `./{{ cookiecutter.backend_container_name }}/` you can install all the dependencies with:

```console
$ poetry install
```

### Nginx
The Nginx webserver acts like a web proxy, or load balancer rather. Incoming requests can get proxy passed to various upstreams eg. `/:service1:8001,/static:service2:8002`

```yml
volumes:
  proxydata-vol:
...
{{ cookiecutter.nginx_container_name }}:
    image: your-registry/{{ cookiecutter.nginx_container_name }}
    # OR you can do the following
    # build:
    #   context: ./{{ cookiecutter.nginx_container_name }}
    #   dockerfile: ./Dockerfile
    environment:
      - UPSTREAMS=/:{{ cookiecutter.backend_container_name }}:8000
      - NGINX_SERVER_NAME=yourservername.com
      - ENABLE_SSL=true
      - HTTPS_REDIRECT=true
      - CERTBOT_EMAIL=youremail@gmail.com
      - DOMAIN_LIST=yourservername.com
      - BASIC_AUTH_USER=user
      - BASIC_AUTH_PASS=pass
    ports:
      - '0.0.0.0:80:80'
      - '0.0.0.0:443:443'
    volumes:
      - proxydata-vol:/etc/letsencrypt
```

Some of the envrionment variables available:
- `UPSTREAMS=/:{{ cookiecutter.backend_container_name }}:8000` a comma separated list of \<path\>:\<upstream\>:\<port\>.  Each of those of those elements creates a location block with proxy_pass in it.
- `HTTPS_REDIRECT=true` enabled a standard, ELB compliant https redirect.
- `ENABLE_SSL=true` to enable redirects to https from http
- `NGINX_SERVER_NAME` name of the server and used as path name to store ssl fullchain and privkey
- `CERTBOT_EMAIL=youremail@gmail.com` the email to register with Certbot.
- `DOMAIN_LIST` domain(s) you are requesting a certificate for.
- `BASIC_AUTH_USER` username for basic auth.
- `BASIC_AUTH_PASS` password for basic auth.

When SSL is enabled, server will install Cerbot in standalone mode and add a new daily periodic script to `/etc/periodic/daily/` to run a cronjob in the background. This allows you to automate cert renewing (every 3 months). See [docker-entrypoint]({{ cookiecutter.nginx_container_name }}/docker-entrypoint.sh) for details.

{%- if cookiecutter.deployments == "yes" %}
### Deployments
A common scenario is to use an orchestration tool, such as docker swarm, to deploy your containers to the cloud (DigitalOcean). This can be automated via GitHub Actions workflow. See [main.yml](/.github/workflows/main.yml) for more.

You will be required to add `secrets` in your repo settings:
- DIGITALOCEAN_TOKEN: your DigitalOcean api token
- REGISTRY: container registry url where your images are hosted
- POSTGRES_PASSWORD: password to postgres database
- STAGING_HOST_IP: ip address of the staging droplet
- PROD_HOST_IP: ip address of the production droplet
- SSH_KEY: ssh key of user connecting to server (`ubuntu` in this case)
{%- endif %}