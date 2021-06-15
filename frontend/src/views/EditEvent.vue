<template>
  <div>
    <h1>Hello edit event page!</h1>
  </div>
</template>

<script>
export default {
  name: "EditEvent",
  props: ["id"],
  async created() {
    if (!this.$store.getters["events/getDetailEvent"]) {
      await this.$store.dispatch("events/loadSelectedEvent", this.id);
    }
    console.log(this.$store.getters["events/getDetailEvent"]);
  },
};
</script>

<style scoped></style>
