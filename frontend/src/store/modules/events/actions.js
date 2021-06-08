import { apiService } from "../../../common/api.service";

export default {
  searchEventsByCity(context, city) {
    let endpoint = `api/events/?venue=${city}`;
    apiService(endpoint).then((response) => {
      console.log(response.results);
    });
  },
};
