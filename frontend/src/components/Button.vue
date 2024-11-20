<template>
  <button
    @click="$emit('click')"
    class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
  >
    {{ buttonLabel}}
  </button>
</template>

<script>
export default {
  props: {
    buttonLabel: {
      type: String
    },
  },
};
</script>
