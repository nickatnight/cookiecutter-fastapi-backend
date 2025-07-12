Continuous Integration and Deployment
====================================

The project uses a typical CI/CD workflow when developing projects.

Any opened pull request to main branch will run:

1. Linting
2. Unit tests
3. Code coverage (automatically includes Codecov reporting)

Releasing and tagging is also supported. When a developer is on ``main`` branch and pushed a new tag:

1. A new tag is created
2. A new GitHub release is created

You can view more details in the `GitHub Actions workflows <https://github.com/nickatnight/cookiecutter-fastapi-backend/tree/master/.github/workflows>`_
