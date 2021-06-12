<template>
  <span class="badge mt-5" :class="category">
    {{ category }}
  </span>
</template>

<script>
export default {
  props: ["category"],
};
</script>

<style scoped>
.badge {
  background-color: #ccc;
  color: #252525;
  border-radius: 30px;
  padding: 0.5rem 1.5rem;
  display: inline-block;
  margin-right: 0.5rem;
}
</style>
