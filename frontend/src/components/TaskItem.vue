<template>
  <div
    class="flex items-center bg-white p-4 rounded shadow-md hover:bg-gray-50"
  >
    <div>
      <h2 class="font-bold">
        {{ task.title }}
      </h2>
      <p class="text-sm text-gray-600">
        {{ task.description }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    task: Object,
  }
};
</script>
