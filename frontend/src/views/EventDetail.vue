<template>
  <h1>Event detail</h1>
  <p>{{ env }}</p>
  <GoogleMap
    :api-key="googleApiKey"
    style="width: 100%; height: 500px"
    :center="center"
    :zoom="15"
  >
    <Marker :options="{ position: center }" />
  </GoogleMap>
</template>

<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker } from "vue3-google-map";

export default defineComponent({
  components: { GoogleMap, Marker },
  computed: {
    googleApiKey() {
      return process.env.VUE_APP_GOOGLE_API_KEY;
    },
  },
  setup() {
    const center = { lat: 40.689247, lng: -74.044502 };

    return { center };
  },
});
</script>

<style scoped></style>
