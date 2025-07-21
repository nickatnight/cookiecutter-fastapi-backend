from enum import Enum


class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)


class SortOrder:
    ASC = "asc"
    DESC = "desc"
