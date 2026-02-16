up:
	docker compose up -d --build
	@echo "Running migrations..."
	docker compose exec backend uv run python manage.py migrate
	@echo "Seeding database..."
	docker compose exec backend uv run python manage.py seed_if_empty
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Ticketoo Test Environment Ready"
	@echo "Nuxt 👉 http://localhost:3000"
	@echo "Django 👉 http://localhost:8000"
	@echo "Postgres 👉 localhost:5433"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo ""

down:
	docker compose down
