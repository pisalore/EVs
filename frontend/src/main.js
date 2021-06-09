import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import EventCard from "./components/events/EventCard";
import EventsSlot from "./ui/EventsSlot";

const app = createApp(App);

app.use(router);
app.use(store);

app.component("event-card", EventCard);
app.component("events-slot", EventsSlot);

app.mount("#app");
