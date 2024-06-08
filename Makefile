# Makefile
# ============================================================================
# Globals
# ============================================================================
CONTAINER_NAME:=internet-connection-log

# ============================================================================
# Development Commands
# ============================================================================

.PHONY: build
build: ## Build the docker image.
	docker compose build

.PHONY: run
run: ## Run program.
	docker compose stop
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry run python /app/src/main.py"

.PHONY: lock-dependencies
lock-dependencies: ## Lock poetry dependencies.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry lock"

.PHONY: console
console: ## Run service linting.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash

.PHONY: lint
lint: ## Run service linting.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry run pylint /app/src"

.PHONY: test
test: ## Run service tests.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry run pytest /app/tests -vv"

.PHONY: debug
debug: ## Run service debugging tool.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry run pytest ${test_dir} -s -vv"

.PHONY: black
black: ## Run code style tool.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry run python -m black ."

.PHONY: get-servers
get-servers: ## Run code style tool.
	docker compose run --rm $(CONTAINER_NAME) /bin/bash -c "speedtest --servers"

.PHONY: get poetry virtualenv
get-virtual-env:
	docker-compose run --rm $(CONTAINER_NAME) /bin/bash -c "poetry env info -p"

