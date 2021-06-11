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
  getNextMostInterestedEventsLink(state) {
    return state.nextMostInterestedEventsLink;
  },
  getNextExpiringEventsLink(state) {
    return state.nextExpiringEventsLink;
  },
  getShowedEventsInEventsPage(state) {
    return state.eventsPageEvs;
  },
  getNextShowedEventsInEventsLink(state) {
    return state.nextEventsPageEvsLink;
  },
};
