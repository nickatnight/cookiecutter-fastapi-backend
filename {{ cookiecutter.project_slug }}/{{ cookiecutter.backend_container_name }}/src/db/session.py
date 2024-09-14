from typing import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from src.core.config import settings


engine = create_engine(
    settings.POSTGRES_URL,
    echo=settings.DEBUG,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def add_postgresql_extension() -> None:
    with SessionLocal() as db:
        query = text("CREATE EXTENSION IF NOT EXISTS pg_trgm")
        db.execute(query)


def get_session() -> Generator[Session, None, None]:
    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    with SessionLocal() as session:
        yield session
