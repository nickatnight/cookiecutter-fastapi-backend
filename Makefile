pytest:
	@echo "Running pytest"
	uv run pytest tests/

dockertest:
	@echo "Running Docker build tests"
	uv run sh tests/test_docker_build.sh

test: pytest dockertest

sphinx:
	@echo "Building Sphinx documentation"
	uv run sphinx-build -M html docs/source/ docs/build/
