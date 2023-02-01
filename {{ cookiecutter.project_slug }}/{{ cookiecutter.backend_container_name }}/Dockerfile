FROM python:3.9 as base

ARG env
ENV PYTHONPATH "${PYTHONPATH}:/code"

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export $(test "${env:-dev}" != "prod" && echo "--with dev") \
    -f requirements.txt \
    --output requirements.txt \
    --without-hashes

FROM python:3.9

COPY --from=base /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ADD . /code/
WORKDIR /code

EXPOSE 8000
