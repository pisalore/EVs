<template>
  <div class="input-group">
    <span class="input-group-addon"><i class="fa fa-search"></i></span>
    <input
      id="searchByName"
      type="text"
      class="form-control"
      name="search"
      placeholder="Search events by name..."
      v-model="searchedEventName"
    />
  </div>
  <div>
    <events-slot :next="nextShowedEventsInEventsLink" next-type="evs">
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
      >
      </event-card>
    </events-slot>
  </div>
</template>

<script>
import EventCard from "../components/events/EventCard";
import EventsSlot from "../ui/EventsSlot";
export default {
  name: "Events",
  components: { EventCard, EventsSlot },
  data() {
    return {
      searchedEventName: "",
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
  },
  async created() {
    const state = this.$store.getters["events/getShowedEventsInEventsPage"];
    if (!state.length) {
      await this.$store.dispatch("events/loadEventsInPageEvents");
    }
  },
};
</script>

<style scoped></style>
