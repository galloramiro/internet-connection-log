# Makefile
# ============================================================================
# Globals
# ============================================================================
CONTAINER_NAME:=internet-connection-log
TAG:=$(shell git log -1 --pretty=format:"%H")

# ============================================================================
# Development Commands
# ============================================================================

.PHONY: build
build: ## Build the docker image.
	docker build \
		--build-arg VERSION=$(TAG) \
		-t $(CONTAINER_NAME) . \
		--network=host

.PHONY: run
run: ## Run program.
	docker run -it \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/tests:/app/tests \
        --env-file .env \
        --network=host \
		$(CONTAINER_NAME) \
		/bin/bash -c "poetry run python /app/src/main.py"

.PHONY: lock-dependencies
lock-dependencies: ## Lock poetry dependencies.
	docker run \
		-v `pwd`:/app \
		--env-file .env \
		-it $(CONTAINER_NAME) poetry lock \

.PHONY: console
console: ## Run service linting.
	docker run -it \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/tests:/app/tests \
		--env-file .env \
		$(CONTAINER_NAME) \
		/bin/bash

.PHONY: lint
lint: ## Run service linting.
	docker run \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/.pylintrc:/app/.pylintrc \
		--env-file .env \
		$(CONTAINER_NAME) \
		poetry run pylint /app/src

.PHONY: test
test: ## Run service tests.
	docker run \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/tests:/app/tests \
        --env-file .env \
		$(CONTAINER_NAME) \
		/bin/bash -c "poetry run pytest /app/tests -vv"

.PHONY: debug
debug: ## Run service debugging tool.
	docker run -it \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/tests:/app/tests \
		--env-file .env \
		$(CONTAINER_NAME) \
		/bin/bash -c "poetry run pytest ${test_dir} -s -vv"

.PHONY: black
black: ## Run code style tool.
	docker run -it \
		-v $(shell pwd)/src:/app/src \
		-v $(shell pwd)/tests:/app/tests \
		--env-file .env \
		$(CONTAINER_NAME) \
		/bin/bash -c "poetry run python -m black ."