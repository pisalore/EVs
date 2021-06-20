<template>
  <div class="mt-4 col-xl-12">
    <h1 class="title">Change your password</h1>
    <p>
      Your password can’t be too similar to your other personal information, it
      must contains at least 8 characters and it can not be entirely numeric.
    </p>
    <hr />
    <password-change-form></password-change-form>
  </div>
</template>

<script>
import PasswordChangeForm from "./PasswordChangeForm";
export default {
  name: "PasswordChange",
  components: { PasswordChangeForm}
};
</script>

<style scoped>
.title {
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  color: #1f6dad;
}
</style>
