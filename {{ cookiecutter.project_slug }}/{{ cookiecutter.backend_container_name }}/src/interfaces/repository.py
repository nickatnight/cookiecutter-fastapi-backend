from abc import ABCMeta, abstractmethod
from typing import Generic, List, Optional, TypeVar


T = TypeVar("T")


class IRepository(Generic[T], metaclass=ABCMeta):
    """Class representing the repository interface."""

    @abstractmethod
    async def create(self, obj_in: T, **kwargs: int) -> T:
        """Create new entity and returns the saved instance."""
        raise NotImplementedError

    @abstractmethod
    async def update(self, instance: T, obj_in: T) -> T:
        """Updates an entity and returns the saved instance."""
        raise NotImplementedError

    @abstractmethod
    async def get(self, **kwargs: int) -> T:
        """Get and return one instance by filter."""
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs: int) -> None:
        """Delete one instance by filter."""
        raise NotImplementedError

    @abstractmethod
    async def all(
        self,
        skip: int = 0,
        limit: int = 50,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> List[T]:
        """Delete one instance by filter."""
        raise NotImplementedError
