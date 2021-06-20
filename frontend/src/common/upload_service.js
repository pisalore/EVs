import { CSRF_TOKEN } from "./csrf_token.js";
import { getJSON } from "./api.service";

function uploadEventCover(endpoint, file, eventId, organizerId) {
  let formData = new FormData();
  formData.append("event_image.document", file);
  formData.append("event_image.event", eventId);
  formData.append("event_image.loaded_by", organizerId);

  const config = {
    method: "PUT",
    body: formData,
    headers: {
      "X-CSRFToken": CSRF_TOKEN,
    },
  };
  return fetch(endpoint, config).then(getJSON);
}

function uploadProfileImage(endpoint, file, userId) {
  let formData = new FormData();
  formData.append("profile_image.document", file);
  formData.append("profile_image.loaded_by", userId);

  const config = {
    method: "PUT",
    body: formData,
    headers: {
      "X-CSRFToken": CSRF_TOKEN,
    },
  };
  return fetch(endpoint, config).then(getJSON);
}

export { uploadEventCover, uploadProfileImage };
