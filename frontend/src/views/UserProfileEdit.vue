<template>
  <div class="container-fluid p-5">
    <div class="row">
      <div class="col-xl-3">
        <div class="py-5">
          <img
            v-if="!userInfo.profile_image"
            src="https://evs-hci.s3.us-west-1.amazonaws.com/media/assets/no-image-profile.jpg"
            alt="Avatar"
            class="mx-auto d-block"
          />
          <img
            v-else
            class="mx-auto d-block"
            :src="userInfo.profile_image.document"
            alt="Avatar"
          />
          <p class="text-center mt-2 username">@{{ userInfo.username }}</p>
        </div>
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
            ><span class="material-icons-outlined icon"> person </span>Profile
            Overview</a
          >
          <a
            class="nav-link"
            id="v-pills-profile-tab"
            data-toggle="pill"
            href="#v-pills-profile"
            role="tab"
            aria-controls="v-pills-profile"
            aria-selected="false"
          >
            <span class="material-icons-outlined icon"> lock </span>Change
            Password</a
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
  computed: {
    userInfo() {
      console.log(this.$store.getters["user/getUserInfo"]);
      return this.$store.getters["user/getUserInfo"];
    },
  },
};
</script>

<style scoped>
.icon {
  padding: 20px;
  font-size: 30px;
}
img {
  border-radius: 50%;
  max-width: 50%;
}
.username {
  font-style: normal;
  font-weight: 200;
  font-size: 36px;
  line-height: 42px;
}
</style>
