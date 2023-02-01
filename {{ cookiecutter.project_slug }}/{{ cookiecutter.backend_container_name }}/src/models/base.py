import uuid as uuid_pkg
from datetime import datetime
from typing import Optional

from sqlmodel import Column, DateTime, Field, SQLModel


class BaseModel(SQLModel):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=True,
        )
    )
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=True,
        )
    )
