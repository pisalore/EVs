<template>
  <div class="mt-3">
    <router-view />
  </div>
</template>

<script>
export default {
  methods: {
    async loadUserInfo() {
      try {
        await this.$store.dispatch("user/loadUserInfo", null);
      } catch (error) {
        this.error = error.message || "Something went wrong!";
      }
    },
  },
  created() {
    //this.loadUserInfo();
  },
};
</script>
