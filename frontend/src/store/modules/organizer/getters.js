export default {
  getOrganizerAvailableEvents(state) {
    return state.organizerAvailableEvents;
  },
  getOrganizerScheduledEvents(state) {
    return state.organizerScheduledEvents;
  },
  getOrganizerCanceledEvents(state) {
    return state.organizerCanceledEvents;
  },
  getOrganizerAvailableEventsNextLink(state) {
    return state.organizerNextAvailableEventsLink;
  },
  getOrganizerScheduledEventsNextLink(state) {
    return state.organizerNextScheduledEventsLink;
  },
  getOrganizerCanceledEventsNextLink(state) {
    return state.organizerNextCanceledEventsLink;
  },
};
