import logging
from abc import ABCMeta
from typing import Generic, Optional, Type, TypeVar, Union, List
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select

from src.core.enums import SortOrder
from src.core.exceptions import ObjectNotFound


ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)

logger: logging.Logger = logging.getLogger(__name__)


class AbstractRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=ABCMeta):
    """interface for database operations"""

    model: Type[ModelType]

    def __init__(self, db: AsyncSession) -> None:
        self.db: AsyncSession = db

    async def insert(
        self,
        *,
        obj_in: CreateSchemaType,
        add: Optional[bool] = True,
        flush: Optional[bool] = True,
        commit: Optional[bool] = True,
    ) -> ModelType:
        db_obj = self.model.from_orm(obj_in)

        logger.info(f"Inserting new object[{db_obj}]")

        if add:
            self.db.add(db_obj)

        # Navigate these with caution
        if add and commit:
            try:
                await self.db.commit()
                await self.db.refresh(db_obj)
            except Exception as exc:
                logger.error(exc)
                await self.db.rollback()

        elif add and flush:
            await self.db.flush()

        return db_obj

    async def get(self, *, ref_id: Union[UUID, str]) -> ModelType:
        logger.info(f"Fetching [{self.model}] object by [{ref_id}]")

        query = select(self.model).where(getattr(self.model, "ref_id") == ref_id)
        response = await self.db.execute(query)
        scalar: Optional[ModelType] = response.scalar_one_or_none()

        if not scalar:
            raise ObjectNotFound(f"Object with [{ref_id}] not found.")
    
        return scalar

    async def update(
        self,
        *,
        obj_current: ModelType,
        obj_in: Union[UpdateSchemaType, ModelType],
    ) -> ModelType:
        logger.info(f"Updating [{self.model}] object with [{obj_in}]")

        update_data = obj_in.dict(
            exclude_unset=True
        )  # This tells Pydantic to not include the values that were not sent

        for field in update_data:
            setattr(obj_current, field, update_data[field])

        self.db.add(obj_current)
        await self.db.commit()
        await self.db.refresh(obj_current)

        return obj_current

    async def remove(self, *, ref_id: Union[UUID, str]) -> ModelType:
        query = select(self.model).where(self.model.ref_id == ref_id)
        response = await self.db.execute(query)
        obj = response.scalar_one()

        await self.db.delete(obj)
        await self.db.commit()
        return obj
    
    async def all(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        sort_field: Optional[str] = "created_at",
        sort_order: Optional[str] = SortOrder.DESC,
    ) -> List[ModelType]:
        columns = self.model.__table__.columns

        order_by = getattr(columns[sort_field], sort_order)()
        query = (
            select(self.model)
            .offset(skip)
            .limit(limit)
            .order_by(order_by)
        )

        response = await self.db.execute(query)
        return response.scalars().all()
