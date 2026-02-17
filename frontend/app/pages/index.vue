<template>
  <SearchInput v-model:search="search"/>
  <div class="container mx-auto flex flex-col items-center">
    <div class="grid lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-4">
      <Card v-for="event in data?.results" :key="event.id" :event="event"/>
    </div>
  </div>
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

// fetch events
const {data} = await useFetch<EventsResponse>('/api/events/', {
  baseURL,
  query: computed(() => {
    const q = route.query.q
    const value = Array.isArray(q) ? q[0] : q
    const trimmed = (value ?? '').trim()
    return trimmed ? {q: trimmed} : {}
  }),
})

// update query param and triggers fetch
watch(search, (value: string) => {
  const trimmed = value.trim()
  const nextQuery: Record<string, any> = {...route.query}

  if (trimmed) {
    nextQuery.q = trimmed
  } else delete nextQuery.q

  router.replace({query: nextQuery})
})
</script>