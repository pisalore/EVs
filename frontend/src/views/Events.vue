<template>
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
  computed: {
    showedEvents() {
      return this.$store.getters["events/getShowedEventsInEventsPage"];
    },
    nextShowedEventsInEventsLink() {
      return this.$store.getters["events/getNextShowedEventsInEventsLink"];
    },
  },
};
</script>

<style scoped></style>
