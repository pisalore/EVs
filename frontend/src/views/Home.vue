<template>
  <div class="container py-4">
    <div>
      <p class="home-claim p-2 mb-5">
        Discover all the best events around you.
      </p>
    </div>
    <form @submit.prevent="searchCityEvents">
      <div class="input-group mb-3">
        <input
          type="text"
          class="form-control form-rounded input-lg mb-4"
          id="inputlg"
          placeholder="Where are you going?"
        />
      </div>
    </form>
    <button type="button" class="search-btn">Go!</button>
  </div>
</template>

<script>
import {apiService} from "../common/api.service";

export default {
  name: "Home",

  data() {
    return {
      searchedCity: "",
      formIsValid: true,
      questions: [],
    };
  },

  methods: {
    validateSearchForm() {
      this.formIsValid = true;
      if (this.searchedCity === "") {
        this.searchedCity.isValid = false;
      }
    },
    searchCityEvents() {
      this.validateSearchForm();
      if (!this.formIsValid) {
        return;
      }
      // const city = this.searchedCity;
    },
    getEvents() {
      let endpoint = "api/events/";
      apiService(endpoint).then((data) => {
        console.log(data.results);
      });
    },
  },

  created() {
    this.getEvents();
  },
};
</script>

<style scoped>
.form-rounded {
  box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  height: 80px;
  width: 820px;
}

.form-control::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  position: absolute;
  left: 2.68%;
  right: 29.27%;
  top: 27.5%;
  bottom: 26.25%;

  font-style: normal;
  font-size: 24px;
  line-height: 42px;

  color: #BDBDBD;
}


.home-claim {
  font-style: normal;
  font-weight: 500;
  font-size: 48px;
  line-height: 56px;
  text-align: center;

  /* Grey_1 */

  color: #575757;
}

.search-btn {
  width: 160px;
  height: 50px;
  left: 246px;
  top: 565px;
  background: #2C98F0;
  /* Blue_3 */

  border: 0.25px solid #1F6DAD;
  box-sizing: border-box;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  color: white;
  font-size: 24px;
}

button:hover, button:focus {
  outline: none;
  cursor: pointer;

}
</style>
