import { apiService } from "../../../common/api.service";

export default {
  async loadUserInfo(context) {
    let endpoint = `api/user/`;
    const response = await apiService(endpoint);
    window.localStorage.setItem("userInfo", JSON.stringify(response));
    context.commit("setUserInfo", response);
  },
};
