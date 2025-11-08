.PHONY: build up down logs shell test check dev

check:
	@docker info > /dev/null 2>&1 || (echo "Docker is not running. Starting Docker..."; open -a Docker && sleep 10 && docker info > /dev/null 2>&1 || (echo "Failed to start Docker. Please start Docker manually." && exit 1))

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f web

shell:
	docker-compose exec web bash

test:
	docker-compose exec web python -m pytest

dev: check build
	docker-compose up

clean:
	docker-compose down -v --remove-orphans

reset: down clean build up