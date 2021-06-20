<template>
  <pulse-loader
    v-if="isLoading"
    :loading="isLoading"
    color="#4BABFA"
    size="20px"
    class="spinner"
  ></pulse-loader>
  <div class="mt-4 col-xl-12">
    <h1 class="title">Change your password</h1>
    <p>
      Your password can’t be too similar to your other personal information, it
      must contains at least 8 characters and it can not be entirely numeric.
    </p>
    <hr />
    <password-change-form
      @update-password="changePassword"
    ></password-change-form>
  </div>
</template>

<script>
import PasswordChangeForm from "./PasswordChangeForm";
import { submitForm } from "../../common/form_request_service";
export default {
  name: "PasswordChange",
  components: { PasswordChangeForm },
  data() {
    return {
      isLoading: false,
    };
  },
  methods: {
    async changePassword(formData) {
      for (var pair of formData.entries()) {
        console.log(pair[0] + ", " + pair[1]);
      }
      this.isLoading = true;
      try {
        let endpoint = `/accounts/change-password/`;
        await submitForm(endpoint, "POST", formData);
        await this.$store.dispatch("user/loadUserInfo");
        this.snackbarMessage =
          "Password updated successfully. Please, login for a new session.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
        setTimeout(() => {
          this.$router.replace("/");
          location.reload();
        }, 3000);
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
      }
      this.isLoading = false;
    },
  },
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
