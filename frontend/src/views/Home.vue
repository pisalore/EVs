<template>
  <div class="container py-4">
    <div>
      <p class="home-claim p-2 mb-5">
        Discover all the best events around you.
      </p>
    </div>
    <form @submit.prevent="searchEventsByCity">
      <div class="input-group mb-3">
        <input
          v-model.trim="searchedCity"
          type="text"
          class="form-control form-rounded input-lg mb-4"
          id="inputlg"
          placeholder="Where are you going?"
          style="font-size: 40px; color: #bdbdbd"
        />
      </div>
      <button type="submit" class="search-btn">Go!</button>
    </form>
  </div>
</template>

<script>
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
      console.log("ok");
      this.formIsValid = true;
      if (this.searchedCity === "") {
        this.searchedCity.isValid = false;
      }
    },
    searchEventsByCity() {
      this.validateSearchForm();
      if (!this.formIsValid) {
        return;
      }
      const city = this.searchedCity;
      this.$store.dispatch("events/searchEventsByCity", city);
    },
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

.form-control::placeholder {
  /* Chrome, Firefox, Opera, Safari 10.1+ */
  position: absolute;
  left: 2.68%;
  right: 29.27%;
  top: 27.5%;
  bottom: 26.25%;

  font-style: normal;
  font-size: 24px;
  line-height: 42px;

  color: #bdbdbd;
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
  background: #2c98f0;
  /* Blue_3 */

  border: 0.25px solid #1f6dad;
  box-sizing: border-box;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 30px;
  color: white;
  font-size: 24px;
}

button:hover,
button:focus {
  outline: none;
  cursor: pointer;
}
</style>
