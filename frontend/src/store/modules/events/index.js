import actions from "./actions.js";
import getters from "./getters.js";
import mutations from "./mutations.js";

export default {
  namespaced: true,
  state() {
    return {
      eventsPageEvs: [],
      nextEventsPageEvsLink: null,
      mostParticipatedEvents: [],
      nextMostParticipatedEventsLink: null,
      mostInterestedEvents: [],
      nextMostInterestedEventsLink: null,
      expiringEvents: [],
      nextExpiringEventsLink: null,
      searchedCity: null,
      selectedDetailEvent: null,
      managedEvent: null,
    };
  },
  actions,
  getters,
  mutations,
};
