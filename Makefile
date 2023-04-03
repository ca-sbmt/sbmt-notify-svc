# Makefile

# Variables
IMAGE_NAME := ca-ai-template
CONTAINER_NAME := ca-ai-template-app

# Docker commands

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container in development mode
.PHONY: run-dev
run-dev:
	docker run -d --name $(CONTAINER_NAME) -p 8000:8000 -e ENV_TYPE=dev $(IMAGE_NAME)

# Run the Docker container in production mode
.PHONY: run-prod
run-prod:
	docker run -d --name $(CONTAINER_NAME) -p 8000:8000 -e ENV_TYPE=prod $(IMAGE_NAME)

# Stop and remove the Docker container
.PHONY: stop
stop:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

# Remove the Docker image
.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME)

# Local commands

# Check if Python 3.9 or higher is installed
.PHONY: check-python
check-python:
	@python3 -c "import sys; assert sys.version_info >= (3, 9), 'Python 3.9 or higher is required'"

# Install Poetry
.PHONY: install-poetry
install-poetry: check-python
	curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
.PHONY: install-dependencies
install-dependencies: check-python
	poetry install

# Run the application locally in development mode
.PHONY: run-local
run-local: check-python
	ENV_TYPE=local poetry run python run.py

# Run the application locally with all dependencies in a virtual environment
.PHONY: run-local-with-deps
run-local-with-deps: install-dependencies
	ENV_TYPE=local poetry run python run.py

# Run the application in Docker with all dependencies
.PHONY: run-docker-with-deps
run-docker-with-deps: build run-dev

# Run tests using pytest
.PHONY: test
test: install-dependencies
	poetry run pytest tests/
