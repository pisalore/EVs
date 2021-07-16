<template>
  <div class="card col-xl-3 mx-3 my-2" style="width: 18rem">
    <div class="card-body d-flex flex-column" @click="eventDetail">
      <h3 class="card-title">{{ name }}</h3>
      <h4 class="card-organizer">{{ organizer }}</h4>
      <h5 class="card-venue">@{{ venue }}</h5>
      <h5 class="card-date">{{ computeDate() }}</h5>
      <h3 v-if="expired && status === 'A'" class="expired">EXPIRED</h3>
      <h3 v-if="expired && status === 'S'" class="scheduled">
        SCHEDULED - Note the past date
      </h3>
      <div v-if="!expired" class="img-div">
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
      <div class="mt-auto" v-if="!expired">
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
    "status",
    "published",
  ],

  data() {
    return {
      userInfo: null,
    };
  },
  methods: {
    eventDetail() {
      console.log(this.userInfo)
      if (this.published && !this.expired) {
        this.$router.push({
          path: `/events/${this.id}`,
        });
      }
      if (this.expired && this.userInfo.is_organizer) {
        this.$router.push({
          path: `/event-edit/${this.id}`,
        });
      }
    },
    computeDate() {
      if (!this.start_date) {
        return "";
      }
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
    expired() {
      let today = new Date().setHours(0, 0, 0, 0);
      let eventStartDate = new Date(this.start_date).setHours(0, 0, 0, 0);
      let eventFinishDate = new Date(this.end_date).setHours(0, 0, 0, 0);
      if (this.start_date && !this.end_date) {
        return eventStartDate < today;
      }
      if (this.start_date && this.end_date) {
        return eventFinishDate < today;
      }
      return false;
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

.expired {
  font-weight: bold;
  font-size: 24px;
  line-height: 24px;
  color: #e32822;
}

.scheduled {
  font-weight: bold;
  font-size: 24px;
  line-height: 24px;
  color: #ffbb33;
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
  width: 100%;
  height: 8vw;
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
