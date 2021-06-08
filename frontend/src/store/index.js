import { createStore } from "vuex";

import EventsModule from "./modules/events/index";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    events: EventsModule,
  },
});
