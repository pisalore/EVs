<template>
  <div class="card col-xl-3 mx-3" style="width: 18rem" @click="eventDetail">
    <div class="card-body">
      <h3 class="card-title">{{ name }}</h3>
      <h4 class="card-organizer">{{ organizer }}</h4>
      <h5 class="card-venue">{{ venue }}</h5>
      <h5 class="card-date">{{ start_date }} - {{ end_date }}</h5>
      <img
        v-if="image"
        class="card-img"
        :src="image.document"
        alt="event-image"
      />
      <div v-if="website" class="text-center pt-3">
        <a class="btn btn-primary" :href="website" role="button">Link</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EventCard",
  props: [
    "id",
    "name",
    "organizer",
    "venue",
    "start_date",
    "end_date",
    "image",
    "website",
  ],
  methods: {
    eventDetail() {
      this.$router.push({
        path: `/events/${this.id}`,
      });
    },
  },
};
</script>

<style scoped>
.card {
  cursor: pointer;
  border-radius: 30px;
  border: 0.5px solid #1f6dad;
  max-width: 400px;
}

.card-title {
  font-style: normal;
  font-weight: normal;
  font-size: 28px;
  line-height: 28px;
  color: #1f6dad;
}

.card-organizer {
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  color: #000000;
}

.card-venue {
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 16px;
  color: #575757;
}

.card-date {
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 16px;
  color: #575757;
}

.card-img {
  border-radius: 20px;
  border: none;
  width: 100%;
  height: 7vw;
  object-fit: cover;
}
</style>
