up:
	docker compose up -d --build
	@echo ""
	@echo "Ticketoo Test Environment Ready"
	@echo "Nuxt 👉 http://localhost:3000"
	@echo "Django 👉 http://localhost:8000"
	@echo "Postgres 👉 localhost:5433"

down:
	docker compose down
