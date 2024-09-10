from abc import ABCMeta, abstractmethod
from typing import Any, List, Optional


class IRepository(metaclass=ABCMeta):
    """Class representing the repository interface."""

    @abstractmethod
    def create(self, obj_in: Any, **kwargs: Any) -> Any:
        """Create new entity and returns the saved instance."""
        raise NotImplementedError

    @abstractmethod
    def update(self, obj_current: Any, obj_in: Any) -> Any:
        """Updates an entity and returns the saved instance."""
        raise NotImplementedError

    @abstractmethod
    def get(self, **kwargs: Any) -> Optional[Any]:
        """Get and return one instance by filter."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, **kwargs: Any) -> None:
        """Delete one instance by filter."""
        raise NotImplementedError

    @abstractmethod
    def all(
        self,
        skip: int = 0,
        limit: int = 50,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> List[Any]:
        """Get all instances."""
        raise NotImplementedError

    @abstractmethod
    def f(self, **kwargs: Any) -> List[Any]:
        """Filter instances"""
        raise NotImplementedError

    @abstractmethod
    def get_or_create(self, obj_in: Any, **kwargs: Any) -> Any:
        """Get or create an instance"""
        raise NotImplementedError
