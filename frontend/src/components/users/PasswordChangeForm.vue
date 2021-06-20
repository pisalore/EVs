<template>
  <div class="container mt-5">
    <form @submit.prevent="updatePassword">
      <div class="form-group">
        <label for="current">Old password</label>
        <input
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
};
</script>

<style scoped></style>
