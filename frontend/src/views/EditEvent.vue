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
  <div v-else class="container">
    <div v-if="event" class="col-xl-12 row">
      <h1 class="title">Edit - {{ event.name }}</h1>
    </div>
    <div class="my-3">
      <img
        v-if="event && event.event_image"
        :src="event.event_image.document"
        alt=""
        style="width: 100%; border-radius: 20px"
        :class="{
          'mobile-img-height': isMobile,
          'desktop-img-height': !isMobile,
        }"
      />
    </div>
    <div class="row">
      <div class="col-xl-7 medium-text my-1">
        Organizer - {{ organizer.first_name }} {{ organizer.last_name }}
      </div>
      <div class="ml-3 col-xl-3">
        <div class="row mt-1">
          <input
            type="file"
            style="
              cursor: pointer;
              opacity: 0;
              position: absolute;
              top: 0;
              left: 0;
              bottom: 0;
              right: 0;
              width: 100%;
              height: 100%;
            "
            ref="file"
            @change="selectFile"
          />
          <div class="mt-1">
            {{ currentFile ? currentFile.name : "Change cover to your Ev" }}
          </div>
          <i
            class="material-icons-outlined ml-1"
            style="font-size: 30px; color: #4babfa"
            >add_a_photo</i
          >
        </div>
      </div>
      <button
        v-if="event && event.event_image"
        class="btn btn-danger ml-3"
        @click="deleteCover"
      >
        Remove cover
      </button>
    </div>
    <div class="container-fluid mt-5">
      <div class="row d-flex">
        <div class="col-xl-12">
          <event-form
            v-if="event"
            :event="event"
            :organizer="organizer"
            @update-event="updateEvent"
            @delete-event="deleteEvent"
          ></event-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { uploadEventCover } from "../common/upload_service";
import { apiService } from "../common/api.service";
import Snackbar from "../ui/Snackbar";
import EventForm from "../components/events/EventForm";

export default {
  name: "EditEvent",
  components: { EventForm, Snackbar },
  props: ["id"],
  data() {
    return {
      selectedFiles: undefined,
      currentFile: undefined,
      isError: false,
      snackbarMessage: "",
      snackBarColor: "",
      showSnackbar: false,
      isLoading: false,
    };
  },
  computed: {
    organizer() {
      return this.$store.getters["user/getUserInfo"];
    },
    event() {
      return this.$store.getters["events/getManagedEvent"];
    },
    isMobile() {
      return (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        ) || window.screen.width < 760
      );
    },
  },
  methods: {
    async onCoverUpload() {
      this.isLoading = true;
      try {
        let endpoint = `/api/events/${this.id}/image/`;
        await uploadEventCover(
          endpoint,
          this.currentFile,
          this.id,
          this.organizer.id
        );
        await this.$store.dispatch("events/loadSelectedEvent", this.id);
        this.snackbarMessage = "Image uploaded successfully.";
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
    async deleteCover() {
      this.isLoading = true;
      try {
        let endpoint = `/api/events/${this.id}/image/`;
        await uploadEventCover(
          endpoint,
          new File([], ""),
          this.id,
          this.organizer.id
        );
        await this.$store.dispatch("events/loadSelectedEvent", this.id);
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
    async updateEvent(formData) {
      this.isLoading = true;
      try {
        let endpoint = `/api/events/organizer/managed-events/${this.id}/`;
        await apiService(endpoint, "PATCH", formData);
        await this.$store.dispatch("events/loadEventToBeModified", this.id);
        this.snackbarMessage = "Event uploaded successfully.";
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
    async deleteEvent() {
      this.isLoading = true;
      try {
        console.log("delete");
        let endpoint = `/api/events/organizer/managed-events/${this.id}/`;
        const response = await apiService(endpoint, "DELETE");
        this.snackbarMessage = "Event deleted successfully.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
        console.log(response);
        await this.$router.replace("/");
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
      }
      this.isLoading = false;
    },
    selectFile() {
      this.selectedFiles = this.$refs.file.files;
      this.currentFile = this.selectedFiles.item(0);
      this.onCoverUpload();
    },
    snackbarFalse() {
      this.showSnackbar = false;
      this.isError = false;
      this.snackbarMessage = "";
      this.snackBarColor = "";
    },
    async loadEvent() {
      this.isLoading = true;
      await this.$store.dispatch("events/loadEventToBeModified", this.id);
    },
    async loadUserInfo() {
      await this.$store.dispatch("user/loadUserInfo");
      this.isLoading = false;
    },
  },
  async created() {
    await this.loadEvent();
    await this.loadUserInfo();
  },
};
</script>

<style scoped>
.title {
  font-style: normal;
  font-weight: normal;
  font-size: 36px;
  line-height: 56px;
  color: #1f6dad;
}

.medium-text {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
}
.mobile-img-height {
  height: 40vw;
}

.desktop-img-height {
  height: 16vw;
}
</style>
