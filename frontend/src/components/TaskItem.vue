<template>
  <div
    class="flex justify-between items-center bg-white p-4 rounded shadow-md hover:bg-gray-50"
  >
    <div>
      <h2 class="font-bold">
        {{ task.title }}
      </h2>
      <p class="text-sm text-gray-600">
        {{ task.description }}
      </p>
    </div>

    <button
      @click="deleteTask"
      class="text-red-500 hover:text-red-700"
      title="Delete Task"
    >
      ❌
    </button>
  </div>
</template>

<script>
export default {
  props: {
    task: Object,
  },
  methods: {
    deleteTask() {
      this.$emit('delete', this.task.id);
    }
  }
};
</script>
