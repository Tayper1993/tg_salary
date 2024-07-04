TAIL = 100

build:
	docker compose -f docker-compose.yaml build
up:
	docker compose -f docker-compose.yaml up -d
down:
	docker compose -f docker-compose.yaml down
pre-commit:
	pip install pre-commit && pre-commit run --all-files
