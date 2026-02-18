<script setup lang="ts">
import type {TicketEvent} from "~/types";

defineProps<{
  event: TicketEvent
}>()
const emit = defineEmits<{ (e: 'select', event: TicketEvent): void }>()
</script>
<template>
  <div class="card w-96 bg-base-100 min-h-60 card-md shadow-sm">
    <div class="card-body">
      <h2 class="card-title">{{ event.title }}</h2>
      <p>{{ event.start_datetime }}</p>
      <p>{{ event.city }} / {{ event.place }}</p>
      <div class="divider"/>
      <div class="justify-end card-actions">
        <button @click="emit('select', event)" class="btn">Biglietti</button>
      </div>
    </div>
  </div>
</template>