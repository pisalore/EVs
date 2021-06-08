<template>
  <div>
   {{venue}}
  </div>
</template>

<script>
export default {
  name: "EventCard",
  props: ["name", "organizer", "venue", "start_date", "end_date"],
};
</script>

<style scoped></style>