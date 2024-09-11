from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic.generics import GenericModel


T = TypeVar("T")


class IResponseBase(GenericModel, Generic[T]):  # type: ignore
    message: str = ""
    meta: Optional[Dict[str, Any]] = {}
    data: Optional[T] = None


class IGetResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Data got correctly"
    data: Optional[T] = None


class IPostResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Data created correctly"
