<template>
  <div class="container-fluid mt-4">
    <h1 class="title px-4">Your Profile</h1>
    <div class="row mt-4">
      <user-info v-if="userInfo" :user="userInfo"> </user-info>
      <div class="col-xl-3 text-center my-2">
        <button class="btn btn-primary">Edit Profile</button>
      </div>
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
.container-fluid {
  width: 90%;
}
</style>
