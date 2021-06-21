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
        <div>
          <button class="btn btn-lg btn-primary" @click="toEditProfile">
            Edit Profile
          </button>
        </div>
      </div>
    </div>
    <hr />
    <div v-if="!user.is_organizer" class="my-5">
      <h1 class="title px-4">Your Personal Events</h1>
      <p class="px-4 subtitle">
        Click on an event card to see event details. Here you can discover your
        upcoming events, the ones you are interested in and the ones you
        enjoyed.
      </p>
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
          :status="ev.status"
          :published="true"
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
          :status="ev.status"
          :published="true"
        >
        </event-card>
      </events-slot>
      <events-slot
        background="azure"
        title="Expired"
        :next="nextUserExpiredEventsLink"
        next-type="user-expired"
      >
        <event-card
          v-for="ev in userExpiredEvents"
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
          :status="ev.status"
          :published="true"
        >
        </event-card>
      </events-slot>
    </div>
    <div v-else class="my-5">
      <div class="col-xl-12">
        <h1 class="title px-4">Your Managed Events</h1>
      </div>
      <div class="col-xl-12">
        <p class="px-4 subtitle">
          Click on an event card to modify the event. They are categorized by
          their availability.
        </p>
      </div>
      <div class="col-xl-3 px-5 mt-4">
        <button class="btn btn-lg btn-primary" @click="createEvent">
          Create Ev
        </button>
      </div>
      <events-slot
        background="azure"
        title="Available"
        :next="nextOrganizerAvailableEventsLink"
        next-type="organizer-available"
        ><event-card
          v-for="ev in organizerAvailableEvents"
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
          :status="ev.status"
          :published="false"
        >
        </event-card>
      </events-slot>
      <events-slot
        background="azure"
        title="Scheduled"
        :next="nextOrganizerScheduledEventsLink"
        next-type="organizer-scheduled"
      >
        <event-card
          v-for="ev in organizerScheduledEvents"
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
          :status="ev.status"
          :published="false"
        >
        </event-card>
      </events-slot>
      <events-slot
        background="azure"
        title="Canceled"
        :next="nextOrganizerCanceledEventsLink"
        next-type="organizer-canceled"
      >
        <event-card
          v-for="ev in organizerCanceledEvents"
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
          :status="ev.status"
          :published="false"
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
    userExpiredEvents() {
      return this.$store.getters["user/getUserExpiredEvents"];
    },
    nextUserGoingEventsLink() {
      return this.$store.getters["user/getUserGoingEventsNextLink"];
    },
    nextUserInterestedEventsLink() {
      return this.$store.getters["user/getUserInterestedEventsNextLink"];
    },
    nextUserExpiredEventsLink() {
      return this.$store.getters["user/getUserExpiredEventsNextLink"];
    },
    organizerAvailableEvents() {
      return this.$store.getters["organizer/getOrganizerAvailableEvents"];
    },
    organizerScheduledEvents() {
      return this.$store.getters["organizer/getOrganizerScheduledEvents"];
    },
    organizerCanceledEvents() {
      return this.$store.getters["organizer/getOrganizerCanceledEvents"];
    },
    nextOrganizerAvailableEventsLink() {
      return this.$store.getters[
        "organizer/getOrganizerAvailableEventsNextLink"
      ];
    },
    nextOrganizerScheduledEventsLink() {
      return this.$store.getters[
        "organizer/getOrganizerScheduledEventsNextLink"
      ];
    },
    nextOrganizerCanceledEventsLink() {
      return this.$store.getters[
        "organizer/getOrganizerCanceledEventsNextLink"
      ];
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
    createEvent() {
      this.$router.push("/event-create");
    },
    async loadUserEvents() {
      this.isLoading = true;
      if (!this.user.is_organizer) {
        await this.$store.dispatch("user/loadUserGoingEvents");
        await this.$store.dispatch("user/loadUserInterestedEvents");
        await this.$store.dispatch("user/loadUserExpiredEvents");
      } else {
        await this.$store.dispatch("organizer/loadOrganizerAvailableEvents");
        await this.$store.dispatch("organizer/loadOrganizerScheduledEvents");
        await this.$store.dispatch("organizer/loadOrganizerCanceledEvents");
      }
      this.isLoading = false;
    },
    toEditProfile() {
      this.$router.push("/edit-profile");
    },
  },
  created() {
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
.subtitle {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #000000;
}
</style>
