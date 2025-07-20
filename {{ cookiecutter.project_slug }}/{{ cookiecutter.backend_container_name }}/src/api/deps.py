from typing import cast

from redis import Redis

from src.core.config import settings


def get_redis_url() -> str:
    return settings.REDIS_URL or ""


def get_redis_client() -> Redis:
    redis = Redis.from_url(
        get_redis_url(),
        max_connections=10,
        encoding="utf8",
        decode_responses=True,
    )
    return cast(Redis, redis)
