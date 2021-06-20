<template>
  <snackbar
    v-if="showSnackbar"
    :is_error="isError"
    :color="snackBarColor"
    :message="snackbarMessage"
    @close="snackbarFalse"
  ></snackbar>
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
    <div v-if="isError" style="color: red" class="col-xl-6 mt-5">
      {{ passwordErrors }}
    </div>
  </div>
</template>

<script>
import PasswordChangeForm from "./PasswordChangeForm";
import { submitForm } from "../../common/form_request_service";
import Snackbar from "../../ui/Snackbar";
export default {
  name: "PasswordChange",
  components: { PasswordChangeForm, Snackbar },
  data() {
    return {
      isLoading: false,
      isError: false,
      snackbarMessage: "",
      snackBarColor: "",
      showSnackbar: false,
      passwordErrors: "",
    };
  },
  methods: {
    async changePassword(formData) {
      this.isError = false;
      this.isLoading = true;
      try {
        let endpoint = `/accounts/change-password/`;
        await submitForm(endpoint, "POST", formData);
        await this.$store.dispatch("user/loadUserInfo");
        this.snackbarMessage =
          "Password updated successfully. You will be redirect for login again.";
        this.snackBarColor = "#3DB834";
        await this.$router.replace("/");
        await location.reload();
      } catch (error) {
        this.isError = true;
        this.passwordErrors = error;
      }
      this.isLoading = false;
    },
    snackbarFalse() {
      this.showSnackbar = false;
      this.isError = false;
      this.snackbarMessage = "";
      this.snackBarColor = "";
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
