<template>
  <div class="mt-5 text-center">
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    async loadUserInfo() {
      try {
        await this.$store.dispatch("user/loadUserInfo");
      } catch (error) {
        this.error = error.message || "Something went wrong!";
      }
    },
  },
  created() {
    this.loadUserInfo();
  },
};
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>