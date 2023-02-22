from src.models.meme import Meme
from src.repositories.sqlalchemy import BaseSQLAlchemyRepository
from src.schemas.meme import IMemeCreate, IMemeUpdate


class MemeRepository(BaseSQLAlchemyRepository[Meme, IMemeCreate, IMemeUpdate]):
    _model = Meme
