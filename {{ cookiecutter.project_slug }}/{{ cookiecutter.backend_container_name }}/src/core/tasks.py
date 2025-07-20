from src.worker import celery_app


@celery_app.task
def hello_world_task() -> None:
    print("Hello World")
