test:
	@echo "Running pytest"
	poetry run tests/

	@echo "Running docker build tests"
	poetry run sh tests/test_docker_build.sh


sphinx:
	@echo "Building Sphinx documentation"
	poetry run sphinx-build -M html docs/source/ docs/build/
