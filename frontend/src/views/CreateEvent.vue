<template>
  <pulse-loader
    v-if="isLoading"
    :loading="isLoading"
    color="#4BABFA"
    size="20px"
    class="spinner"
  ></pulse-loader>
  <div v-else class="container">
    <div class="col-xl-12 row">
      <h1 class="title">Create new Event</h1>
    </div>
    <div class="row">
      <div class="col-xl-7 medium-text my-1">
        Organizer - {{ organizer.first_name }} {{ organizer.last_name }}
      </div>
    </div>
    <div class="container-fluid mt-5">
      <div class="row d-flex">
        <div class="col-xl-12">
          <event-form
            :organizer="organizer"
            :is-create="true"
            @create-event="createEvent"
          ></event-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EventForm from "../components/events/EventForm";
import { apiService } from "../common/api.service";
export default {
  name: "CreateEvent",
  components: { EventForm },
  data() {
    return {
      isLoading: false,
    };
  },
  computed: {
    organizer() {
      return this.$store.getters["user/getUserInfo"];
    },
  },
  methods: {
    async loadOrganizer() {
      await this.$store.dispatch("user/loadUserInfo");
    },
    async createEvent(formData) {
      this.isLoading = true;
      try {
        let endpoint = "/api/events/organizer/managed-events/";
        await apiService(endpoint, "POST", formData);
        this.snackbarMessage = "Event created successfully.";
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
  },
  created() {
    this.loadOrganizer();
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
