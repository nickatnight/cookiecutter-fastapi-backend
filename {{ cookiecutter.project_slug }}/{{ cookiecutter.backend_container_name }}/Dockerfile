FROM python:{{ cookiecutter.py_version}} as base

ARG env

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export $(test "${env:-dev}" != "prod" && echo "--with dev") \
    -f requirements.txt \
    --output requirements.txt \
    --without-hashes

FROM python:{{ cookiecutter.py_version}}

COPY --from=base /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ADD . /code/
WORKDIR /code
ENV PYTHONPATH=/code

EXPOSE 8000
