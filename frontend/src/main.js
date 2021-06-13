import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import EventCard from "./components/events/EventCard";
import EventsSlot from "./ui/EventsSlot";
import Snackbar from "./ui/Snackbar";
import BaseBadge from "./ui/BaseBadge";
import FilterEvents from "./components/events/FilterEvents";
import ScrollToTopArrow from "./ui/ScrollToTopArrow";

const app = createApp(App);

app.use(router);
app.use(store);

app.component("event-card", EventCard);
app.component("events-slot", EventsSlot);
app.component("filter-events", FilterEvents);
app.component("snackbar", Snackbar);
app.component("base-badge", BaseBadge);
app.component("scroll-arrow", ScrollToTopArrow);

app.mount("#app");
