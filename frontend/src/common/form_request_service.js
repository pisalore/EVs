import { CSRF_TOKEN } from "./csrf_token";
import { getJSON } from "./api.service";

function submitForm(endpoint, method, formData) {
  const config = {
    method: method,
    body: formData,
    headers: {
      "X-CSRFToken": CSRF_TOKEN,
    },
  };
  return fetch(endpoint, config).then(getJSON);
}

export { submitForm };
