from datetime import datetime, timezone

from pydantic import BaseConfig
from sqlmodel import Column, DateTime, Field, SQLModel

from src.models.base import BaseModel


class MemeBase(SQLModel):
    submission_id: str = Field(...)
    submission_url: str = Field(...)
    submission_title: str = Field(...)
    permalink: str = Field(...)
    author: str = Field(...)
    timestamp: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
        )
    )

    class Config(BaseConfig):
        json_encoder = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc).isoformat(),
        }
        schema_extra = {
            "example": {
                "id": 1,
                "ref_id": "1234-43143-3134-13423",
                "submission_id": "nny218",
                "submission_title": "This community is so nice. Helps me hodl.",
                "submission_url": "https://i.redd.it/gdv6tbamkb271.jpg",
                "permalink": "/r/dogecoin/comments/nnvakd/still_holding_keep_the_faith/",
                "author": "42points",
                "timestamp": "2004-09-16T23:59:58.75",
                "created_at": "2004-09-16T23:59:58.75",
            }
        }


class Meme(BaseModel, MemeBase, table=True):
    pass
