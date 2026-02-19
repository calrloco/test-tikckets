# Ticketoo Test

---

## Struttura del progetto

- `backend/` Django 5.1 + DRF (API)
- `frontend/` Nuxt 4
- `docker-compose.yml` Stack completo (PostgreSQL + Backend + Frontend)
- `Makefile` Comandi (`make up`, `make down`)

---

## Avvio ambiente

Avviare l’intero stack:

```sh
make up
```

Output atteso:

```
Ticketoo Test Environment Ready

Nuxt     👉  http://localhost:3000
Django   👉  http://localhost:8000
Postgres 👉  localhost:5433
```

Per fermare:

```sh
make down
```

---

## Backend

### Endpoint principale

```
GET /api/events/
```

Query params:

- `q` ricerca full-text su `title` e `city`
- `page` paginazione (DRF PageNumberPagination)

Esempi:

```
/api/events/?q=rome
/api/events/?page=2
/api/events/?q=rome&page=2
```

---

### Ricerca full-text (PostgreSQL)

La ricerca è implementata tramite PostgreSQL Full Text Search con:

- `SearchVector`
- `SearchQuery`
- `SearchRank`
- `indicizzazione GIN`

### Logica di query:

- Filtra solo eventi futuri (`start_datetime >= now`)
- Applica ricerca full-text su `title` + `city`

---

### Seed dati

È disponibile un comando per generare dati fake:

```sh
docker compose exec backend uv run python manage.py seed
```

---

## Frontend

### `frontend/app/pages/index`

- Lista eventi con paginazione
- Ricerca sincronizzata con URL (`?q=`)
- Stato guidato da query string

### Dettaglio biglietti

- Apertura tramite modale `frontend/app/components/ticket-detail`
- Ordinamento client-side per prezzo

---

## Scelte architetturali

- Docker Compose per ambiente riproducibile
- Full-text search con GIN index per performance reali
- SSR Nuxt con doppia base URL (interna container + pubblica browser)
- Prefetch lato ORM per evitare N+1
- URL come fonte unica di stato (ricerca + paginazione)