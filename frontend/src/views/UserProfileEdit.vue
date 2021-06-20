<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-xl-3">
        <div
          class="nav flex-column nav-pills"
          id="v-pills-tab"
          role="tablist"
          aria-orientation="vertical"
        >
          <a
            class="nav-link active"
            id="v-pills-home-tab"
            data-toggle="pill"
            href="#v-pills-home"
            role="tab"
            aria-controls="v-pills-home"
            aria-selected="true"
            >Profile Overview</a
          >
          <a
            class="nav-link"
            id="v-pills-profile-tab"
            data-toggle="pill"
            href="#v-pills-profile"
            role="tab"
            aria-controls="v-pills-profile"
            aria-selected="false"
            >Change Password</a
          >
        </div>
      </div>

      <div class="tab-content col-xl-9" id="v-pills-tabContent">
        <div
          class="tab-pane fade show active"
          id="v-pills-home"
          role="tabpanel"
          aria-labelledby="v-pills-home-tab"
        >
          <profile-overview-edit></profile-overview-edit>
        </div>
        <div
          class="tab-pane fade"
          id="v-pills-profile"
          role="tabpanel"
          aria-labelledby="v-pills-profile-tab"
        >
          <password-change></password-change>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileOverviewEdit from "../components/users/ProfileOverviewEdit";
import PasswordChange from "../components/users/PasswordChange";
export default {
  name: "UserProfileEdit",
  components: {
    ProfileOverviewEdit,
    PasswordChange,
  },
  data() {
    return {
      userInfo: null,
    };
  },
  created() {
    this.userInfo = this.$store.getters["user/getUserInfo"];
  },
};
</script>

<style scoped></style>
