<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
    <div class="bg-white p-6 rounded shadow-md max-w-sm w-full">
      <h2 class="text-xl font-bold mb-4">{{ task.id ? 'Edit Task' : 'Create Task' }}</h2>
      <form @submit.prevent="onSave">
        <div class="mb-4">
          <label class="block mb-1 font-semibold">Title</label>
          <input
            v-model="task.title"
            type="text"
            class="w-full p-2 border rounded"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-1 font-semibold">Description</label>
          <textarea
            v-model="task.description"
            class="w-full p-2 border rounded"
            required
          ></textarea>
        </div>
        <div class="flex justify-end space-x-4">
          <button
            type="button"
            @click="$emit('cancel')"
            class="bg-gray-300 px-4 py-2 rounded hover:bg-gray-400"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Save
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    task: Object,
  },
  methods: {
    onSave() {
      this.$emit('save', this.task);
    },
  },
};
</script>
