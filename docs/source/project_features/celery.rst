Asynchronous Tasks with Celery
==============================

The project uses Celery for asynchronous tasks, with Celery beat for task scheduling, and Redis is used as the broker by default.

.. note::

   You can read more here on how to get started with `Celery <https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html>`_

FastAPI comes with built-in `BackgroundTasks <https://fastapi.tiangolo.com/tutorial/background-tasks/>`_, however, they run in a single
process. This won't work well for more complex tasks, especially at scale. The Celery worker and beat service can scale independently of
the FastAPI application, which is how typical async applications are deployed.

Configuring Celery Workers
--------------------------

Celery workers can be configured to run on a specific number of workers. This is useful for scaling the application to handle more requests.

.. code-block:: python

  ...

  @router.get("/ping", tags=["health"])
    def pong() -> Response:
        hello_world_task.delay()
        # or a task with arguments
        my_task.delay(id=1)
        return JSONResponse({"ping": "pong!"})

You can read more about the different application settings `here <https://docs.celeryq.dev/en/v5.2.7/userguide/application.html#application>`_.


Configuring Celery Beat
-----------------------

Celery beat is used to schedule periodic tasks. It can be configured to run on a schedule, or to run on a fixed time interval.

.. code-block:: python

  # worker.py

   from celery.schedules import crontab

   ...
   app.conf.beat_schedule = {
        # Executes every Monday morning at 7:30 a.m.
        'add-every-monday-morning': {
            'task': 'src.core.tasks.add',
            'schedule': crontab(hour=7, minute=30, day_of_week=1),
            'args': (16, 16),
        },
        # Executes every 3rd minute
        'hello-every-third-minute': {
            'task': 'src.core.tasks.hello_world_task',
            'schedule': crontab(minute="*/3"),
        },
        # Executes at sunset in Melbourne
        'add-at-melbourne-sunset': {
            'task': 'src.core.tasks.melbourne_add',
            'schedule': solar('sunset', -37.81753, 144.96715),
            'args': (16, 16),
        },
    }

You can read more about the different schedule `types <https://docs.celeryq.dev/en/v5.2.7/userguide/periodic-tasks.html#crontab-schedules>`_.
