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
  <div v-else class="container-fluid p-5">
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
          <div class="row mt-1 d-flex justify-content-center">
            <label id="getFileLabel" for="getFile" style="cursor: pointer">{{
              currentFile ? currentFile.name : "Change your profile image"
            }}</label>
            <input
              class="input-profile-image"
              type="file"
              id="getFile"
              ref="file"
              @change="selectFile"
            />
            <i
              class="material-icons-outlined ml-1"
              style="font-size: 30px; color: #4babfa"
              >add_a_photo</i
            >
          </div>
          <div v-if="userInfo.profile_image" class="text-center">
            <button class="btn btn-danger" @click="showDeleteImageProfileModal">
              Delete your profile image
            </button>
          </div>
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
          <profile-overview-edit
            v-if="userInfo.id"
            :user="userInfo"
          ></profile-overview-edit>
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
  <base-modal
    v-if="showModal"
    @cancel-modal="showModal = false"
    @confirm-modal="deleteProfileImage"
    :title="modalTitle"
    :message="modalMessage"
    :confirm="modalConfirm"
    :cancel="modalCancel"
    :action="modalAction"
  ></base-modal>
</template>

<script>
import ProfileOverviewEdit from "../components/users/ProfileOverviewEdit";
import PasswordChange from "../components/users/PasswordChange";
import Snackbar from "../ui/Snackbar";
import BaseModal from "../ui/BaseModal";
import { uploadProfileImage } from "../common/upload_service";

export default {
  name: "UserProfileEdit",
  components: {
    ProfileOverviewEdit,
    PasswordChange,
    Snackbar,
    BaseModal
  },
  data() {
    return {
      selectedFiles: null,
      currentFile: null,
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
  computed: {
    userInfo() {
      console.log(this.$store.getters["user/getUserInfo"]);
      return this.$store.getters["user/getUserInfo"];
    },
  },
  methods: {
    selectFile() {
      this.selectedFiles = this.$refs.file.files;
      this.currentFile = this.selectedFiles.item(0);
      this.onProfileImageUpload();
    },
    async onProfileImageUpload() {
      this.isLoading = true;
      try {
        let endpoint = `/api/profile-image/`;
        await uploadProfileImage(endpoint, this.currentFile, this.userInfo.id);
        await this.loadUserInfo();
        this.snackbarMessage = "Image uploaded successfully.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
        this.currentFile = null;
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
      }
      this.isLoading = false;
    },
    showDeleteImageProfileModal() {
      this.showModal = true;
      this.modalAction = "delete";
      this.modalTitle = "User Delete";
      this.modalMessage =
        "Do you really want to delete your profile image? It will be lost.";
      this.modalConfirm = "Confirm";
      this.modalCancel = "Cancel";
    },
    async deleteProfileImage() {
      this.showModal = false;
      this.isLoading = true;
      try {
        let endpoint = `/api/profile-image/`;
        await uploadProfileImage(endpoint, new File([], ""), this.userInfo.id);
        await this.loadUserInfo();
        this.snackbarMessage = "Image removed successfully.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
        this.currentFile = undefined;
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
    async loadUserInfo() {
      await this.$store.dispatch("user/loadUserInfo");
    },
  },
  created() {
    this.loadUserInfo();
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
  height: auto;
  max-width: 50%;
  min-height: 200px;
  min-width: 200px;
}
.username {
  font-style: normal;
  font-weight: 200;
  font-size: 36px;
  line-height: 42px;
}
.input-profile-image {
  display: none;
}
</style>
