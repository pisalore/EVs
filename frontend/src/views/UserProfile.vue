<template>
  <div class="container-fluid mt-4">
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