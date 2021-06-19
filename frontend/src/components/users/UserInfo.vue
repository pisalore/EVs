<template>
  <div class="col-xl-2">
    <img
      v-if="!user.profile_image"
      src="https://evs-hci.s3.us-west-1.amazonaws.com/media/assets/no-image-profile.jpg"
      alt="Avatar"
    />
    <img v-else :src="user.profile_image.document" alt="Avatar" />
    <p class="text-center mt-2 username">@{{ user.username }}</p>
  </div>
  <div class="col-xl-7">
    <div class="user-main-info">
      <div class="container">
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">info</div>
          <div class="col-11">{{ headerFirstInfo }}</div>
        </div>
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">alternate_email</div>
          <div class="col-11">{{ user.email }}</div>
        </div>
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">location_city</div>
          <div class="col-11">{{ user.city }}</div>
        </div>
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">done_outline</div>
          <div class="col-11">Join EVs on {{ joinedDate }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserInfo",
  props: ["user"],
  computed: {
    headerFirstInfo() {
      return this.user.is_organizer
        ? this.user.organization_name
        : this.user.first_name + " " + this.user.last_name;
    },
    joinedDate() {
      let joinedDate = new Date(this.user.date_joined);
      let month = joinedDate.getUTCMonth() + 1; //months from 1-12
      let day = joinedDate.getUTCDate();
      let year = joinedDate.getUTCFullYear();
      return `${day}/${month}/${year}`;
    },
  },
};
</script>

<style scoped>
img {
  border-radius: 50%;
  max-width: 100%;
}
.user-main-info {
  background: #f0f2f5;
  border-radius: 30px;
  border-color: red;
  height: 100%;
  font-style: normal;
  font-weight: 200;
  font-size: 32px;
  line-height: 42px;
}
.icon {
  color: #1f6dad;
  font-size: 30px;
  margin-top: 5px;
}
.username {
  font-weight: 200;
  font-size: 36px;
  line-height: 42px;
}
</style>
