# Ticketoo Test

## Avvio ambiente

### Avvio dell'ambiente Docker

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