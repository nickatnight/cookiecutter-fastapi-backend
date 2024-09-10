import logging
from typing import Any, Dict, List, Optional, Union

from pydantic import (
    AnyHttpUrl,
    Field,
    PostgresDsn,
    ValidationInfo,
    field_validator,
    validator,
)
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: Optional[str] = Field(..., env="NGINX_HOST")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    LOG_LEVEL: int = Field(default=logging.INFO, env="LOG_LEVEL")

    VERSION: str = Field(default="", env="VERSION")
    DEBUG: bool = Field(default=True, env="DEBUG")

    POSTGRES_USER: str = Field(default="", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(default="", env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(default="", env="POSTGRES_HOST")
    POSTGRES_PORT: str = Field(default="", env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(default="", env="POSTGRES_DB")
    POSTGRES_URL: Union[Optional[PostgresDsn], Optional[str]] = None

    REDIS_HOST: str = Field(default="", env="REDIS_HOST")
    REDIS_PORT: str = Field(default="", env="REDIS_PORT")

    DB_POOL_SIZE: int = Field(default=83, env="DB_POOL_SIZE")
    WEB_CONCURRENCY: int = Field(default=9, env="WEB_CONCURRENCY")
    MAX_OVERFLOW: int = Field(default=64, env="MAX_OVERFLOW")
    POOL_SIZE: Optional[int] = None

    @validator("POOL_SIZE", pre=True)
    def build_pool(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, int):
            return v

        return max(values.get("DB_POOL_SIZE") // values.get("WEB_CONCURRENCY"), 5)  # type: ignore

    @field_validator("POSTGRES_URL", mode="before")
    @classmethod
    def build_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOST"),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        ).unicode_string()


settings = Settings()
