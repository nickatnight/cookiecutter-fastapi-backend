from uuid import UUID

from src.models.meme import MemeBase


class IMemeCreate(MemeBase):
    pass


class IMemeRead(MemeBase):
    id: UUID
