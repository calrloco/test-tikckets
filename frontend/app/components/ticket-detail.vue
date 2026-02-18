<script setup lang="ts">
import type {TicketItem} from "~/types";

defineProps<{
  ticket: TicketItem
}>()
</script>
<template>
  <li class="list-row">
    <div>
      <img class="size-10 rounded-box" src="https://images.pexels.com/photos/16882422/pexels-photo-16882422.jpeg"/>
    </div>
    <div>
      <div>{{ ticket.price }} €</div>
      <div class="text-xs capitalize font-semibold opacity-60">Seat: {{ ticket.seat }} - Sect: {{ ticket.sector }}</div>
    </div>
  </li>
</template>