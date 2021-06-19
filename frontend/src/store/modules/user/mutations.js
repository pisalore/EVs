export default {
  setUserInfo(state, payload) {
    state.userInfo = payload;
  },
  setUserGoingEvents(state, payload) {
    state.userGoingEvents = payload;
  },
  setUserInterestedEvents(state, payload) {
    state.userInterestedEvents = payload;
  },
  setUserGoingEventsNextLink(state, payload) {
    state.userNextGoingEventsLink = payload;
  },
  setUserInterestedEventsNextLink(state, payload) {
    state.userNextInterestedEventsLink = payload;
  },
  updateUserGoingEvents(state, payload) {
    payload.forEach(function (ev) {
      state.userGoingEvents.push(ev);
    });
  },
  updateUserInterestedEvents(state, payload) {
    payload.forEach(function (ev) {
      state.userInterestedEvents.push(ev);
    });
  },
};
