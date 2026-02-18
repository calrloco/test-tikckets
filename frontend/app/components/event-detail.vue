<script setup lang="ts">
import type {TicketEvent} from "~/types";
import TicketDetail from "~/components/ticket-detail.vue";
import Sort from "~/components/sort.vue";
import {computed, ref} from 'vue'

const {event} = defineProps<{
  event: TicketEvent | null
}>()

const emit = defineEmits(['close'])

const sortDirection = ref<'asc' | 'desc'>('asc')

type TicketItem = TicketEvent['ticket_items'][number]

function getTicketPrice(ticket: TicketItem): number {
  const value = (ticket as any).price ?? (ticket as any).price_cents ?? (ticket as any).amount ?? 0
  return Number(value)
}

const sortedTickets = computed<TicketItem[]>(() => {
  if (!event) return []

  return [...event.ticket_items].sort((a, b) => {
    const pa = getTicketPrice(a)
    const pb = getTicketPrice(b)
    return sortDirection.value === 'asc' ? pa - pb : pb - pa
  })
})

onMounted(() => {
  const handler = (e: KeyboardEvent) => {
    if (e.key === 'Escape') emit('close')
  }
  window.addEventListener('keydown', handler)
  onUnmounted(() => window.removeEventListener('keydown', handler))
})
</script>
<template>
  <Transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
  >
    <div v-if="event" @click.self="emit('close')"
         class="overflow-hidden fixed inset-0 z-100 overflow-y-auto grid place-items-center bg-black/50 backdrop-blur-sm">
      <p @click.self="emit('close')" class="kbd absolute top-5 right-5">esc</p>
      <div class="bg-base-100 card  shadow-md md:min-w-[50vh]">
        <button @click="emit('close')" class="absolute btn btn-ghost btn-circle top-2 right-2">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
               stroke="currentColor"
               class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12"/>
          </svg>
        </button>
        <div class="card-body">
          <div class="px-4 pt-4">
            <h3 class="text-2xl card-title">{{ event.title }}</h3>
            <div class="divider"/>
            <p class="text-lg font-bold card-title">{{ event.city }}</p>
            <span class="pb-2 text-xs opacity-60 tracking-wide">{{ event.start_datetime }}</span>
          </div>
          <div>
            <div class="pl-2">
              <p class="py-3">Prezzo</p>
              <Sort @sort="sortDirection = $event"/>
            </div>
            <p class="p-4 pb-2 text-xs opacity-60 tracking-wide">Biglietti</p>
            <TransitionGroup
                tag="ul"
                class="list rounded-box max-h-[50vh] overflow-y-scroll"
                enter-active-class="transition-all duration-200 ease-out"
                enter-from-class="opacity-0 -translate-y-2"
                enter-to-class="opacity-100 translate-y-0"
                leave-active-class="transition-all duration-150 ease-in absolute w-full"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0 translate-y-2"
                move-class="transition-transform duration-200"
            >
              <TicketDetail v-for="ticket in sortedTickets" :ticket="ticket" :key="ticket.id"/>
            </TransitionGroup>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>