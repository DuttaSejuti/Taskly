<template>
  <h1 class="text-lg font-bold mb-4 text-center">Taskly</h1>
  <div class="flex justify-between items-center mb-6">
    <Button @click="$emit('create')" button-label="Create Task" />
  </div>
</template>

<script>
import Button from './Button.vue';

export default {
  components: {
    Button,
  },
  emits: ['create'],
};
</script>
