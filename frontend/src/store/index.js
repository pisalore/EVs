import Vue from "vue";
import Vuex from "vuex";

import EventsModule from "./modules/events/index";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    events: EventsModule,
  },
});

export default store;
