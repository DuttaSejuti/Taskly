<template>
  <button
    @click="emitClick"
    class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
  >
    {{ buttonLabel }}
  </button>
</template>

<script setup>
defineProps({
  buttonLabel: String
});

const emit = defineEmits(['click']);

const emitClick = () => emit('click');
</script>
