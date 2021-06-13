<template>
  <div class="container">
    <div class="text-center">
      <div>
        <p class="home-claim p-2 mb-5">
          Discover all the best events around you.
        </p>
      </div>
      <div>
        <form @submit.prevent="searchEventsByCity">
          <div class="form-group mb-3">
            <input
              v-model="searchedCity"
              v-on:focus="clearErrors()"
              type="text"
              class="form-control form-rounded mb-4"
              :class="{ invalid: !searchFieldIsNotEmpty }"
              placeholder="Where are you going?"
              style="font-size: 40px"
            />
          </div>
          <p v-if="!searchFieldIsNotEmpty" style="color: #e32822">
            Please, insert a city name.
          </p>
          <button type="submit" class="search-btn">Go!</button>
        </form>
      </div>
    </div>
  </div>
  <div v-if="!isMobile">
    <events-slot
      background="azure"
      title="Most participated"
      :next="nextMostParticipatedEventsLink"
      next-type="participated"
    >
      <event-card
        v-for="ev in mostParticipatedEvents"
        :key="ev.id"
        :name="ev.name"
        :id="ev.id"
        :organizer="ev.organizer_username"
        :venue="ev.venue"
        :start_date="ev.start_date"
        :end_date="ev.finish_date"
        :image="ev.event_image"
        :website="ev.event_website"
        :interested="ev.interested_count"
        :participants="ev.participants_count"
        :user_going="ev.user_is_going"
        :user_interested="ev.user_is_interested"
      >
      </event-card>
    </events-slot>
    <events-slot
      background="grey"
      title="Most interested"
      :next="nextMostInterestedEventsLink"
      next-type="interested"
    >
      <event-card
        v-for="ev in mostInterestedEvents"
        :key="ev.id"
        :name="ev.name"
        :id="ev.id"
        :organizer="ev.organizer_username"
        :venue="ev.venue"
        :start_date="ev.start_date"
        :end_date="ev.finish_date"
        :image="ev.event_image"
        :website="ev.event_website"
        :interested="ev.interested_count"
        :participants="ev.participants_count"
        :user_going="ev.user_is_going"
        :user_interested="ev.user_is_interested"
      >
      </event-card>
    </events-slot>
    <events-slot
      background="grey"
      title="Expiring"
      :next="nextExpiringEventsLink"
      next-type="expiring"
    >
      <event-card
        v-for="ev in expiringEvents"
        :key="ev.id"
        :id="ev.id"
        :name="ev.name"
        :organizer="ev.organizer_username"
        :venue="ev.venue"
        :start_date="ev.start_date"
        :end_date="ev.finish_date"
        :image="ev.event_image"
        :website="ev.event_website"
        :interested="ev.interested_count"
        :participants="ev.participants_count"
        :user_going="ev.user_is_going"
        :user_interested="ev.user_is_interested"
      >
      </event-card>
    </events-slot>
  </div>
  <div v-else>
    <events-slot-mobile
      background="azure"
      title="Most participated"
      sliderId="slider1"
      :next="nextMostParticipatedEventsLink"
      next-type="participated"
    >
      <div
        class="carousel-item"
        v-for="(ev, idx) in mostParticipatedEvents"
        :key="ev.id"
        :class="{ active: idx === 0 }"
      >
        <event-card
          :name="ev.name"
          :id="ev.id"
          :organizer="ev.organizer_username"
          :venue="ev.venue"
          :start_date="ev.start_date"
          :end_date="ev.finish_date"
          :is_mobile="true"
          :website="ev.event_website"
          :interested="ev.interested_count"
          :participants="ev.participants_count"
          :user_going="ev.user_is_going"
          :user_interested="ev.user_is_interested"
        >
        </event-card>
      </div>
    </events-slot-mobile>
    <events-slot-mobile
      background="grey"
      sliderId="slider2"
      title="Most interested"
      :next="nextMostInterestedEventsLink"
      next-type="interested"
    >
      <div
        class="carousel-item"
        v-for="(ev, idx) in mostInterestedEvents"
        :key="ev.id"
        :class="{ active: idx === 0 }"
      >
        <event-card
          :name="ev.name"
          :id="ev.id"
          :organizer="ev.organizer_username"
          :venue="ev.venue"
          :start_date="ev.start_date"
          :end_date="ev.finish_date"
          :is_mobile="true"
          :website="ev.event_website"
          :interested="ev.interested_count"
          :participants="ev.participants_count"
          :user_going="ev.user_is_going"
          :user_interested="ev.user_is_interested"
        >
        </event-card>
      </div>
    </events-slot-mobile>
    <events-slot-mobile
      background="grey"
      sliderId="slider3"
      title="Expiring"
      :next="nextExpiringEventsLink"
      next-type="expiring"
    >
      <div
        class="carousel-item"
        v-for="(ev, idx) in expiringEvents"
        :key="ev.id"
        :class="{ active: idx === 0 }"
      >
        <event-card
          :name="ev.name"
          :id="ev.id"
          :organizer="ev.organizer_username"
          :venue="ev.venue"
          :start_date="ev.start_date"
          :end_date="ev.finish_date"
          :is_mobile="true"
          :website="ev.event_website"
          :interested="ev.interested_count"
          :participants="ev.participants_count"
          :user_going="ev.user_is_going"
          :user_interested="ev.user_is_interested"
        >
        </event-card>
      </div>
    </events-slot-mobile>
  </div>
  <scroll-to-top-arrow></scroll-to-top-arrow>
