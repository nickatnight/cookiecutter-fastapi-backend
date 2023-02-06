
class {{ cookiecutter.project_name|title|replace(' ', '') }}Exception:
    pass


class ObjectNotFound({{ cookiecutter.project_name|title|replace(' ', '') }}Exception):
    pass
