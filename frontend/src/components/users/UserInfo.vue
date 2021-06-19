<template>
  <div class="col-xl-2">
    <img
      v-if="!user.profile_image"
      src="https://evs-hci.s3.us-west-1.amazonaws.com/media/assets/no-image-profile.jpg"
      alt="Avatar"
    />
    <img
      v-else
      :src="user.profile_image.document"
      alt="Avatar"
    />
  </div>
  <div class="col-xl-7">
    <div class="user-main-info my-4">
      <div class="single-info">
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">info</div
          >
          <div class="col-11">{{ user.first_name }} {{ user.last_name }}</div>
        </div>
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">alternate_email</div
          >
          <div class="col-11">{{ user.email }}</div>
        </div>
        <div class="row p-3">
          <div class="col-1 material-icons-outlined icon">location_city</div
          >
          <div class="col-11">{{ user.city }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserInfo",
  props: ["user"],
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
}
.single-info {
  font-style: normal;
  font-weight: 200;
  font-size: 36px;
  line-height: 42px;
}
.icon {
  color: #1f6dad;
  font-size: 30px;
  margin-top: 5px;
}
</style>