</template>

<script>
import EventCard from "../components/events/EventCard";
import EventsSlot from "../ui/EventsSlot";
import EventsSlotMobile from "../ui/EventsSlotMobile";
import ScrollToTopArrow from "../ui/ScrollToTopArrow";

export default {
  name: "Home",
  components: { EventsSlot, EventsSlotMobile, EventCard, ScrollToTopArrow },
  data() {
    return {
      searchedCity: "",
      searchFieldIsNotEmpty: true,
    };
  },

  methods: {
    validateSearchForm() {
      this.searchFieldIsNotEmpty = this.searchedCity !== "";
    },
    async searchEventsByCity() {
      this.validateSearchForm();
      if (!this.searchFieldIsNotEmpty) {
        return;
      }
      const city = this.searchedCity;
      await this.$store.dispatch("events/searchEventsByCity", city);
      await this.$router.push("/events");
    },
    clearErrors() {
      this.searchFieldIsNotEmpty = true;
    },
    async loadEvents() {
      try {
        await this.$store.dispatch("events/loadMostParticipatedEvents");
        await this.$store.dispatch("events/loadMostInterestedEvents");
        await this.$store.dispatch("events/loadExpiringEvents");
      } catch (error) {
        this.error = error.message || "Something went wrong!";
      }
    },
  },
  computed: {
    mostParticipatedEvents() {
      return this.$store.getters["events/getMostParticipatedEvents"];
    },
    nextMostParticipatedEventsLink() {
      return this.$store.getters["events/getNextMostParticipatedEventsLink"];
    },
    mostInterestedEvents() {
      return this.$store.getters["events/getMostInterestedEvents"];
    },
    nextMostInterestedEventsLink() {
      return this.$store.getters["events/getNextMostInterestedEventsLink"];
    },
    expiringEvents() {
      return this.$store.getters["events/getExpiringEvents"];
    },
    nextExpiringEventsLink() {
      return this.$store.getters["events/getNextExpiringEventsLink"];
    },
    isMobile() {
      return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
        navigator.userAgent
      );
    },
  },

  created() {
    this.loadEvents();
  },
};
</script>

<style scoped>
.form-rounded {
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  height: 80px;
}

.form-control::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  position: absolute;
  left: 15px;
  right: 29.27%;
  top: 27.5%;
  bottom: 26.25%;

  font-style: normal;
  font-size: 20px;
  line-height: 42px;

  color: #bdbdbd;
}

.home-claim {
  font-style: normal;
  font-weight: 500;
  font-size: 48px;
  line-height: 56px;
  text-align: center;

  /* Grey_1 */

  color: #575757;
}

.search-btn {
  width: 160px;
  height: 50px;
  left: 246px;
  top: 565px;
  background: #2c98f0;
  /* Blue_3 */

  border: 0.25px solid #1f6dad;
  box-sizing: border-box;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  color: white;
  font-size: 24px;
}

button:hover,
button:focus {
  outline: none;
  cursor: pointer;
  background-color: white;
  color: #2c98f0;
}

.invalid {
  border: 1px solid red;
}
</style>
