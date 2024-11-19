<template>
  <div class="space-y-4">
    <TaskItem
      v-for="task in tasks"
      :key="task.id"
      :task="task"
    />
  </div>
</template>

<script>
import TaskItem from './TaskItem.vue';

export default {
  components: { TaskItem },
  props: {
    tasks: Array,
  },
};
</script>
