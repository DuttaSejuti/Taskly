<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <h1 class="text-lg font-bold mb-4 text-center">Taskly</h1>
    <div class="max-w-2xl mx-auto">
      <TaskList
        :tasks="tasks"
      />
    </div>

  </div>
</template>

<script>
import TaskList from '@/components/TaskList.vue';
import apiClient from '@/client/axios.ts';

export default {
  components: {
    TaskList,
  },
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await apiClient.get('/tasks');
        this.tasks = response.data;
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    },
  },
  created() {
    this.fetchTasks();
  },
};
</script>
