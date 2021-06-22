<template>
  <div
    class="card mt-4"
    :class="{
      'text-secondary': isRead,
      'card border-primary text-primary bg-azure': !isRead && eventAvailable,
      'card border-warning text-warning': !isRead && type === 'TBA',
      'card border-danger text-danger': !isRead && type === 'canceled',
    }"
  >
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
  computed: {
    eventAvailable() {
      return (
        this.type === "changed" ||
        this.type === "now available" ||
        this.type === "re-added"
      );
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 15px;
}
.bg-azure {
  background-color: #e8f1ff;
}
</style>
