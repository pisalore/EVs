import { CSRF_TOKEN } from "./csrf_token.js";

async function getJSON(response) {
  if (response.ok) {
    if (response.status === 204) return "";
    return response.json();
  }
  return response.text().then((text) => {
    const errors = JSON.parse(text);
    let stringErrors = "";
    for (var key in errors) {
      stringErrors += errors[key] + " ";
      console.log(stringErrors);
    }
    throw new Error(stringErrors);
  });
}

function apiService(endpoint, method, data) {
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: { "content-type": "application/json", "X-CSRFToken": CSRF_TOKEN },
  };
  return fetch(endpoint, config).then(getJSON);
}

export { apiService, getJSON };
