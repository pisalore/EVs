<template>
  <div class="card mt-2" :class="{ 'bg-light': isRead, 'bg-primary text-white': !isRead }">
    <div class="card-body">
      <h5 class="card-text">{{ message }}</h5>
      <p class="card-text">
        {{ new Date(createdAt).toDateString() }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Notification",
  props: ["createdAt", "message", "type", "isRead", "eventId"],
};
</script>

<style scoped></style>
