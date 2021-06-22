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
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
import Notification from "../components/Notification";
import ScrollToTopArrow from "../ui/ScrollToTopArrow";

export default {
  name: "Notifications",
  components: { Notification, ScrollToTopArrow },
  data() {
    return {
      notificationsList: [],
      isLoading: true,
    };
  },
  methods: {
    async loadNotifications() {
      let endpoint = "/api/notifications/";
      const response = await apiService(endpoint);
      this.notificationsList = await response;
    },
    async setNotificationsRead() {
      let endpoint = "/api/notifications-read/";
      await apiService(endpoint, "POST");
    },
  },
  async created() {
    await this.loadNotifications();
    this.isLoading = false;
  },
  beforeUpdate() {
    this.setNotificationsRead();
  },
};
</script>

<style scoped></style>
