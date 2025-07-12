Quickstart
==========

To get started, install the latest version of `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_:

.. code-block:: bash

    pip install cookiecutter

Then, generate a new project

.. note::
   You'll be prompted to enter values for the project.

   Then it'll create your Python package in the current working directory, based on those values.

Using a GitHub templates:

.. code-block:: bash

    cookiecutter gh:nickatnight/cookiecutter-fastapi-backend.git


Using a local template:

.. code-block:: bash

    cookiecutter ookiecutter-fastapi-backend

Using from Python:

.. code-block:: python

    from cookiecutter.main import cookiecutter

    # Create project from the cookiecutter-pypackage/ template
    cookiecutter("cookiecutter-fastapi-backend/")

    # Create project from the cookiecutter-fastapi-backend.git repo template
    cookiecutter("gh:nickatnight/cookiecutter-fastapi-backend.git")
