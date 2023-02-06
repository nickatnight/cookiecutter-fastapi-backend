import logging
from typing import AsyncGenerator

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.api.deps import get_redis_client
from src.core.config import settings


logger = logging.getLogger(__name__)


engine = create_async_engine(
    settings.POSTGRES_URL,
    echo=True,
    future=True,
    pool_size=settings.POOL_SIZE,
    max_overflow=settings.MAX_OVERFLOW,
)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def on_startup() -> None:
    redis_client = await get_redis_client()
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    logger.info("FastAPI app running...")


# async def add_postgresql_extension() -> None:
#     async with db():
#         query = text("CREATE EXTENSION IF NOT EXISTS pg_trgm")
#         return await db.session.execute(query)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async with SessionLocal() as session:
        yield session
