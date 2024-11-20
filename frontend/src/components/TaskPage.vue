<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <div class="max-w-2xl mx-auto">
      <Header
        @create="openModal"
      />
      <TaskList
        :tasks="tasks"
        @delete="deleteTask"
        @toggle="toggleCheckbox"
        @edit="openModal"
      />
    </div>

    <TaskModal
      v-if="isModalOpen"
      :task="modalTask"
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
      modalTask: { id: null, title: '', description: '' },
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
    openModal(task) {
      this.isModalOpen = true;
      if (task) {
        this.modalTask = { ...task };
      } else {
        this.modalTask = { id: null, title: '', description: '' };
      }
    },
    closeModal() {
      this.isModalOpen = false;
    },
    async saveTask(task) {
      if (task.id) {
        this.updateTask(task);
        return
      }
      try {
        const response = await apiClient.post('/tasks', { ...task });
        this.tasks.push(response.data);
        this.closeModal();
      } catch (error) {
        console.error('Error saving task:', error);
      }
    },
    async updateTask(task) {
      try {
        const response = await apiClient.put(`/tasks/${task.id}`, { ...task });
        this.tasks = this.tasks.map((t) => t.id === task.id ? response.data : t);
        this.closeModal();
      } catch (error) {
        console.error('Error updating task:', error);
      }
    },
    async deleteTask(id) {
      try {
        await apiClient.delete(`/tasks/${id}`);
        this.tasks = this.tasks.filter((task) => task.id !== id);
      } catch (error) {
        console.error('Error deleting task:', error);
      }
    },
    async toggleCheckbox(id) {
      const task = this.tasks.find((task) => task.id === id);
      if (task) {
        try {
          await apiClient.put(`/tasks/${id}`, { is_completed: !task.is_completed });
          task.is_completed = !task.is_completed;
        } catch (error) {
          console.error('Error updating task:', error);
        }
      }
    },
  },
  created() {
    this.fetchTasks();
  },
};
</script>
