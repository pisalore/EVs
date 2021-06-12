<template>
  <div class="chip">
    <div class="row justify-content-around">
      <div>
        {{ category }}
      </div>
      <div class="material-icons" style="margin-top: 11px" @click="close">
        close
      </div>
    </div>

  </div>
</template>

<script>
export default {
  emits: ["close-chip"],
  props: ["category"],
  methods: {
    close() {
      this.$emit("close-chip", this.category);
    },
  },
};
</script>

<style scoped>
.chip {
  display: inline-block;
  padding: 0 25px;
  font-size: 16px;
  line-height: 50px;
  border-radius: 25px;
  background-color: #f1f1f1;
  text-align: center;
  width: 200px;;
}
</style>
