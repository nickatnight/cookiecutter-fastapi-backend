pytest:
	@echo "Running pytest"
	uv run pytest tests/

dockertest:
	@echo "Running Docker build tests"
	uv run sh tests/test_docker_build.sh

test: pytest dockertest
