<template>
  <div class="container">
    <div class="col-xl-12 row">
      <h1 class="title">{{ titlePage }}</h1>
    </div>
    <div class="row">
      <div class="col-xl-7 medium-text">
        Organizer - {{ organizer.first_name }} {{ organizer.last_name }}
      </div>
      <div class="col-xl-3 row">
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
        <div class="mt-2">Add a cover for your Ev</div>
        <i
          class="material-icons-outlined ml-1"
          style="font-size: 30px; color: #4babfa"
          >add_a_photo</i
        >
      </div>
      <button class="btn btn-success ml-5" @click="onCoverUpload">
          Upload
        </button>
      <span v-if="currentFile">{{ currentFile.name }}</span>
    </div>
  </div>
</template>

<script>
import { uploadEventCover } from "../common/upload_service";

export default {
  name: "EditEvent",
  props: ["id"],
  data() {
    return {
      titlePage: "",
      selectedFiles: undefined,
      currentFile: undefined,
    };
  },
  computed: {
    organizer() {
      return this.$store.getters["user/getUserInfo"];
    },
  },
  methods: {
    async onCoverUpload() {
      let endpoint = `/api/events/${this.id}/image/`;
      console.log(endpoint, this.currentFile, this.id);
      const response = await uploadEventCover(
        endpoint,
        this.currentFile,
        this.id,
        this.organizer.id
      );
      console.log(response);
    },
    selectFile() {
      this.selectedFiles = this.$refs.file.files;
      this.currentFile = this.selectedFiles.item(0);
      console.log(this.selectedFiles);
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
