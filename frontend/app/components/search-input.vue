<template>
  <div class="flex justify-center my-10">
    <label class="input">
      <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        <g
            stroke-linejoin="round"
            stroke-linecap="round"
            stroke-width="2.5"
            fill="none"
            stroke="currentColor"
        >
          <circle cx="11" cy="11" r="8"></circle>
          <path d="m21 21-4.3-4.3"></path>
        </g>
      </svg>
      <input
          v-model="input"
          class="grow"
          placeholder="Search"
      />
    </label>
  </div>
</template>
<script setup lang="ts">
import debounce from "lodash.debounce";

const {default_value, debounce_ms} = defineProps({
  default_value: {
    type: String,
    default: ''
  },
  debounce_ms: {
    type: Number,
    default: 250
  },
});

const input = ref(default_value ?? '')
const search = defineModel<string>('search')

watch(input, debounce((value: string) => {
  search.value = value
}, debounce_ms))
</script>