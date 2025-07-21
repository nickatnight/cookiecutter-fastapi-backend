class {{ cookiecutter.project_name|title|replace(' ', '') }}Exception(Exception):
    pass


class ObjectNotFound({{ cookiecutter.project_name|title|replace(' ', '') }}Exception):
    pass
