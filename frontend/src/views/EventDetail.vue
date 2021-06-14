<template>
  <div v-if="selectedEvent" class="container-fluid">
    <div class="col-xl-12">
      <div class="row">
        <div class="col-xl-6 p-0 m-0">
          <h1>{{ selectedEvent.name }}</h1>
          <h2>{{ selectedEvent.venue }}</h2>
        </div>
        <div
          v-if="selectedEvent.event_image"
          class="col-xl-6 p-0 m-0"
          style="width: 100%; display: block"
        >
          <img
            :src="selectedEvent.event_image.document"
            alt=""
            :class="{
              'mobile-img-height': isMobile,
              'desktop-img-height': !isMobile,
            }"
          />
        </div>
      </div>
      <div class="row">
        <div class="col-xl-6 p-0 m-0">
          <h1>Other info here...</h1>
        </div>
        <div class="col-xl-6 p-0 m-0">
          <GoogleMap
            :api-key="googleApiKey"
            style="width: 100%; height: 500px"
            :center="coordinates"
            :zoom="15"
          >
            <Marker :options="{ position: coordinates }" />
          </GoogleMap>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { GoogleMap, Marker } from "vue3-google-map";

export default {
  components: { GoogleMap, Marker },
  props: ["id"],
  data() {
    return {
      coordinates: null,
      eventVenue: null,
    };
  },
  computed: {
    googleApiKey() {
      return process.env.VUE_APP_GOOGLE_API_KEY;
    },
    selectedEvent() {
      return this.$store.getters["events/getDetailEvent"];
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
    async loadSelectedEvent() {
      const googleGeocodingAPI =
        "https://maps.googleapis.com/maps/api/geocode/json?address=";
      await this.$store.dispatch("events/loadSelectedEvent", this.id);
      console.log(this.selectedEvent);
      this.eventVenue = this.selectedEvent.venue;
      const endpoint = `${googleGeocodingAPI + this.eventVenue}&key=${
        this.googleApiKey
      }`;
      const response = await fetch(endpoint);
      const data = await response.json();
      this.coordinates = data.results[0].geometry.location;
    },
  },
  created() {
    this.loadSelectedEvent();
  },
};
</script>

<style scoped>
img {
  width: 100%;
}

.mobile-img-height {
  height: 40vw;
}

.desktop-img-height {
  height: 15vw;
}
</style>
