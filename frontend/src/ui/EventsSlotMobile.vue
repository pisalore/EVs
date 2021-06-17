<template>
  <div class="mt-5 py-4 text-center" :class="background">
    <div class="p-3">
      <h2 class="slot-title">{{ title }}</h2>
    </div>
    <div class="col">
      <div class="d-flex justify-content-center row">
        <div :id="sliderId" class="carousel slide" data-interval="false">
          <div class="carousel-inner">
            <slot></slot>
          </div>
          <a
            class="carousel-control-prev"
            :href="getSliderId"
            role="button"
            data-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            :href="getSliderId"
            role="button"
            data-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
    </div>
    <div>
      <button
        @click="goToEventsPageByType"
        type="button"
        class="btn btn-success px-4 mt-2"
      >
        {{ goTostring }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "EventsSlotMobile",
  props: {
    background: {
      type: String,
      required: false,
      default: null,
    },
    title: {
      type: String,
      required: true,
    },
    next: {
      type: String,
      required: false,
      default: null,
    },
    nextType: {
      type: String,
      required: false,
    },
    sliderId: {
      required: true,
    },
  },
  computed: {
    getSliderId() {
      return "#" + this.sliderId;
    },
    goTostring() {
      if (this.nextType === "expiring") {
        return "See all expiring events!";
      } else if (this.nextType === "participated") {
        return "See all most participated events!";
      } else if (this.nextType === "interested") {
        return "See all most interested events!";
      }
      return "Go to events";
    },
  },
  methods: {
    async goToEventsPageByType() {
      let searchString = "api/";
      if (this.nextType === "expiring") {
        searchString += "expiring";
      } else if (this.nextType === "participated") {
        searchString += "most-participated";
      } else if (this.nextType === "interested") {
        searchString += "most-interested";
      }
      searchString += "/";
      await this.$store.dispatch("events/loadEventsInPageEvents", searchString);
      await this.$router.push("/events");
    },
  },
};
</script>

<style scoped>
.azure {
  background-color: #dfebf9;
  border-radius: 30px;
}
.grey {
  background-color: #f0f2f5;
  border-radius: 30px;
}
.carousel-control-next-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='blue' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E");
}
.carousel-control-prev-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='blue' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E");
}
</style>
