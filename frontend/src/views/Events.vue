<template>
  <pulse-loader
    v-if="isLoading"
    :loading="isLoading"
    color="#4BABFA"
    size="20px"
    class="spinner"
  ></pulse-loader>
  <div v-else>
    <div class="input-group px-4">
      <span>
        <i class="fa fa-search"></i>
      </span>
      <input
        type="search"
        class="form-control rounded"
        placeholder="Search by event name..."
        aria-label="Search"
        aria-describedby="search-addon"
        v-model="searchedEventName"
      />
    </div>
    <filter-events
      @searching="isLoading = true"
      @searched="isLoading = false"
    ></filter-events>
    <div>
      <events-slot
        :next="nextShowedEventsInEventsLink"
        next-type="evs"
        :title="'Searched Events'"
      >
        <event-card
          v-for="ev in showedEvents"
          :key="ev.id"
          :name="ev.name"
          :id="ev.id"
          :organizer="ev.organizer_username"
          :venue="ev.venue"
          :start_date="ev.start_date"
          :end_date="ev.finish_date"
          :start_hour="ev.start_hour"
          :image="ev.event_image"
          :website="ev.event_website"
          :interested="ev.interested_count"
          :participants="ev.participants_count"
          :is_mobile="isMobile"
        >
        </event-card>
      </events-slot>
      <scroll-to-top-arrow></scroll-to-top-arrow>
    </div>
  </div>
</template>

<script>
import EventCard from "../components/events/EventCard";
import EventsSlot from "../ui/EventsSlot";
import FilterEvents from "../components/events/FilterEvents";
import ScrollToTopArrow from "../ui/ScrollToTopArrow";

export default {
  name: "Events",
  components: {
    ScrollToTopArrow,
    EventCard,
    EventsSlot,
    FilterEvents,
  },
  data() {
    return {
      searchedEventName: "",
      isLoading: false,
    };
  },
  computed: {
    showedEvents() {
      const events = this.$store.getters["events/getShowedEventsInEventsPage"];
      if (this.searchedEventName === "") {
        return events;
      }
      return events.filter((event) => {
        if (
          event.name
            .toLowerCase()
            .includes(this.searchedEventName.toLocaleLowerCase())
        ) {
          return true;
        }
      });
    },
    nextShowedEventsInEventsLink() {
      return this.$store.getters["events/getNextShowedEventsInEventsLink"];
    },
    isMobile() {
      return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
        navigator.userAgent
      );
    },
  },
  async created() {
    const state = this.$store.getters["events/getShowedEventsInEventsPage"];
    if (!state.length) {
      this.isLoading = true;
      await this.$store.dispatch(
        "events/loadEventsInPageEvents",
        "api/events/"
      );
      this.isLoading = false;
    }
  },
};
</script>
