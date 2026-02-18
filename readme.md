w# Ticketoo Test

## Avvio ambiente

### Avvio dell'ambiente Docker

Prima del primo avvio, crea il file `.env` a partire da `.env.example`:

```sh
cp .env.example .env
```

Per avviare l'intero stack (PostgreSQL, Backend Django e Frontend Nuxt) eseguire:

```sh
make up
````

Al termine dell'avvio, dovresti vedere le porte per ogni servizio in console:

```
Ticketoo Dev Environment Ready

Nuxt     👉  http://localhost:3000
Django   👉  http://localhost:8000
Postgres 👉  localhost:5433
```

### Per arrestare Docker

```sh
make down
```

### Seeding

Per popolare il database con altri dati di test eseguire con il numero di eventi desiderato:

```sh
dcx backend uv run python manage.py seed --events 500
```
