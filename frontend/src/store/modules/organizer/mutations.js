export default {
  setOrganizerAvailableEvents(state, payload) {
    state.organizerAvailableEvents = payload;
  },
  setOrganizerAvailableEventsNextLink(state, payload) {
    state.organizerNextAvailableEvents = payload;
  },
  setOrganizerScheduledEvents(state, payload) {
    state.organizerScheduledEvents = payload;
  },
  setOrganizerScheduledEventsNextLink(state, payload) {
    state.organizerNextScheduledEvents = payload;
  },
  setOrganizerCanceledEvents(state, payload) {
    state.organizerCanceledEvents = payload;
  },
  setOrganizerCanceledEventsNextLink(state, payload) {
    state.organizerNextCanceledEvents = payload;
  },
  updateOrganizerAvailableEvents(state, payload) {
    payload.forEach(function (ev) {
      state.organizerAvailableEvents.push(ev);
    });
  },
  updateOrganizerScheduledEvents(state, payload) {
    payload.forEach(function (ev) {
      state.organizerScheduledEvents.push(ev);
    });
  },
  updateOrganizerCanceledEvents(state, payload) {
    payload.forEach(function (ev) {
      state.organizerCanceledEvents.push(ev);
    });
  },
};
