<template>
  <div class="card col-xl-3 mx-3 my-2" style="width: 18rem">
    <div class="card-body" @click="eventDetail">
      <h3 class="card-title">{{ name }}</h3>
      <h4 class="card-organizer">{{ organizer }}</h4>
      <h5 class="card-venue">@{{ venue }}</h5>
      <h5 class="card-date">{{ computeDate() }}</h5>
      <div class="img-div">
        <img
          v-if="image && !is_mobile"
          class="card-img-top"
          :src="image.document"
          alt="event-image"
        />
        <img
          v-else-if="!image && !is_mobile"
          class="card-img-top"
          src="https://evs-hci.s3.us-west-1.amazonaws.com/media/assets/event-placeholder.png"
          alt=""
        />
      </div>
      <div v-if="website && !isUser" class="text-center pt-5">
        <a :href="website">
          <button
            type="button"
            class="btn simple-card-button"
            onclick="event.stopPropagation()"
          >
            Go to website
          </button>
        </a>
      </div>
      <div class="mt-2" v-else>
        <div class="row d-flex justify-content-around pt-4">
          <div>
            <span class="px-2" style="color: #e32822">
              <i
                v-if="!user_interested"
                class="material-icons-outlined mr-1"
                aria-hidden="true"
                style="font-size: 30px"
                >favorite_border</i
              >
              <i
                v-else
                class="material-icons mr-1"
                aria-hidden="true"
                style="font-size: 30px"
                >favorite</i
              >{{ interested }} likes
            </span>
          </div>
          <div>
            <span class="px-2" style="color: #1f6dad">
              <i
                v-if="!user_going"
                class="material-icons mr-1"
                aria-hidden="true"
                style="font-size: 30px"
                >calendar_today</i
              >
              <i
                v-else
                class="material-icons mr-1"
                aria-hidden="true"
                style="font-size: 30px"
                >event_available</i
              >{{ participants }} going
            </span>
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
    "image",
    "is_mobile",
    "website",
    "interested",
    "participants",
    "user_going",
    "user_interested",
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
      };
      let startDate = new Date(this.start_date).toLocaleDateString(
        "en",
        options
      );
      let endDate = this.end_date;
      if (endDate) {
        endDate = new Date(this.end_date).toLocaleDateString("en", options);
        startDate += ` to ${endDate}`;
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

.card-img-top {
  border-radius: 20px;
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

.img-div {
  margin-top: 30px;
}
</style>
