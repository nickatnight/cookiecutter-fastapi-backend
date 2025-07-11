{%- if cookiecutter.use_celery == "yes" %}from .worker import celery_app


__all__ = ("celery_app",)
{%- endif %}