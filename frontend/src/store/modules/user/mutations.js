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
  setUserExpiredEvents(state, payload) {
    state.userExpiredEvents = payload;
  },
  setUserGoingEventsNextLink(state, payload) {
    state.userNextGoingEventsLink = payload;
  },
  setUserInterestedEventsNextLink(state, payload) {
    state.userNextInterestedEventsLink = payload;
  },
  setUserExpiredEventsNextLink(state, payload) {
    state.userNextExpiredEventsLink = payload;
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
  updateUserExpiredEvents(state, payload) {
    payload.forEach(function (ev) {
      state.userExpiredEvents.push(ev);
    });
  },
};
