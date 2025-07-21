Quickstart
==========

To get started, install the latest version of `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_:

.. code-block:: bash

    pipx install cookiecutter

Then, generate a new project

.. note::
   You'll be prompted to enter values for the project.

   Then it'll create your Python package in the current working directory, based on those values.

Using a GitHub templates:

.. code-block:: bash

    pipx run cookiecutter gh:nickatnight/cookiecutter-fastapi-backend


Using a local template:

.. code-block:: bash

    pipx run cookiecutter cookiecutter-fastapi-backend

Using from Python:

.. code-block:: python

    from cookiecutter.main import cookiecutter

    # Create project from the cookiecutter-pypackage/ template
    cookiecutter("cookiecutter-fastapi-backend/")

    # Create project from the cookiecutter-fastapi-backend.git repo template
    cookiecutter("gh:nickatnight/cookiecutter-fastapi-backend")

Input Variables
---------------

The generator (cookiecutter) will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto generated) are:

* `project_name`: The name of the project
* `author_email`: The authors email...used for certbot
* `py_version`: The version of Python to install. Options are `3.9`, `3.10`, and `3.11`
* `db_container_name`: The name of the database container. Default `db`
* `backend_container_name`: The name of the backend container. Default `backend`
* `use_celery`: Whether to use Celery and Redis for asynchronous tasks. Default `no`
* `periodic_tasks`: Whether to use Celery Beat for periodic tasks (requires Celery). Default `no`
* `use_sentry`: Whether to use Sentry for application monitoring and error tracking. Default `no`
* `github_username`: The username of the GitHub user. Used for badge display in generated project `README.md`
* `deployments`: Deploy to your favorite platform, Render.com (and more to come). Default `none`

After using this generator, your new project (the directory created) will contain an extensive `README.md` with instructions for development, deployment, etc. You can view it `here <https://github.com/nickatnight/cookiecutter-fastapi-backend/blob/master/%7B%7B%20cookiecutter.__project_slug%20%7D%7D/README.md>`_.
