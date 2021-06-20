import { apiService } from "../../../common/api.service";

export default {
  async loadUserInfo(context, payload) {
    let endpoint = `/api/user/`;
    if (payload) {
      endpoint += payload;
    }
    const response = await apiService(endpoint);
    window.localStorage.setItem("userInfo", JSON.stringify(response));
    context.commit("setUserInfo", response);
    context.commit("setUserGoingEventsNextLink", response.next);
  },
  async loadUserGoingEvents(context) {
    let endpoint = "/api/events/user/personal-going-events/";
    const response = await apiService(endpoint);
    context.commit("setUserGoingEvents", response.results);
    context.commit("setUserGoingEventsNextLink", response.next);
  },
  async loadUserInterestedEvents(context) {
    let endpoint = "/api/events/user/personal-interested-events/";
    const response = await apiService(endpoint);
    context.commit("setUserInterestedEvents", response.results);
    context.commit("setUserInterestedEventsNextLink", response.next);
  },
  async loadNextEvents(context, info) {
    if (info.endpoint) {
      const response = await apiService(info.endpoint);
      if (info.type === "user-participated") {
        context.commit("setUserGoingEventsNextLink", response.next);
        context.commit("updateUserGoingEvents", response.results);
      } else if (info.type === "user-interested") {
        context.commit("setUserInterestedEventsNextLink", response.next);
        context.commit("updateUserInterestedEvents", response.results);
      }
    }
  },
};
