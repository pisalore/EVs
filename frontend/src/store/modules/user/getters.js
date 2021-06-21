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
  getUserExpiredEvents(state) {
    return state.userExpiredEvents;
  },
  getUserGoingEventsNextLink(state) {
    return state.userNextGoingEventsLink;
  },
  getUserInterestedEventsNextLink(state) {
    return state.userNextInterestedEventsLink;
  },
  getUserExpiredEventsNextLink(state) {
    return state.userNextExpiredEventsLink;
  },
};
