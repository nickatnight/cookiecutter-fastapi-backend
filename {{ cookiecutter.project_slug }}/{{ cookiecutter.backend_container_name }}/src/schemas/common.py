from typing import Generic, List, Optional, TypeVar

from pydantic.generics import GenericModel


DataType = TypeVar("DataType")


class IResponseBase(GenericModel, Generic[DataType]):
    message: str = ""
    meta: dict = {}
    data: Optional[DataType] = None


class IGetResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str = "Data got correctly"
    data: Optional[List[DataType]] = None


class IPostResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str = "Data created correctly"
