<template>
  <div class="container-fluid mt-4">
    <h1 class="title px-4">Your Profile</h1>
      <user-info v-if="userInfo" :user="userInfo"> </user-info>
  </div>
</template>

<script>
import UserInfo from "../components/users/UserInfo";
export default {
  name: "UserProfile",
  components: { UserInfo },
  computed: {
    userInfo() {
      return this.$store.getters["user/getUserInfo"];
    },
  },
  methods: {
    async loadUserInfo() {
      await this.$store.dispatch("user/loadUserInfo");
    },
  },
  created() {
    this.loadUserInfo();
  },
};
</script>

<style scoped>
.title {
  font-style: normal;
  font-weight: 300;
  font-size: 48px;
  line-height: 56px;
  color: #1f6dad;
}
</style>
