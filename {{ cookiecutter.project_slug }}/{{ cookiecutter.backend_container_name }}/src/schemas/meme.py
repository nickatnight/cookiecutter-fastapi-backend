from uuid import UUID

from src.models.meme import MemeBase


class IMemeCreate(MemeBase):
    pass


class IMemeRead(MemeBase):
    ref_id: UUID


class IMemeUpdate(MemeBase):
    pass
