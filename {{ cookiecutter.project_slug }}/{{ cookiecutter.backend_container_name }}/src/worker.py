from celery import Celery


celery_app = Celery(__name__)
# add more tasks roots here
celery_app.autodiscover_tasks(["src.core.tasks"], related_name="tasks", force=True)
