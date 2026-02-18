<template>
  <SearchInput :default_value="search" v-model:search="search"/>
  <div class="container mx-auto flex flex-col items-center">
    <div class="grid lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-4">
      <Card @select="setSelected" v-for="event in data?.results" :key="event.id" :event="event"/>
    </div>
  </div>
  <div class="grid place-items-center my-10">
    <div v-if="(data?.results)?.length" class="join">
      <button @click="goToPage(currentPage - 1)" :disabled="!data.previous" class="join-item btn">« Prev
      </button>
      <button class="join-item btn">{{ currentPage }}</button>
      <button @click="goToPage(currentPage + 1)" :disabled="!data.next" class="join-item btn">Next »</button>
    </div>
  </div>
  <EventDetail @close="clearSelected" :event="selected"/>
</template>

<script setup lang="ts">
import type {TicketEvent} from "~/types";
import Card from "~/components/card.vue";
import SearchInput from "~/components/search-input.vue";

interface EventsResponse {
  results: TicketEvent[];
  count: number;
  next?: string;
  previous?: string;
}

const config = useRuntimeConfig()
const route = useRoute()
const router = useRouter()
const baseURL = import.meta.server ? config.apiInternalBase : config.public.apiBase
const search = ref(route.query.q as string ?? '')
const selected = ref<TicketEvent | null>(null)
const {data} = await useFetch<EventsResponse>('/api/events/', {
  baseURL,
  query: computed(() => ({q: (route.query.q as string || '').trim() || undefined, page: route.query.page || 1})),
})
const currentPage = computed(() => {
  return Number(route.query.page ?? 1)
})
// update search param and triggers fetch
watch(search, (value: string) => {
  const trimmed = value.trim()
  const next_q: Record<string, any> = {...route.query}

  if (trimmed) {
    next_q.q = trimmed
  } else delete next_q.q
  delete next_q.page

  next_q.page = 1

  router.replace({query: next_q})
})

function goToPage(page: number) {
  const next_q: Record<string, any> = {...route.query}
  if (page <= 1) delete next_q.page
  else next_q.page = String(page)

  router.push({query: next_q})
}

function setSelected(event: TicketEvent) {
  selected.value = event
}

function clearSelected() {
  selected.value = null
}
</script>