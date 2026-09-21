.PHONY: help install dev backend frontend worker migrate migrate-run seed test lint format docker-up docker-down

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install backend + frontend dependencies
	cd backend && pip install -r requirements-dev.txt
	cd frontend && npm install

dev: ## Start backend + frontend dev servers
	@echo "Starting backend..."
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
	@echo "Starting frontend..."
	cd frontend && npm run dev

backend: ## Start backend only
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend: ## Start frontend only
	cd frontend && npm run dev

worker: ## Start Celery worker
	cd backend && celery -A workers.celery_app worker --loglevel=info

migrate: ## Create a new migration
	cd backend && alembic revision --autogenerate -m "$(msg)"

migrate-run: ## Run migrations
	cd backend && alembic upgrade head

seed: ## Seed database with initial data
	cd backend && python -m scripts.seed

test: ## Run tests
	cd backend && pytest -v

lint: ## Lint code
	cd backend && ruff check app/ workers/
	cd frontend && npm run lint

format: ## Format code
	cd backend && ruff format app/ workers/
	cd frontend && npm run format

docker-up: ## Start infrastructure via Docker Compose
	docker compose up -d

docker-down: ## Stop Docker Compose
	docker compose down
