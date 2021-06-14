<template>
  <div v-if="selectedEvent" class="container">
    <h1>{{ selectedEvent.name }}</h1>
    <GoogleMap
      :api-key="googleApiKey"
      style="width: 100%; height: 500px"
      :center="coordinates"
      :zoom="15"
    >
      <Marker :options="{ position: coordinates }" />
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";
export default defineComponent({
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
  },
  methods: {
    async loadSelectedEvent() {
      const googleGeocodingAPI =
        "https://maps.googleapis.com/maps/api/geocode/json?address=";
      await this.$store.dispatch("events/loadSelectedEvent", this.id);
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
  // setup() {
  //   const center = { lat: 40.689247, lng: -74.044502 };
  //   return { center };
  // },
});
</script>

<style scoped></style>
