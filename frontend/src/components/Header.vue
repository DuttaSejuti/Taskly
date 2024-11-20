<template>
  <h1 class="text-lg font-bold mb-4 text-center">Taskly</h1>
  <div class="flex justify-between items-center mb-6">
    <Button @click="emitCreate" button-label="Create Task" />
  </div>
</template>

<script setup>
import Button from './Button.vue';

const emit = defineEmits(['create']);

const emitCreate = () => emit('create');
</script>
