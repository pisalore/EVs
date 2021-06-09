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
    if (!response.results) {
      throw new Error("Failed to fetch events.");
    }
    context.commit("setMostParticipatedEvents", response.results);
  },
  async loadMostInterestedEvents(context) {
    let endpoint = `api/most-interested/`;
    const response = await apiService(endpoint);
    if (!response.results) {
      throw new Error("Failed to fetch events.");
    }
    context.commit("setMostInterestedEvents", response.results);
  },
  async loadExpiringEvents(context) {
    let endpoint = `api/expiring/`;
    const response = await apiService(endpoint);
    if (!response.results) {
      throw new Error("Failed to fetch events.");
    }
    context.commit("setExpiringEvents", response.results);
  },
};
