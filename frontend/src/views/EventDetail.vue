<template>
  <div v-if="selectedEvent" class="ml-3" style="overflow: hidden">
    <div class="col-xl-12 container-fluid">
      <div class="row">
        <div class="col-xl-6 p-0 m-0">
          <h1 class="event-title my-3">{{ selectedEvent.name }}</h1>
          <h2 class="event-venue my-3">@{{ selectedEvent.venue }}</h2>
          <h2 class="event-time my-3">{{ computeDate }}</h2>
          <div class="row my-3 container">
            <div class="mr-4">
              <span class="px-2" style="color: #e32822">
                <i
                  class="material-icons mr-2"
                  aria-hidden="true"
                  style="font-size: 30px"
                  >favorite</i
                >{{ selectedEvent.interested_count }} likes
              </span>
            </div>
            <div>
              <span class="px-2" style="color: #1f6dad">
                <i
                  class="material-icons mr-2"
                  aria-hidden="true"
                  style="font-size: 30px"
                  >event_available</i
                >{{ selectedEvent.participants_count }} going
              </span>
            </div>
          </div>
          <div :class="{ 'text-center': isMobile }">
            <base-badge
              v-for="category in selectedEvent.categories"
              :key="category.id"
              :category="category"
              :categoryStyle="badgeStyle(category.category)"
              :type="'badge'"
            ></base-badge>
          </div>
        </div>
        <div class="col-xl-6 p-0 m-0" style="width: 100%; display: block">
          <img
            v-if="selectedEvent.event_image"
            :src="selectedEvent.event_image.document"
            alt=""
            :class="{
              'mobile-img-height': isMobile,
              'desktop-img-height': !isMobile,
            }"
          />
          <img
            v-else
            src="https://evs-hci.s3.us-west-1.amazonaws.com/media/assets/event-placeholder.png"
            alt=""
            :class="{
              'mobile-img-height': isMobile,
              'desktop-img-height': !isMobile,
            }"
          />
        </div>
        <div v-if="isMobile">
          <div class="my-3">
            <base-action-button
              :icon="'event_available'"
              :label="'Going'"
              :user-going="userIsGoing"
              @click="goingToggle"
              class="mx-1"
            ></base-action-button>
            <base-action-button
              v-if="!selectedEvent.user_is_going"
              :icon="'favorite'"
              :label="'Like'"
              :user-interested="userIsInterested"
              @click="likeToggle"
              class="mx-1"
            ></base-action-button>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-xl-6 p-0">
          <div class="mt-2">
            <h1 class="subtitle">Main information</h1>
          </div>
          <div class="main-info">
            <div class="d-flex">
              <base-badge
                :content="'Organizer'"
                :categoryStyle="badgeStyle()"
                :type="'badge'"
              ></base-badge>
              <div class="ml-auto mt-4 p-1 info">
                {{ selectedEvent.organizer_username }}
              </div>
            </div>
            <div class="d-flex">
              <base-badge
                :content="'Website'"
                :categoryStyle="badgeStyle()"
                :type="'badge'"
              ></base-badge>
              <div class="ml-auto mt-4 p-1 info">
                <a :href="selectedEvent.event_website">{{
                  selectedEvent.event_website
                }}</a>
              </div>
            </div>
            <div class="d-flex">
              <base-badge
                :content="'Tickets'"
                :categoryStyle="badgeStyle()"
                :type="'badge'"
              ></base-badge>
              <div class="ml-auto mt-4 p-1 info">
                <a :href="selectedEvent.tickets_website">{{
                  selectedEvent.tickets_website
                }}</a>
              </div>
            </div>
          </div>
          <div class="ev-description mt-">
            <div class="mt-4 pr-5">
              <h1 class="subtitle">Event detail</h1>
              <p class="description">{{ selectedEvent.description }}</p>
              <div v-if="!isMobile">
                <base-action-button
                  :icon="'event_available'"
                  :label="'Going'"
                  :user-going="userIsGoing"
                  @click="goingToggle"
                  class="action-button going-action-button"
                ></base-action-button>
                <base-action-button
                  v-if="!selectedEvent.user_is_going"
                  :icon="'favorite'"
                  :label="'Like'"
                  :user-interested="userIsInterested"
                  @click="likeToggle"
                  class="action-button like-action-button"
                ></base-action-button>
              </div>
            </div>
          </div>
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
  <scroll-to-top-arrow></scroll-to-top-arrow>
