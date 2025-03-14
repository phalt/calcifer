help:
	@echo Developer commands for CalciferPi
	@echo
	@grep -E '^[ .a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

install:  ## Install requirements ready for development
	poetry install

deploy-docs:  ## Build and deploy the documentation
	mkdocs build
	mkdocs gh-deploy

release:  ## Build a new version and release it
	poetry build
	poetry publish

mypy: ## Run a static syntax check
	poetry run mypy .

format: ## Format the code correctly
	poetry run ruff format .

clean:  ## Clear any cache files and test files
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf site/
	rm -rf dist/
	rm -rf **/__pycache__
	rm -rf **/*.pyc

test:  ## Run tests
	pytest -vvv

shell:  ## Run an ipython shell
	poetry run ipython
