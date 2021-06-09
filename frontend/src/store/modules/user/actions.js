import { apiService } from "../../../common/api.service";

export default {
  async loadUserInfo(context) {
    let endpoint = `api/user/`;
    const response = await apiService(endpoint);
    window.localStorage.setItem("userInfo", JSON.stringify(response));
    if (!response.results) {
      throw new Error("Failed to fetch events.");
    }
    context.commit("setUserInfo", response);
  },
};
