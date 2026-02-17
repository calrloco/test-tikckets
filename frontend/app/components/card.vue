<script setup lang="ts">
import type {TicketEvent} from "~/types";

defineProps<{
  event: TicketEvent
}>()
</script>

<template>
  <div class="card w-96 bg-base-100 card-md shadow-sm">
    <div class="card-body">
      <h2 class="card-title">{{ event.title }}</h2>
      <p>{{ event.city }} / {{ event.place }}</p>
      <p>{{ event.start_datetime }}</p>
      <div class="justify-end card-actions">
        <button class="btn">Biglietti</button>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>