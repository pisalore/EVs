<template>
  <pulse-loader
    v-if="isLoading"
    :loading="isLoading"
    color="#4BABFA"
    size="20px"
    class="spinner"
  ></pulse-loader>
  <div v-else>
    <scroll-to-top-arrow></scroll-to-top-arrow>
    <h1 class="title px-4">Your Profile</h1>
    <div class="row my-5">
      <div class="col-xl-2">
        <img
          v-if="!user.profile_image"
          src="https://evs-hci.s3.us-west-1.amazonaws.com/media/assets/no-image-profile.jpg"
          alt="Avatar"
        />
        <img v-else :src="user.profile_image.document" alt="Avatar" />
        <p class="text-center mt-2 username">@{{ user.username }}</p>
      </div>
      <div class="col-xl-7">
        <div class="user-main-info">
          <div class="container">
            <div class="row p-3">
              <div class="col-1 material-icons-outlined icon">info</div>
              <div class="col-11">{{ headerFirstInfo }}</div>
            </div>
            <div class="row p-3">
              <div class="col-1 material-icons-outlined icon">
                alternate_email
              </div>
              <div class="col-11">{{ user.email }}</div>
            </div>
            <div class="row p-3">
              <div class="col-1 material-icons-outlined icon">
                location_city
              </div>
              <div class="col-11">{{ user.city }}</div>
            </div>
            <div class="row p-3">
              <div class="col-1 material-icons-outlined icon">done_outline</div>
              <div class="col-11">Join EVs on {{ joinedDate }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-3 text-center my-2">
        <button class="btn btn-lg btn-primary">Edit Profile</button>
      </div>
    </div>
    <hr />
    <div v-if="!user.is_organizer" class="my-5">
      <h1 class="title px-4">Your Personal Events</h1>
      <events-slot
        background="azure"
        title="Upcoming"
        :next="nextUserGoingEventsLink"
        next-type="user-going"
        ><event-card
          v-for="ev in userGoingEvents"
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
      <events-slot
        background="azure"
        title="Interested in"
        :next="nextUserInterestedEventsLink"
        next-type="user-interested"
      >
        <event-card
          v-for="ev in userInterestedEvents"
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
    <div v-else class="my-5">
      <h1 class="title px-4">Your Personal Events</h1>
      <events-slot
        background="azure"
        title="Available"
        :next="nextUserGoingEventsLink"
        next-type="organizer-available"
        ><event-card
          v-for="ev in userGoingEvents"
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
      <events-slot
        background="azure"
        title="Interested in"
        :next="nextUserInterestedEventsLink"
        next-type="organizer-scheduled"
      >
        <event-card
          v-for="ev in userInterestedEvents"
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
      <events-slot
        background="azure"
        title="Interested in"
        :next="nextUserInterestedEventsLink"
        next-type="organizer-canceled"
      >
        <event-card
          v-for="ev in userInterestedEvents"
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
  </div>
</template>

<script>
import ScrollToTopArrow from "../../ui/ScrollToTopArrow";
import EventsSlot from "../../ui/EventsSlot";
import EventCard from "../events/EventCard";
export default {
  name: "UserInfo",
  components: { EventsSlot, EventCard, ScrollToTopArrow },
  props: ["user"],
  emits: ["loading-finished"],
  data() {
    return {
      isLoading: false,
    };
  },
  computed: {
    userGoingEvents() {
      return this.$store.getters["user/getUserGoingEvents"];
    },
    userInterestedEvents() {
      return this.$store.getters["user/getUserInterestedEvents"];
    },
    nextUserGoingEventsLink() {
      return this.$store.getters["user/getUserGoingEventsNextLink"];
    },
    nextUserInterestedEventsLink() {
      return this.$store.getters["user/getUserInterestedEventsNextLink"];
    },
    headerFirstInfo() {
      return this.user.is_organizer
        ? this.user.organization_name
        : this.user.first_name + " " + this.user.last_name;
    },
    joinedDate() {
      let joinedDate = new Date(this.user.date_joined);
      let month = joinedDate.getUTCMonth() + 1; //months from 1-12
      let day = joinedDate.getUTCDate();
      let year = joinedDate.getUTCFullYear();
      return `${day}/${month}/${year}`;
    },
    isMobile() {
      return (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        ) || window.screen.width < 760
      );
    },
  },
  methods: {
    async loadUserEvents() {
      this.isLoading = true;
      if (!this.user.is_organizer) {
        await this.$store.dispatch("user/loadUserGoingEvents");
        await this.$store.dispatch("user/loadUserInterestedEvents");
      }
      this.isLoading = false;
    },
  },
  created() {
    console.log(this.user)
    this.loadUserEvents();
  },
};
</script>

<style scoped>
img {
  border-radius: 50%;
  max-width: 100%;
}
.user-main-info {
  background: #f0f2f5;
  border-radius: 30px;
  border-color: red;
  height: 100%;
  font-style: normal;
  font-weight: 200;
  font-size: 32px;
  line-height: 42px;
}
.icon {
  color: #1f6dad;
  font-size: 30px;
  margin-top: 5px;
}
.username {
  font-weight: 200;
  font-size: 36px;
  line-height: 42px;
}
.title {
  font-style: normal;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  color: #1f6dad;
}
</style>
