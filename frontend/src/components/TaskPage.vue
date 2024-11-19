<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <div class="max-w-2xl mx-auto">
      <Header
        @create="openModal"
      />
      <TaskList
        :tasks="tasks"
      />
    </div>

    <TaskModal
      v-if="isModalOpen"
      @save="saveTask"
      @cancel="closeModal"
    />
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import TaskList from '@/components/TaskList.vue';
import TaskModal from '@/components/TaskModal.vue';
import apiClient from '@/client/axios.ts';

export default {
  components: {
    Header,
    TaskList,
    TaskModal,
  },
  data() {
    return {
      tasks: [],
      isModalOpen: false,
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
    openModal() {
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    async saveTask(task) {
      try {
        const response = await apiClient.post('/tasks', {
          ...task,
        });
        this.tasks.push(response.data);
        this.closeModal();
      } catch (error) {
        console.error('Error saving task:', error);
      }
    },
  },
  created() {
    this.fetchTasks();
  },
};
</script>
