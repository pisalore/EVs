export default {
  getExpiringEvents(state) {
    return state.expiringEvents;
  },
  getMostInterestedEvents(state) {
    return state.mostInterestedEvents;
  },

  getMostParticipatedEvents(state) {
    return state.mostParticipatedEvents;
  },
  getNextMostParticipatedEventsLink(state) {
    return state.nextMostParticipatedEventsLink;
  },
};
