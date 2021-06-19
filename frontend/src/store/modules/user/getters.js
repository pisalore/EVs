export default {
  getUserInfo(state) {
    return state.userInfo;
  },
  getUserGoingEvents(state) {
    return state.userGoingEvents;
  },
  getUserInterestedEvents(state) {
    return state.userInterestedEvents;
  },
  getUserGoingEventsNextLink(state) {
    return state.userNextGoingEventsLink;
  },
  getUserInterestedEventsNextLink(state) {
    return state.userNextInterestedEventsLink;
  },
};
