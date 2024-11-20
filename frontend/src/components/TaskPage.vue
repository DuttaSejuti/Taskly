<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <div class="max-w-2xl mx-auto">
      <Header @create="openModal" />
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search tasks..."
        class="w-full p-2 mb-4 border rounded"
      />
      <TaskList
        :tasks="filteredTasks"
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

<script setup>
import { ref, computed } from 'vue';
import Header from '@/components/Header.vue';
import TaskList from '@/components/TaskList.vue';
import TaskModal from '@/components/TaskModal.vue';
import apiClient from '@/client/axios.ts';

const tasks = ref([]);
const isModalOpen = ref(false);
const modalTask = ref({ id: null, title: '', description: '' });
const searchQuery = ref('');

const filteredTasks = computed(() => {
  const query = searchQuery.value.toLowerCase();
  return tasks.value.filter(
    (task) =>
      task.title.toLowerCase().includes(query) ||
      task.description.toLowerCase().includes(query)
  );
});

const fetchTasks = async () => {
  try {
    const response = await apiClient.get('/tasks');
    tasks.value = response.data;
  } catch (error) {
    console.error('Error fetching tasks:', error);
  }
};

const openModal = (task) => {
  isModalOpen.value = true;
  modalTask.value = task ? { ...task } : { id: null, title: '', description: '' };
};

const closeModal = () => {
  isModalOpen.value = false;
};

const saveTask = async (task) => {
  if (task.id) {
    updateTask(task);
    return;
  }
  try {
    const response = await apiClient.post('/tasks', { ...task });
    tasks.value.push(response.data);
    closeModal();
  } catch (error) {
    console.error('Error saving task:', error);
  }
};

const updateTask = async (task) => {
  try {
    const response = await apiClient.put(`/tasks/${task.id}`, { ...task });
    tasks.value = tasks.value.map((t) => (t.id === task.id ? response.data : t));
    closeModal();
  } catch (error) {
    console.error('Error updating task:', error);
  }
};

const deleteTask = async (id) => {
  try {
    await apiClient.delete(`/tasks/${id}`);
    tasks.value = tasks.value.filter((task) => task.id !== id);
  } catch (error) {
    console.error('Error deleting task:', error);
  }
};

const toggleCheckbox = async (id) => {
  const task = tasks.value.find((task) => task.id === id);
  if (task) {
    try {
      await apiClient.put(`/tasks/${id}`, { is_completed: !task.is_completed });
      task.is_completed = !task.is_completed;
    } catch (error) {
      console.error('Error updating task:', error);
    }
  }
};

fetchTasks();
</script>
