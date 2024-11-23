{%- if cookiecutter.use_celery == "yes" %}from .worker import app as celery_app


__all__ = ("celery_app",){%- endif %}