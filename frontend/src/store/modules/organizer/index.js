import actions from "./actions.js";
import getters from "./getters.js";
import mutations from "./mutations.js";

export default {
  namespaced: true,
  state() {
    return {
      organizerAvailableEvents: {},
      organizerScheduledEvents: {},
      organizerCanceledEvents: {},
      organizerNextAvailableEventsLink: null,
      organizerNextScheduledEventsLink: null,
      organizerNextCanceledEventsLink: null,
    };
  },
  actions,
  getters,
  mutations,
};
