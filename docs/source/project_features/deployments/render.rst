Render
======

Render is by the easiest and quickest way to deploy your new FastAPI backend.

.. note::
   Render deployments rely on a "blueprint", which can can be found at the root of your project after its generated (in the ``render.yaml`` file).

   You can familiarize yourself with blueprints `here <https://render.com/docs/infrastructure-as-code#setup>`_.

Once you've created an account on Render and linked your GitHub account, you are ready to deploy your backend.

1. On the "Dashboard" page, click the "New" button in the top right corner.
2. Select "Blueprint" from the dropdown menu.
3. Give the project a name.
4. Press "Deploy"

Depending on the services you required during cookiecutter generations, it will take a few moments for both the database and services to deploy.
