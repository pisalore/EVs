<template>
  <div class="mt-5">
    <form @submit.prevent="changePassword">
      <div class="form-group">
        <label for="current">Old password</label>
        <input
          v-model="oldPassword"
          type="password"
          class="form-control"
          id="current"
          placeholder="Type your current password"
          required
        />
      </div>
      <div class="form-group">
        <label for="new1">New password</label>
        <input
          v-model="newPassword"
          type="password"
          class="form-control"
          id="new1"
          placeholder="Type your new password"
          required
        />
      </div>
      <div class="form-group">
        <label for="new2">Retype new password</label>
        <input
          v-model="retypedPassword"
          type="password"
          class="form-control"
          id="new2"
          placeholder="Type again your new password"
          required
        />
      </div>
      <div class="d-flex justify-content-center mt-4">
        <button type="submit" class="btn btn-lg btn-primary">
          Update Password
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "PasswordChangeForm",
  emits: ["update-password"],
  data() {
    return {
      oldPassword: null,
      newPassword: null,
      retypedPassword: null,
    };
  },
  methods: {
    changePassword() {
      let formData = new FormData();
      formData.append("old_password", this.oldPassword);
      formData.append("password", this.newPassword);
      formData.append("password_confirm", this.retypedPassword);
      this.$emit("update-password", formData);
    },
  },
};
</script>

<style scoped></style>
