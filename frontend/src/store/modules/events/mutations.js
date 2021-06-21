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
  setNextMostInterestedEventsLink(state, payload) {
    state.nextMostInterestedEventsLink = payload;
  },
  setNextExpiringEventsLink(state, payload) {
    state.nextExpiringEventsLink = payload;
  },
  updateMostParticipatedEvents(state, payload) {
    payload.forEach(function (ev) {
      state.mostParticipatedEvents.push(ev);
    });
  },
  updateMostInterestedEvents(state, payload) {
    payload.forEach(function (ev) {
      state.mostInterestedEvents.push(ev);
    });
  },
  updateExpiringEvents(state, payload) {
    payload.forEach(function (ev) {
      state.expiringEvents.push(ev);
    });
  },
  setEventsPageEvents(state, payload) {
    state.eventsPageEvs = payload;
  },
  updateEventsPageEvents(state, payload) {
    payload.forEach(function (ev) {
      state.eventsPageEvs.push(ev);
    });
  },
  setNextEventsPageEvsLink(state, payload) {
    state.nextEventsPageEvsLink = payload;
  },
  setSearchedCity(state, payload) {
    state.searchedCity = payload;
  },
  setDetailEvent(state, payload) {
    state.selectedDetailEvent = payload;
  },
  setManagedEvent(state, payload) {
    state.managedEvent = payload;
  },
};
