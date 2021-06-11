import { createStore } from "vuex";

import EventsModule from "./modules/events/index";
import UserModule from "./modules/user/index";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    events: EventsModule,
    user: UserModule,
  },
});
