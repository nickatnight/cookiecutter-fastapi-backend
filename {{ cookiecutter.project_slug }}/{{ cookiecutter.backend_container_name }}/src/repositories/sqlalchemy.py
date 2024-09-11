import logging
from typing import Any, Generic, List, Optional, Type, TypeVar

from sqlalchemy.orm import Session
from sqlmodel import SQLModel, select

from src.interfaces.repository import IRepository


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)
logger: logging.Logger = logging.getLogger(__name__)


class BaseSQLAlchemyRepository(IRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    _model: Type[ModelType]

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, obj_in: CreateSchemaType, **kwargs: Any) -> ModelType:
        logger.info(f"Inserting new object[{obj_in.__class__.__name__}]")

        db_obj = self._model.from_orm(obj_in)
        add = kwargs.get("add", True)
        flush = kwargs.get("flush", True)
        commit = kwargs.get("commit", True)

        if add:
            self.db.add(db_obj)

        # Navigate these with caution
        if add and commit:
            try:
                self.db.commit()
                self.db.refresh(db_obj)
            except Exception as exc:
                logger.error(exc)
                self.db.rollback()

        elif add and flush:
            self.db.flush()

        return db_obj

    def get(self, **kwargs: Any) -> Optional[ModelType]:
        logger.info(f"Fetching [{self._model.__class__.__name__}] object by [{kwargs}]")

        query = select(self._model).filter_by(**kwargs)  # type: ignore
        response = self.db.execute(query)
        scalar: Optional[ModelType] = response.scalar_one_or_none()

        # if not scalar:
        #     raise ObjectNotFound(f"Object with [{kwargs}] not found.")

        return scalar

    def update(self, obj_current: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        logger.info(f"Updating [{self._model.__class__.__name__}] object with [{obj_in}]")

        update_data = obj_in.dict(
            exclude_unset=True
        )  # This tells Pydantic to not include the values that were not sent

        for field in update_data:
            setattr(obj_current, field, update_data[field])

        self.db.add(obj_current)
        self.db.commit()
        self.db.refresh(obj_current)

        return obj_current

    def delete(self, **kwargs: Any) -> None:
        obj = self.get(**kwargs)

        self.db.delete(obj)  # type: ignore
        self.db.commit()

    def all(
        self,
        skip: int = 0,
        limit: int = 100,
        sort_field: Optional[str] = None,
        sort_order: Optional[str] = None,
    ) -> List[ModelType]:
        columns = self._model.__table__.columns

        if not sort_field:
            sort_field = "created_at"

        if not sort_order:
            sort_order = "desc"

        order_by = getattr(columns[sort_field], sort_order)()
        query = select(self._model).offset(skip).limit(limit).order_by(order_by)  # type: ignore

        response = self.db.execute(query)
        return response.scalars().all()  # type: ignore

    def f(self, **kwargs: Any) -> List[ModelType]:
        logger.info(f"Fetching [{self._model.__class__.__name__}] object by [{kwargs}]")

        query = select(self._model).filter_by(**kwargs)  # type: ignore
        response = self.db.execute(query)
        scalars: List[ModelType] = response.scalars().all()

        return scalars

    def get_or_create(self, obj_in: CreateSchemaType, **kwargs: Any) -> ModelType:
        get_instance: Optional[ModelType] = self.get(**kwargs)

        if get_instance:
            return get_instance

        instance: ModelType = self.create(obj_in)

        return instance
