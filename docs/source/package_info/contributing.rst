Contributing to Cookiecutter FastAPI Backend
============================================

This is an open-source project and contributions are always welcome. The project has strict linting rules, so please be sure to following existing patterns and conventions.

.. note::

    This section assumes you have Python 3.9+ installed on your system, `uv <https://docs.astral.sh/uv/getting-started/installation/>`_ Python package manager, and `pre-commit <https://pre-commit.com/>`_ installed.

Setting Up Your Development Environment
---------------------------------------

To get started, fork the `cookiecutter-fastapi-backend` repository on GitHub and clone your fork locally.

.. code-block:: bash

    $ git clone https://github.com/nickatnight/cookiecutter-fastapi-backend.git

Sync the project:

.. code-block:: bash

    $ uv sync

Install Pre-commit hooks:

.. code-block:: bash

    $ pre-commit install

Running Tests
-------------

The project uses a combination of ``pytest`` and ``docker`` for testing. To run the test suite, use the following command:

.. code-block:: bash

    $ make test
