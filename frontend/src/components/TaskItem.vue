<template>
  <div
    class="flex justify-between items-center bg-white p-4 rounded shadow-md hover:bg-gray-50"
    @click="emitClick"
  >
    <div class="flex items-center">
      <input
        type="checkbox"
        class="mr-3 w-5 h-5"
        :checked="task.is_completed"
        @click.stop
        @change="toggleCheckbox"
      />
      <div>
        <h2 class="font-bold" :class="{ 'line-through text-gray-500': task.is_completed }">
          {{ task.title }}
        </h2>
        <p class="text-sm text-gray-600" :class="{ 'line-through text-gray-500': task.is_completed }">
          {{ task.description }}
        </p>
      </div>
    </div>

    <button
      @click.stop="deleteTask"
      class="text-red-500 hover:text-red-700"
      title="Delete Task"
    >
      ❌
    </button>
  </div>
</template>

<script setup>
const props = defineProps({
  task: Object,
});

const emit = defineEmits(['click', 'delete', 'toggle']);

const emitClick = () => emit('click');
const deleteTask = () => emit('delete', props.task.id);
const toggleCheckbox = () => emit('toggle', props.task.id);

</script>
