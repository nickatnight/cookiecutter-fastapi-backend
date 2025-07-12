# Install uv
FROM python:{{ cookiecutter.py_version}}-slim
COPY --from=ghcr.io/astral-sh/uv:0.7.18 /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

# Compile bytecode
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

# uv Cache
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project

# Copy the project into the image
ADD . /code

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync
