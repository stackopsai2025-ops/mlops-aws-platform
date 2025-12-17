SHELL := /bin/zsh

.PHONY: help lint test format build

help:
	@echo "Available commands: lint test format build"

lint:
	poetry run ruff check .

format:
	poetry run black .

test:
	poetry run pytest -q

build:
	@echo "No build step configured"
