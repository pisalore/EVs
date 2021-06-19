import actions from "./actions.js";
import getters from "./getters.js";
import mutations from "./mutations.js";

export default {
  namespaced: true,
  state() {
    return {
      userInfo: {},
      userGoingEvents: {},
      userNextGoingEventsLink: null,
      userInterestedEvents: {},
      userNextInterestedEventsLink: null,
    };
  },
  actions,
  getters,
  mutations,
};
