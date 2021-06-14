<template>
  <div class="container">
    <h1>{{ selectedEvent.name }}</h1>
    <GoogleMap
      :api-key="googleApiKey"
      style="width: 100%; height: 500px"
      :center="center"
      :zoom="15"
    >
      <Marker :options="{ position: center }" />
    </GoogleMap>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

export default defineComponent({
  components: { GoogleMap, Marker },
  props: ["id"],
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
      await this.$store.dispatch("events/loadSelectedEvent", this.id);
    },
  },
  created() {
    this.loadSelectedEvent();
  },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };

    return { center };
  },
});
</script>

<style scoped></style>
