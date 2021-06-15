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
  },
};
