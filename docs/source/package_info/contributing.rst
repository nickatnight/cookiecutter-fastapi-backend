Contributing to Cookiecutter FastAPI Backend
============================================

This is an open-source project and contributions are always welcome. The project has strict linting rules, so please be sure to following existing patterns and conventions.

.. note::

    This section assumes you have Python 3.9+ installed on your system


Setting Up Your Development Environment
---------------------------------------

This project uses `Poetry <https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions>`_ to manage dev environment.  Once installed:

1. install packages with `poetry install`

Pre-commit:

1. Install pre-commit hooks with `pre-commit install`
2. Run hooks with `pre-commit run --all-files`


Running Tests
-------------

The project uses ``pytest`` for testing. To run the test suite, use the following command:

.. code-block:: bash

    $ make test
