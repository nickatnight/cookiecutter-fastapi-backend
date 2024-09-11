from redis import Redis

from src.core.config import settings


def get_redis_client() -> Redis:
    redis = Redis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        max_connections=10,
        encoding="utf8",
        decode_responses=True,
    )
    return redis
