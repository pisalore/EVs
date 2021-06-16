<template>
  <div class="form-div">
    <div class="p-4">
      <h1 class="title">1. Add ev’s main information.</h1>
      <h2 class="subtitle">
        Provide an evocative name and information you think are useful for
        potential partecipants. For example: age range, restrictions, how to get
        ev location, services...
      </h2>
      <div class="form-group">
        <label for="evName">Event name</label>
        <input
          type="text"
          class="form-control"
          id="evName"
          placeholder="Event name..."
        />
      </div>
      <div class="form-group">
        <label for="evDescription">Ev description</label>
        <textarea
          class="form-control"
          id="evDescription"
          rows="5"
          placeholder="Description here..."
        ></textarea>
      </div>
    </div>
  </div>
  <div class="form-div mt-3">
    <div class="p-4">
      <h1 class="title">2. Add ev’s venue and date.</h1>
      <h2 class="subtitle">
        Provide the venue for your Ev and fill date and hour field.
      </h2>
      <div class="form-group">
        <label for="evVenue">Event venue</label>
        <input
          type="text"
          class="form-control"
          id="evVenue"
          placeholder="Event venue..."
        />
      </div>
      <div class="col-xl-12">
        <div class="row my-2">
          <div class="col-xl-4 mt-2"><span>Start date and hour</span></div>
          <div class="col-xl-8">
            <input class="form-control" type="datetime-local" id="startDate" />
          </div>
        </div>
        <div class="row my-2">
          <div class="col-xl-4 mt-2"><span>Finish date and hour</span></div>
          <div class="col-xl-8">
            <input class="form-control" type="datetime-local" id="endDate" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="form-div mt-3">
    <div class="p-4">
      <h1 class="title">3. Add ev’s website, tickets and categories.</h1>
      <h2 class="subtitle">
        Provide links to external services for the event you are creating
        (tickets, organization website...), choose interesting categories and
        set a status.
      </h2>
      <div class="form-group">
        <label for="evWebsite">Website</label>
        <input
          type="text"
          class="form-control"
          id="evWebsite"
          placeholder="Event website..."
        />
      </div>
      <div class="form-group">
        <label for="evTickets">Tickets</label>
        <input
          type="text"
          class="form-control"
          id="evTickets"
          placeholder="Event tickets..."
        />
      </div>
      <div class="col-xl-12" :class="{ row: !isMobile }">
        <div class="dropdown">
          <button
            type="button"
            class="btn btn-lg btn-outline-primary dropdown-toggle"
            data-toggle="dropdown"
          >
            Add categories...
          </button>
          <div class="dropdown-menu">
            <a
              class="dropdown-item text-center"
              v-for="category in categories"
              :key="category.id"
              @click="addCategory(category)"
            >
              {{ category.category }}
            </a>
          </div>
        </div>
        <div class="col-xl-8">
          <base-badge
            v-for="category in selectedCategories"
            :key="category.id"
            :category="category"
            :categoryStyle="badgeStyle(category.category)"
            @close-chip="removeCategory"
          ></base-badge>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../../common/api.service";
import BaseBadge from "../../ui/BaseBadge";

export default {
  name: "EventForm",
  components: { BaseBadge },
  props: ["event"],
  data() {
    return {
      categories: [],
      selectedCategories: [],
    };
  },
  computed: {
    isMobile() {
      return (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        ) || window.screen.width < 760
      );
    },
  },
  methods: {
    addCategory(category) {
      if (this.selectedCategories.indexOf(category) === -1)
        this.selectedCategories.push(category);
      console.log(this.selectedCategories);
    },
    removeCategory(category) {
      console.log(category);
      const index = this.selectedCategories.indexOf(category);
      this.selectedCategories.splice(index, 1);
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
  },
  async created() {
    let endpoint = "/api/categories/";
    this.categories = await apiService(endpoint);
  },
};
</script>

<style scoped>
.form-div {
  background: #fbfbfb;
  border: 1px solid #f0f2f5;
  box-sizing: border-box;
  border-radius: 30px;
}
.title {
  font-style: normal;
  font-weight: normal;
  font-size: 36px;
  line-height: 42px;
  color: #575757;
}
.subtitle {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #575757;
}
</style>
