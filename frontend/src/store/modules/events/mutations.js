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
};
