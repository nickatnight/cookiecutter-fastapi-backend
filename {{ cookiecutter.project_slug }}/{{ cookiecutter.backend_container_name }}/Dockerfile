FROM python:{{ cookiecutter.py_version}} AS base

ARG env

WORKDIR /tmp

RUN pip install uv

COPY ./requirements*.txt /tmp/

RUN uv pip install -r requirements.txt $(test "${env:-dev}" != "prod" && echo "-r requirements-dev.txt")

FROM python:{{ cookiecutter.py_version}}

COPY --from=base /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages

ADD . /code/
WORKDIR /code
ENV PYTHONPATH=/code

EXPOSE 8000
