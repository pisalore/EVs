import { CSRF_TOKEN } from "./csrf_token";
import { getJSON } from "./api.service";

function putForm(endpoint, formData) {
  for (var pair of formData.entries()) {
    console.log(pair[0] + ", " + pair[1]);
  }
  const config = {
    method: "PUT",
    body: formData,
    headers: {
      "X-CSRFToken": CSRF_TOKEN,
    },
  };
  return fetch(endpoint, config).then(getJSON);
}

export { putForm };
