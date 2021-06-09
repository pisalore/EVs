import actions from "./actions.js";
import getters from "./getters.js";
import mutations from "./mutations.js";

export default {
  namespaced: true,
  state() {
    return {
      mostParticipatedEvents: [],
      nextMostParticipatedEventsLink: null,
      mostInterestedEvents: [],
      nextMostInterestedEvents: null,
      expiringEvents: [],
      nextExpiringEvents: null,
    };
  },
  actions,
  getters,
  mutations,
};
