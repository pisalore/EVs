import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import EventCard from "./components/events/EventCard";

const app = createApp(App);

app.use(router);
app.use(store);

app.component("event-card", EventCard);

app.mount("#app");
