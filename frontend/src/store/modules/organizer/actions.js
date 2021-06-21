import { apiService } from "../../../common/api.service";

export default {
  async loadOrganizerAvailableEvents(context) {
    let endpoint = "/api/events/organizer/managed-events/?status=A";
    const response = await apiService(endpoint);
    context.commit("setOrganizerAvailableEvents", response.results);
    context.commit("setOrganizerAvailableEventsNextLink", response.next);
  },
  async loadOrganizerScheduledEvents(context) {
    let endpoint = "/api/events/organizer/managed-events/?status=S";
    const response = await apiService(endpoint);

    context.commit("setOrganizerScheduledEvents", response.results);
    context.commit("setOrganizerScheduledEventsNextLink", response.next);
  },
  async loadOrganizerCanceledEvents(context) {
    let endpoint = "/api/events/organizer/managed-events/?status=C";
    const response = await apiService(endpoint);
    context.commit("setOrganizerCanceledEvents", response.results);
    context.commit("setOrganizerCanceledEventsNextLink", response.next);
  },
  async loadNextEvents(context, info) {
    if (info.endpoint) {
      const response = await apiService(info.endpoint);
      if (info.type === "organizer-available") {
        context.commit("setOrganizerAvailableEventsNextLink", response.next);
        context.commit("updateOrganizerAvailableEvents", response.results);
      } else if (info.type === "organizer-scheduled") {
        context.commit("setOrganizerScheduledEventsNextLink", response.next);
        context.commit("updateOrganizerScheduledEvents", response.results);
      } else if (info.type === "organizer-canceled") {
        context.commit("setOrganizerCanceledEventsNextLink", response.next);
        context.commit("updateOrganizerCanceledEvents", response.results);
      }
    }
  },
};