</template>

<script>
import { GoogleMap, Marker } from "vue3-google-map";
import { apiService } from "../common/api.service";
import BaseBadge from "../ui/BaseBadge";
import BaseActionButton from "../ui/BaseActionButton";
import ScrollToTopArrow from "../ui/ScrollToTopArrow";

export default {
  components: {
    ScrollToTopArrow,
    BaseActionButton,
    GoogleMap,
    Marker,
    BaseBadge,
  },
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
    computeDate() {
      const options = {
        month: "long",
        day: "numeric",
        year: "numeric",
      };
      let startDate = new Date(
        this.selectedEvent.start_date
      ).toLocaleDateString("en", options);
      let endDate = this.selectedEvent.end_date;
      if (endDate) {
        endDate = new Date(this.end_date).toLocaleDateString("en", options);
        startDate += ` to ${endDate}`;
      }
      let startHour = this.selectedEvent.start_hour;
      if (startHour) {
        startDate += `, at ${startHour}`;
      }
      return startDate;
    },
    userIsGoing() {
      return this.selectedEvent.user_is_going;
    },
    userIsInterested() {
      console.log(this.selectedEvent.user_is_interested);
      return this.selectedEvent.user_is_interested;
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
    badgeStyle(category) {
      if (category === "Food") {
        return "food";
      }
      if (category === "Art & Culture") {
        return "art";
      }
      if (category === "Music") {
        return "music";
      }
      if (category === "Other") {
        return "other";
      }
      if (category === "Sport") {
        return "sport";
      }
      if (!category) {
        if (this.isMobile) {
          return "base-mobile";
        } else {
          return "base"
        }
      }
    },
    async goingToggle() {
      const endpoint = `/api/events/${this.selectedEvent.id}/going/`;
      if (this.selectedEvent.user_is_going) {
        await apiService(endpoint, "DELETE");
      } else {
        await apiService(endpoint, "POST");
      }
      await this.$store.dispatch(
        "events/loadSelectedEvent",
        this.selectedEvent.id
      );
    },
    async likeToggle() {
      const endpoint = `/api/events/${this.selectedEvent.id}/interesting/`;
      if (this.selectedEvent.user_is_interested) {
        await apiService(endpoint, "DELETE");
      } else {
        await apiService(endpoint, "POST");
      }
      await this.$store.dispatch(
        "events/loadSelectedEvent",
        this.selectedEvent.id
      );
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
  height: 16vw;
}

.event-title {
  font-style: normal;
  font-weight: normal;
  font-size: 48px;
  line-height: 56px;
  margin-bottom: 15px;
  color: #1f6dad;
}

.event-venue {
  font-style: normal;
  font-weight: normal;
  font-size: 28px;
  line-height: 28px;
  color: #575757;
  margin-bottom: 15px;
}

.event-time {
  font-style: normal;
  font-weight: normal;
  font-size: 28px;
  line-height: 28px;
  margin-bottom: 15px;
  color: #bdbdbd;
}

.subtitle {
  font-weight: 400;
  font-size: 24px;
  line-height: 28px;
  color: #2c98f0;
}

.main-info {
  border-bottom: 0.5px solid #bdbdbd;
  margin-right: 50px;
}

.info {
  font-size: 18px;
}

.description {
  font-style: normal;
  font-weight: 300;
  font-size: 18px;
  line-height: 21px;
}
.action-button {
  display: block;
  position: fixed;
  z-index: 99;
  right: 50px;
}
.going-action-button {
  top: 180px;
}
.like-action-button {
  top: 260px;
}
</style>
