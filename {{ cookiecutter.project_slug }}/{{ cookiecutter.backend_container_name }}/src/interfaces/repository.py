from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, TypeVar, Union, List

from sqlmodel import SQLModel


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class IRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta):
    """Class representing the repository interface."""

    @abstractmethod
    async def create(self, obj_in: CreateSchemaType, **kwargs: int) -> ModelType:
        """Create new entity and returns the saved instance."""
        raise NotImplementedError

    @abstractmethod
    async def update(self, instance: ModelType, obj_in: Union[UpdateSchemaType, ModelType]) -> ModelType:
        """Updates an entity and returns the saved instance."""
        raise NotImplementedError

    @abstractmethod
    async def get(self, **kwargs) -> ModelType:
        """Get and return one instance by filter."""
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs) -> None:
        """Delete one instance by filter."""
        raise NotImplementedError
    
    @abstractmethod
    async def all(self, skip: int = 0, limit: int = 100, sort_field: Optional[str] = None, sort_order: Optional[str] = None) -> List[ModelType]:
        """Delete one instance by filter."""
        raise NotImplementedError
