<template>
  <div class="space-y-4">
    <TaskItem
      v-for="task in tasks"
      :key="task.id"
      :task="task"
      @delete="onDelete"
      @toggle="onToggle"
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
  methods: {
    onDelete(id) {
      this.$emit('delete', id);
    },
    onToggle(id) {
      this.$emit('toggle', id);
    },
  }
};
</script>
