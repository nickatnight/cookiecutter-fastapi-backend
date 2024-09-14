all:

# docker
up:
	@echo "bringing up project...."
	docker compose up

down:
	@echo "bringing down project...."
	docker compose down

bash:
	@echo "connecting to container...."
	docker compose exec {{ cookiecutter.backend_container_name }} bash

# alembic
alembic-scaffold:
	@echo "scaffolding migrations folder..."
	docker compose exec {{ cookiecutter.backend_container_name }} alembic init migrations

alembic-init:
	@echo "initializing first migration...."
	docker compose exec {{ cookiecutter.backend_container_name }} alembic revision --autogenerate -m "init"

alembic-make-migrations:
	@echo "creating migration file...."
	docker compose exec {{ cookiecutter.backend_container_name }} alembic revision --autogenerate -m "add year"

alembic-migrate:
	@echo "applying migration...."
	docker compose exec {{ cookiecutter.backend_container_name }} alembic upgrade head

# lint
test:
	@echo "running pytest...."
	docker compose exec {{ cookiecutter.backend_container_name }} pytest --cov-report xml --cov=src tests/

lint:
	@echo "running ruff...."
	docker compose exec {{ cookiecutter.backend_container_name }} ruff check src

black:
	@echo "running black...."
	docker compose exec {{ cookiecutter.backend_container_name }} black .

mypy:
	@echo "running mypy...."
	docker compose exec {{ cookiecutter.backend_container_name }} mypy src/

# database
init-db: alembic-init alembic-migrate
	@echo "initializing database...."
	docker compose exec {{ cookiecutter.backend_container_name }} python3 src/db/init_db.py

# misc
check: BREW-exists
BREW-exists: ; @which brew > /dev/null

hooks: check
	@echo "installing pre-commit hooks...."
	pre-commit install
