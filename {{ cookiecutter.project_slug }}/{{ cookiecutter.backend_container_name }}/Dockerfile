FROM python:{{ cookiecutter.py_version}} AS base

ARG env

WORKDIR /tmp

RUN pip install uv

COPY ./pyproject.toml ./uv.lock* /tmp/

RUN uv pip compile pyproject.toml -o requirements.txt

FROM python:{{ cookiecutter.py_version}}

COPY --from=base /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ADD . /code/
WORKDIR /code
ENV PYTHONPATH=/code

EXPOSE 8000
