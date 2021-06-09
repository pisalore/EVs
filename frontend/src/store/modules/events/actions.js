import { apiService } from "../../../common/api.service";

export default {
  searchEventsByCity(context, city) {
    let endpoint = `api/events/?venue=${city}`;
    apiService(endpoint).then((response) => {
      console.log(response.results);
    });
  },
  async loadMostParticipatedEvents(context) {
    let endpoint = `api/most-participated/`;
    const response = await apiService(endpoint);

    context.commit("setNextMostParticipatedEventsLink", response.next);
    context.commit("setMostParticipatedEvents", response.results);
  },
  async loadMostInterestedEvents(context) {
    let endpoint = `api/most-interested/`;
    const response = await apiService(endpoint);

    context.commit("setNextMostInterestedEventsLink", response.next);
    context.commit("setMostInterestedEvents", response.results);

  },
  async loadExpiringEvents(context) {
    let endpoint = `api/expiring/`;
    const response = await apiService(endpoint);

    context.commit("setNextExpiringEventsLink", response.next);
    context.commit("setExpiringEvents", response.results);
  },
  async loadNextEvents(context, info) {
    if (info.endpoint) {
      const response = await apiService(info.endpoint);
      console.log(" res: ", response);
      if (info.type === "participated") {
        context.commit("setNextMostParticipatedEventsLink", response.next);
        context.commit("updateMostParticipatedEvents", response.results);
      } else if (info.type === "interested") {
        context.commit("setNextMostInterestedEventsLink", response.next);
        context.commit("updateMostInterestedEvents", response.results);
      } else if (info.type === "expiring") {
        context.commit("setNextExpiringEventsLink", response.next);
        context.commit("updateExpiringEvents", response.results);
      }
    }
  },
};
