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

Quando parte l’ambiente viene eseguito automaticamente un seed iniziale di 200 eventi (se il DB è vuoto).

Vai su:

- Nuxt: http://localhost:3000

Per fermare docker:

```sh
make down
```

## Seed dati

Per rigenerare manualmente dati di test:

```sh
dcx backend uv run python manage.py seed --events 500
```

> Nota: nel container si usa `uv`, quindi i comandi Django vanno eseguiti con `uv run`.