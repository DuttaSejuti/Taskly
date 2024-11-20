<template>
  <div class="space-y-4">
    <TaskItem
      v-for="task in tasks"
      :key="task.id"
      :task="task"
      @delete="onDelete"
      @toggle="onToggle"
      @click="onTaskClick(task)"
    />
  </div>
</template>

<script setup>
import TaskItem from './TaskItem.vue';

defineProps({
  tasks: Array
});

const emit = defineEmits(['delete', 'toggle', 'edit']);

const onDelete = (id) => emit('delete', id);
const onToggle = (id) => emit('toggle', id);
const onTaskClick = (task) => emit('edit', task);

</script>
