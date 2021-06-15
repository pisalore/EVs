<template>
  <snackbar
    v-if="showSnackbar"
    :is_error="isError"
    :color="snackBarColor"
    :message="snackbarMessage"
    @close="snackbarFalse"
  ></snackbar>
  <div class="container">
    <div class="col-xl-12 row">
      <h1 class="title">{{ titlePage }}</h1>
    </div>
    <div class="row">
      <div class="col-xl-7 medium-text">
        Organizer - {{ organizer.first_name }} {{ organizer.last_name }}
      </div>
      <div class="ml-3 col-xl-3">
        <div class="row">
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
          <div class="mt-2">
            {{ currentFile ? currentFile.name : "Add a cover for your Ev" }}
          </div>
          <i
            class="material-icons-outlined ml-1"
            style="font-size: 30px; color: #4babfa"
            >add_a_photo</i
          >
        </div>
      </div>

      <button class="btn btn-success ml-3" @click="onCoverUpload">
        Upload
      </button>
    </div>
  </div>
</template>

<script>
import { uploadEventCover } from "../common/upload_service";
import Snackbar from "../ui/Snackbar";

export default {
  name: "EditEvent",
  components: { Snackbar },
  props: ["id"],
  data() {
    return {
      titlePage: "",
      selectedFiles: undefined,
      currentFile: undefined,
      isError: false,
      snackbarMessage: "",
      userEmailForm: "",
      snackBarColor: "",
      showSnackbar: false,
    };
  },
  computed: {
    organizer() {
      return this.$store.getters["user/getUserInfo"];
    },
  },
  methods: {
    async onCoverUpload() {
      try {
        let endpoint = `/api/events/${this.id}/image/`;
        const response = await uploadEventCover(
          endpoint,
          this.currentFile,
          this.id,
          this.organizer.id
        );
        this.snackbarMessage = "Image uploaded successfully.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
        this.currentFile = undefined;
        console.log(response);
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
      }
    },
    selectFile() {
      this.selectedFiles = this.$refs.file.files;
      this.currentFile = this.selectedFiles.item(0);
      console.log(this.selectedFiles);
    },
    snackbarFalse() {
      this.showSnackbar = false;
      this.isError = false;
      this.snackbarMessage = "";
      this.snackBarColor = "";
    },
  },
  async created() {
    await this.$store.dispatch("user/loadUserInfo");
    const event = this.$store.getters["events/getDetailEvent"];
    if (event) {
      this.titlePage = `Edit ${event.name}`;
    } else if (this.id) {
      await this.$store.dispatch("events/loadSelectedEvent", this.id);
      this.titlePage = `Edit ${this.$store.getters["events/getDetailEvent"].name}`;
    } else {
      this.titlePage = "Create new Event";
    }
    console.log(event);
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
</style>
