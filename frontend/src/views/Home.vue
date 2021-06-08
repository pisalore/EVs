<template>
  <div class="home"></div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
  name: "Home",

  data() {
    return {
      questions: [],
    };
  },

  methods: {
    getEvents() {
      let endpoint = "api/events/";
      apiService(endpoint).then((data) => {
        console.log(data.results);
      });
    },
  },

  created() {
    this.getEvents();
  },
};
</script>
