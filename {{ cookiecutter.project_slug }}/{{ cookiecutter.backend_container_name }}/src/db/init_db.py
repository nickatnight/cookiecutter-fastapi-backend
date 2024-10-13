import logging

from src.db.session import SessionLocal


logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


def create_init_data() -> None:
    with SessionLocal() as session:
        # Add initial data here eg session.add(Model(field=value))
        session.add()
        session.add()

        session.commit()


def main() -> None:
    logger.info("Creating initial data")
    create_init_data()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
