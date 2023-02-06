from src.models.meme import Meme
from src.repository.base import AbstractRepository
from src.schemas.meme import IMemeCreate, IMemeUpdate


class MemeRepository(AbstractRepository[Meme, IMemeCreate, IMemeUpdate]):
    model = Meme
