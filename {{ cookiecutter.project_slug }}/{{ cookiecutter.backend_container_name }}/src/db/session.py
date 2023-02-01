import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import settings


logger = logging.getLogger(__name__)


engine = create_async_engine(
    settings.POSTGRES_URL,
    echo=True,
    future=True,
    pool_size=settings.POOL_SIZE,
    max_overflow=settings.MAX_OVERFLOW,
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def on_startup():
    logger.info("FastAPI app running...")


# async def add_postgresql_extension() -> None:
#     async with db():
#         query = text("CREATE EXTENSION IF NOT EXISTS pg_trgm")
#         return await db.session.execute(query)


async def get_session() -> AsyncSession:
    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async with async_session() as session:
        yield session
