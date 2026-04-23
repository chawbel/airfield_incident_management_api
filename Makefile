up:
	docker-compose up --build -d
	docker-compose logs -f api

down:
	docker-compose down

logs:
	docker-compose logs -f

restart:
	docker-compose down && docker-compose up --build

migrate:
	docker-compose exec api alembic upgrade head

shell:
	docker-compose exec api bash
