DigitalOcean
============

There a couple of house keeping steps to take before deploying to DigitalOcean. You can
read more about the steps `here <https://docs.digitalocean.com/products/app-platform/how-to/deploy-from-github-actions/#prerequisites>`_.

.. note::

   Be sure you have the official `DigitalOcean GitHub App <https://cloud.digitalocean.com/apps/github/install>`_ installed in your GitHub account.
   It is recommended to only allow the app to access the repositories you want to deploy.

   Meaning, once your project has been scaffolded with this cookiecutter, you'll have to push
   it to GitHub for it to be available to DigitalOcean.

Once the prerequisites are met:
--------------------------------

Provision the app using the provided script ``bin/provision-app.sh``.

.. code-block:: bash

   $ ./bin/provision-app.sh

This creates app based on the spec file ``digitalocean.yaml`` at the root of the project. The services will get created, but
will fail deployment, which is expected. They fail because we've deployed the app from the CLI without any of the environment variables.

Ensure the following variables are in the Apps Environment Variables:

- ``POSTGRES_USER``
- ``POSTGRES_PASSWORD``
- ``POSTGRES_DB``
- ``POSTGRES_HOST``
- ``POSTGRES_PORT``

They can be found in the database settings within your Apps deployment.

Once saved, the deployment for the app will get re-triggered, and the services will be deployed successfully. Now, any merges into your main branch will trigger a deployment.
