<template>
  <div class="p-4">
    <form @submit.prevent="searchEventsUsingFilters">
      <div class="container-fluid">
        <div class="row">
          <div class="col-xl-3 mt-4">
            <span class="title">Filter by:</span>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <input
                type="text"
                v-model="filterCity"
                class="form-control"
                id="inlineFormInputGroup"
                placeholder="Enter a city..."
              />
            </div>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <input
                class="form-control"
                placeholder="From date..."
                type="text"
                v-model="fromDate"
                onfocus="(this.type='date')"
              />
            </div>
            <div class="input-group-lg my-3">
              <input
                class="form-control"
                placeholder="...to date"
                type="text"
                v-model="toDate"
                onfocus="(this.type='date')"
              />
            </div>
          </div>
          <div class="dropdown col-xl-3 my-3">
            <button
              type="button"
              class="btn btn-lg btn-outline-primary dropdown-toggle"
              data-toggle="dropdown"
            >
              Select some event category...
            </button>
            <div class="dropdown-menu">
              <a
                class="dropdown-item color-category"
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
        <hr>
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
          <div class="mt-5 col-xl-12 d-flex justify-content-center">
            <div class="py-2">
              <button type="submit" class="btn btn-lg btn-success mx-2">
                Search
              </button>
            </div>
            <div class="py-2">
              <button
                @click="clearAllFilters"
                type="submit"
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
  data() {
    return {
      searchIsValid: false,
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
      console.log(this.searchCategories);
    },
    removeCategory(category) {
      console.log(category);
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
      this.validateForm();
      console.log(this.searchIsValid);
      if (this.searchIsValid) {
        let searchString = "api/events/?";
        if (this.filterCity) {
          searchString += `venue=${this.filterCity}`;
        }
        if (this.fromDate) {
          searchString += `&start_date=${this.fromDate}`;
        }
        if (this.toDate) {
          searchString += `&end_date=${this.toDate}`;
        }
        if (this.searchCategories.length) {
          searchString += "&categories=";
          this.searchCategories.forEach((category) => {
            searchString += `${category.id}&`;
          });
        }
        if (searchString.charAt(-1) === "&") {
          searchString.slice(0, -1);
        }
        console.log(searchString);
        await this.$store.dispatch(
          "events/loadEventsInPageEvents",
          searchString
        );
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
    this.filterCity = this.$store.getters["events/getSearchedCity"];
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
</style>
