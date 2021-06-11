import { CSRF_TOKEN } from "./csrf_token.js";

async function getJSON(response) {
  if (response.ok) {
    if (response.status === 204) return "";
    return response.json();
  } else {
    console.log("error", response);
    throw new Error(`${response.status}- ${response.statusText}`);
  }
}

function apiService(endpoint, method, data) {
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: { "content-type": "application/json", "X-CSRFToken": CSRF_TOKEN },
  };
  return fetch(endpoint, config).then(getJSON);
}

export { apiService };
