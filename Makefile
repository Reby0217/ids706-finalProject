.ONESHELL:
SHELL := /bin/bash
ENV_PREFIX := $(shell python3 -c "from pathlib import Path; print('venv/bin/' if Path('venv/bin/pip').exists() else '')")

.PHONY: setup format lint test clean install all docker-build-front docker-run-front

# Setup the virtual environment
setup:
	@echo "Setting up the virtual environment..."
	python3 -m venv venv
	@echo "Virtual environment created. Activate with: 'source venv/bin/activate'"
	@. venv/bin/activate && pip install --upgrade pip

format: ## Format code using black & isort.
	@echo "Formatting code..."
	$(ENV_PREFIX)isort frontend/
	$(ENV_PREFIX)black -l 79 frontend/

lint: format ## Run black, and mypy linters.
	@echo "Linting code..."
	$(ENV_PREFIX)black -l 79 --check --exclude '/(env|venv)/' frontend/apps/
	$(ENV_PREFIX)black -l 79 --check --exclude '/(env|venv)/' frontend/tests/


test: lint        ## Run tests and generate coverage report.
	@echo "Running tests..."
	$(ENV_PREFIX)pytest -v frontend/tests
	$(ENV_PREFIX)coverage run -m pytest frontend/tests
	$(ENV_PREFIX)coverage xml
	$(ENV_PREFIX)coverage html

clean: ## Clean unused files.
	@echo "Cleaning up..."
	@find . \( -name '*.pyc' -o -name '__pycache__' \) -exec rm -rf {} +

install: ## Install the project in dev mode.
	@echo "Installing dependencies..."
	$(ENV_PREFIX)pip install -r requirements.txt
	@echo "Virtual environment created. Activate with: 'source env/bin/activate'"

docker-build-front: ## Build the Docker image for the frontend
	@echo "Building the Docker image for frontend..."
	cd frontend && docker build -t frontend .

docker-run-front: ## Run the Docker container for frontend
	@echo "Running the Docker container for frontend..."
	docker run -p 5085:5005 --name frontend_container --rm frontend

all: setup install format lint test
