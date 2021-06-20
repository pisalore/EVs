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
  <div class="col-xl-12">
    <h1 class="title">Edit your account info</h1>
    Your city will make us able to suggest events near you.
    <hr />
    <user-edit-form
      v-if="user.id"
      :user="user"
      @update-user="updateUser"
    ></user-edit-form>
  </div>
  <div class="col-xl-12">
    <hr />
    <h1 class="title">Delete your account</h1>
    <p>This action is not reversible. You will lost all your saved EVs.</p>
    <div class="d-flex justify-content-center">
      <button
        type="button"
        class="btn btn-lg btn-danger"
        @click="showDeleteModal"
      >
        Delete Account
      </button>
    </div>
  </div>
  <base-modal
    v-if="showModal"
    @cancel-modal="showModal = false"
    @confirm-modal="deleteUser"
    :title="modalTitle"
    :message="modalMessage"
    :confirm="modalConfirm"
    :cancel="modalCancel"
    :action="modalAction"
  ></base-modal>
</template>

<script>
import UserEditForm from "./UserEditForm";
import Snackbar from "../../ui/Snackbar";
import BaseModal from "../../ui/BaseModal";
import { submitForm } from "../../common/form_request_service";
import { apiService } from "../../common/api.service";
export default {
  name: "ProfileOverviewEdit",
  components: { UserEditForm, Snackbar, BaseModal },
  props: ["user"],
  data() {
    return {
      isError: false,
      snackbarMessage: "",
      snackBarColor: "",
      showSnackbar: false,
      isLoading: false,
      showModal: false,
      modalTitle: "",
      modalMessage: "",
      modalAction: "",
      modalConfirm: "",
      modalCancel: "",
    };
  },
  methods: {
    async updateUser(formData) {
      this.isLoading = true;
      try {
        let endpoint = `/api/user/${this.user.username}/`;
        await submitForm(endpoint, "PUT", formData);
        await this.$store.dispatch("user/loadUserInfo");
        this.snackbarMessage = "User updated successfully.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
      }
      this.isLoading = false;
    },
    showDeleteModal() {
      this.showModal = true;
      this.modalAction = "delete";
      this.modalTitle = "User Delete";
      this.modalMessage =
        "Do you really want to delete your Ev account? This operation is not reversible.";
      this.modalConfirm = "Confirm";
      this.modalCancel = "Cancel";
    },
    async deleteUser() {
      this.showModal = false;
      this.isLoading = true;
      try {
        let endpoint = `/api/user/${this.user.username}/`;
        await apiService(endpoint, "DELETE");
        await this.$router.replace("/");
        await location.reload();
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
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
p {
  font-weight: bold;
}
</style>
