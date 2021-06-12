<template>
  <div class="p-4">
    <form>
      <div class="container-fluid">
        <div class="row justify-content-around">
          <div class="col-xl-2 mt-4">
            <span class="title">Filter by:</span>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <input
                type="text"
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
                onfocus="(this.type='date')"
              />
            </div>
            <div class="input-group-lg my-3">
              <input
                class="form-control"
                placeholder="...to date"
                type="text"
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
                @click="addCategory(category.category)"
              >
                {{ category.category }}
              </a>
            </div>
          </div>
        </div>
        <div class="col-xl-6">
          <base-badge
            v-for="category in searchCategories"
            :key="category.id"
            :category="category"
            :categoryStyle="badgeStyle(category)"
            @close-chip="removeCategory"
          ></base-badge>
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
      categories: [],
      searchCategories: [],
    };
  },
  methods: {
    addCategory(category) {
      if (this.searchCategories.indexOf(category) === -1)
        this.searchCategories.push(category);
      console.log(this.searchCategories);
    },
    removeCategory(category) {
      const index = this.searchCategories.indexOf(category);
      this.searchCategories.splice(index, 1);
    },
    badgeStyle(category) {
      console.log(category);
      if (category.category === "Food") {
        console.log(category)
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
  },
  async created() {
    let endpoint = "api/categories/";
    this.categories = await apiService(endpoint);
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


</style>
