<template>
    <div class="col-xl-2">hi {{ isOrganizer }}</div>
    <div class="col-xl-8">hi {{ isOrganizer }}</div>
</template>

<script>
export default {
  name: "UserInfo",
  props: ["isOrganizer"],
};
</script>

<style scoped></style>
