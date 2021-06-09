import actions from "./actions.js";
import getters from "./getters.js";
import mutations from "./mutations";

export default {
  namespaced: true,
  state() {
    return {
      userInfo: {},
    };
  },
  actions,
  getters,
  mutations,
};
