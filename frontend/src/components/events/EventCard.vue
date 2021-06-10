<template>
  <div
    class="card col-xl-3 mx-3 my-2"
    style="width: 18rem"
    @click="eventDetail"
  >
    <div class="card-body">
      <h3 class="card-title">{{ name }}</h3>
      <h4 class="card-organizer">{{ organizer }}</h4>
      <h5 class="card-venue">@{{ venue }}</h5>
      <h5 class="card-date">{{ computeDate() }}</h5>
      <img
        v-if="image"
        class="card-img"
        :src="image.document"
        alt="event-image"
      />
      <img
        v-else
        class="card-img"
        src="/static/assets/event-placeholder.png"
        alt=""
      />
      <div v-if="website && !isUser" class="text-center pt-3">
        <a :href="website">
          <button type="button" class="btn simple-card-button">
            Go to website
          </button>
        </a>
      </div>
      <div class="mt-2" v-else>
        <div class="row d-flex justify-content-around">
          <div>
            <button type="button" class="btn btn-sm btn-outline-danger px-2">
              <i class="fa fa-heart" aria-hidden="true"></i
              >{{ interested }} likes
            </button>
          </div>
          <div>
            <button type="button" class="btn btn-sm btn-outline-primary px-2">
              <i class="fa fa-calendar" aria-hidden="true"></i
              >{{ participants }} going
            </button>
          </div>
        </div>
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
    "start_hour",
    "image",
    "website",
    "interested",
    "participants",
  ],
  data() {
    return {
      userInfo: null,
    };
  },
  methods: {
    eventDetail() {
      this.$router.push({
        path: `/events/${this.id}`,
      });
    },
    computeDate() {
      const options = {
        month: "long",
        day: "numeric",
        year: "numeric",
      }
      let startDate = new Date(this.start_date).toLocaleDateString(
        "en",
        options
      );
      let endDate = this.end_date;
      let startHour = this.start_hour;
      if (endDate) {
        endDate = new Date(this.end_date).toLocaleDateString("en", options);
        startDate += ` to ${endDate}`;
      }
      if (startHour) {
        startDate += ` at ${startHour}`;
      }
      return startDate;
    },
  },
  computed: {
    isUser() {
      return !!this.userInfo;
    },
  },
  created() {
    this.userInfo = this.$store.getters["user/getUserInfo"];
  },
};
</script>

<style scoped>
.card {
  cursor: pointer;
  border-radius: 30px;
  max-width: 400px;
  min-height: 300px;
  background: #ffffff;
  box-sizing: border-box;
}

.card:hover {
  border: 0.5px solid #1f6dad;
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

.simple-card-button {
  background: #ffffff;
  border: 1px solid #f1f1f1;
  box-shadow: 0 0.5px 1px 1px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
}

.simple-card-button:hover {
  box-shadow: 0 0 0 0 rgba(0, 0, 0, 0);
}
.btn-sm {
  width: 120px;
}
</style>
