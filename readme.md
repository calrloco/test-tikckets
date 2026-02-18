# Ticketoo Test

## Avvio ambiente

Prima del primo avvio crea il file `.env`:

```sh
cp .env.example .env
```

Avvia lo stack (Postgres, Backend, Frontend):

```sh
make up
```

Quando parte l’ambiente viene eseguito automaticamente un seed iniziale di 1000 eventi (se il DB è vuoto).

Vai su:

- Nuxt: http://localhost:3000

Per fermare docker:

```sh
make down
```

## Seed dati

Per inserire nuovi dati di test:

```sh
docker compose exec backend uv run python manage.py seed --events 500
```