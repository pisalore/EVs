<template>
  <router-view />
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
