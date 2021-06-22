<template>
  <div class="container">
    <div v-if="notificationsList.length">
      <notification
        v-for="n in notificationsList"
        :key="n.id"
        :created-at="n.created_at"
        :message="n.message"
        :type="n.type"
        :is-read="n.user_has_read"
        :event-id="n.modified_event_id"
      ></notification>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
import Notification from "../components/Notification";
export default {
  name: "Notifications",
  components: { Notification },
  data() {
    return {
      notificationsList: [],
    };
  },
  methods: {
    async loadNotifications() {
      let endpoint = "/api/notifications/";
      const response = await apiService(endpoint);
      this.notificationsList = await response;
      console.log(this.notificationsList);
    },
    async setNotificationsRead() {
      let endpoint = "/api/notifications-read/";
      await apiService(endpoint, "POST");
    },
  },
  created() {
    this.loadNotifications();
  },
  beforeUnmount() {
    this.setNotificationsRead();
  },
};
</script>

<style scoped></style>
