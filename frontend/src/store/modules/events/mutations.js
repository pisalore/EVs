export default {
  setMostParticipatedEvents(state, payload) {
    state.mostParticipatedEvents = payload;
  },
  setMostInterestedEvents(state, payload) {
    state.mostInterestedEvents = payload;
  },
  setExpiringEvents(state, payload) {
    state.expiringEvents = payload;
  },
  setNextMostParticipatedEventsLink(state, payload) {
    state.nextMostParticipatedEventsLink = payload;
  },
  setNextMostInterestedEvents(state, payload) {
    state.nextMostInterestedEvents = payload;
  },
  setNextExpiringEvents(state, payload) {
    state.nextExpiringEvents = payload;
  },
  updateMostParticipatedEvents(state, payload) {
    payload.forEach(function (ev) {
      console.log(ev);
      state.mostParticipatedEvents.push(ev);
    });
  },
};
