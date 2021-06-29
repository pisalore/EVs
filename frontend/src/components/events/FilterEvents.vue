<template>
  <div class="p-2">
    <form @submit.prevent="searchEventsUsingFilters">
      <div class="container-fluid">
        <div class="row">
          <div class="col-xl-3 mt-4">
            <span class="title">Filter by:</span>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <label for="venue">Event venue:</label>
              <input
                type="text"
                v-model="filterCity"
                class="form-control"
                id="venue"
                placeholder="Enter a city..."
              />
            </div>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <label for="fromdate">From date...</label>
              <input
                class="form-control"
                :class="{ invalid: !searchIsValid }"
                @focus="searchIsValid = true"
                placeholder="From date..."
                type="date"
                v-model="fromDate"
                id="fromdate"
              />
            </div>
            <div class="input-group-lg my-3">
              <label for="todate">...to date</label>
              <input
                class="form-control"
                :class="{ invalid: !searchIsValid }"
                @focus="searchIsValid = true"
                placeholder="...to date"
                type="date"
                v-model="toDate"
                id="todate"
              />
              <p v-if="!searchIsValid" style="color: red">
                Start date must be before end date!
              </p>
            </div>
          </div>

          <div class="dropdown col-xl-3 mt-3">
            <label for="selectcategories">Events ategories...</label>
            <button
              type="button"
              class="btn btn-lg btn-outline-primary dropdown-toggle"
              data-toggle="dropdown"
              id="selectcategories"
            >
              Select some event category...
            </button>
            <div class="dropdown-menu">
              <a
                class="dropdown-item"
                v-for="category in categories"
                :key="category.id"
                @click="addCategory(category)"
              >
                {{ category.category }}
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="container-fluid my-2">
        <hr />
        <div class="row">
          <div class="col-xl-2 py-2">
            <span class="title">Selected categories:</span>
          </div>
          <div class="col-xl-10">
            <base-badge
              v-for="category in searchCategories"
              :key="category.id"
              :category="category"
              :categoryStyle="badgeStyle(category.category)"
              @close-chip="removeCategory"
            ></base-badge>
          </div>
          <div class="mt-2 col-xl-12 d-flex justify-content-center">
            <div class="py-2">
              <button type="submit" class="btn btn-lg btn-success mx-2">
                Search
              </button>
            </div>
            <div class="py-2">
              <button
                @click="clearAllFilters"
                type="button"
                class="btn btn-lg btn-outline-danger mx-2"
              >
                Clear
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { apiService } from "../../common/api.service";
import BaseBadge from "../../ui/BaseBadge";

export default {
  name: "FilterEvents",
  components: { BaseBadge },
  emits: ["searching", "searched"],
  data() {
    return {
      searchIsValid: true,
      categories: [],
      searchCategories: [],
      filterCity: "",
      fromDate: null,
      toDate: null,
    };
  },
  methods: {
    addCategory(category) {
      if (this.searchCategories.indexOf(category) === -1)
        this.searchCategories.push(category);
    },
    removeCategory(category) {
      const index = this.searchCategories.indexOf(category);
      this.searchCategories.splice(index, 1);
    },
    badgeStyle(category) {
      if (category === "Food") {
        return "food";
      }
      if (category === "Art & Culture") {
        return "art";
      }
      if (category === "Music") {
        return "music";
      }
      if (category === "Other") {
        return "other";
      }
      if (category === "Sport") {
        return "sport";
      }
    },
    validateForm() {
      if (this.toDate && this.fromDate) {
        const toDate = new Date(this.toDate);
        const fromDate = new Date(this.fromDate);
        this.searchIsValid = fromDate <= toDate;
      } else {
        this.searchIsValid = true;
      }
    },
    async searchEventsUsingFilters() {
      this.$emit("searching");
      this.validateForm();
      if (this.searchIsValid) {
        let searchString = "api/events/?";
        if (this.filterCity) {
          this.filterCity = this.filterCity.charAt(0).toUpperCase() + this.filterCity.slice(1);
          searchString += `venue=${this.filterCity}`;
          this.$store.dispatch("events/setSearchedCity", this.filterCity);
        }
        if (this.fromDate) {
          searchString += `&start_date=${this.fromDate}`;
          this.$store.dispatch("events/setSearchedFromDate", this.fromDate);
        }
        if (this.toDate) {
          searchString += `&end_date=${this.toDate}`;
          this.$store.dispatch("events/setSearchedToDate", this.toDate);
        }
        if (this.searchCategories.length) {
          searchString += "&categories=";
          this.searchCategories.forEach((category) => {
            searchString += `${category.id}&`;
          });
          this.$store.dispatch(
            "events/setSearchedCategories",
            this.searchCategories
          );
        }
        if (searchString.charAt(-1) === "&") {
          searchString.slice(0, -1);
        }
        await this.$store.dispatch(
          "events/loadEventsInPageEvents",
          searchString
        );
      }
      await this.$emit("searched");
      if (this.searchIsValid) {
        document
          .getElementById("results")
          .scrollIntoView({ block: "end", behavior: "smooth" });
      }
    },
    async clearAllFilters() {
      this.filterCity = "";
      this.toDate = null;
      this.fromDate = null;
      this.searchCategories = [];
      this.searchIsValid = false;
    },
  },
  async created() {
    let endpoint = "api/categories/";
    this.categories = await apiService(endpoint);
    this.filterCity = await this.$store.getters["events/getSearchedCity"];
    this.fromDate = await this.$store.getters["events/getSearchedFromDate"];
    this.toDate = await this.$store.getters["events/getSearchedToDate"];
    this.searchCategories = await this.$store.getters[
      "events/getSearchedCategories"
    ];
  },
};
</script>

<style scoped>
.title {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;

  color: #000000;
}

.dropdown-menu a {
  cursor: pointer;
}

.invalid {
  border: 1px solid red;
}
</style>
