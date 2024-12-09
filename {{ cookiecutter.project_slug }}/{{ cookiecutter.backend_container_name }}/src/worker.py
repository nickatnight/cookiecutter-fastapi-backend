from celery import Celery

from src.api.deps import get_redis_url


redis_url = get_redis_url()
celery_app = Celery(__name__, broker=redis_url, backend=redis_url)
# add more tasks roots here
celery_app.autodiscover_tasks(["src.core.tasks"], related_name="tasks", force=True)
