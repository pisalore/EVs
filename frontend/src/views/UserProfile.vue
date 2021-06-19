<template>
  <div class="container-fluid mt-4">
    <h1 class="title px-4">Your Profile</h1>
    <div class="row p-5">
      <user-info v-if="userInfo" :is-organizer="userInfo.is_organizer">
      </user-info>
      <div class="col-xl-2">edit</div>
    </div>
  </div>
</template>

<script>
import UserInfo from "../components/users/UserInfo";
export default {
  name: "UserProfile",
  components: { UserInfo },
  computed: {
    userInfo() {
      console.log(this.$store.getters["user/getUserInfo"]);
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
