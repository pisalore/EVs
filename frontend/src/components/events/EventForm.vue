<template>
  <form @submit.prevent="submitForm">
    <div class="form-div">
      <div class="p-4">
        <h1 class="title">1. Add ev’s main information.</h1>
        <h2 class="subtitle">
          Provide an evocative name and information you think are useful for
          potential participants. For example: age range, restrictions, how to
          get ev location, services...
        </h2>
        <div class="form-group">
          <label for="evName">Event name</label>
          <input
            v-model="formEventName"
            type="text"
            class="form-control"
            id="evName"
            placeholder="Event name..."
            :class="{ invalid: nameError }"
            @focus="nameError = false"
          />
        </div>
        <div class="form-group">
          <label for="evDescription">Ev description</label>
          <textarea
            v-model="formEventDescription"
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
            v-model="formEventVenue"
            type="text"
            class="form-control"
            id="evVenue"
            placeholder="Event venue..."
          />
        </div>
        <div class="col-xl-12">
          <div class="row my-2">
            <div class="col-xl-4 mt-2"><span>Start date and hour</span></div>
            <div class="col-xl-4">
              <input
                v-model="formEventStartDate"
                class="form-control"
                type="date"
                id="startDate"
                :class="{ invalid: formError2 }"
                @focus="formError2 = false"
              />
            </div>
            <div class="col-xl-4">
              <input
                v-model="formEventStartTime"
                class="form-control"
                type="time"
                id="startTime"
                @focus="formError2 = false"
              />
            </div>
          </div>
          <div class="row my-2">
            <div class="col-xl-4 mt-2"><span>Finish date and hour</span></div>
            <div class="col-xl-4">
              <input
                v-model="formEventEndDate"
                class="form-control"
                type="date"
                id="endDate"
                :class="{ invalid: formError2 }"
              />
            </div>
            <div class="col-xl-4">
              <input
                v-model="formEventEndTime"
                class="form-control"
                type="time"
                id="endTime"
              />
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
            v-model="formEventWebsite"
            type="text"
            class="form-control"
            id="evWebsite"
            placeholder="Event website..."
          />
        </div>
        <div class="form-group">
          <label for="evTickets">Tickets</label>
          <input
            v-model="formEventTickets"
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
        <div class="col-xl-12" :class="{ row: !isMobile }">
          <div class="dropdown mt-3">
            <button
              type="button"
              class="btn btn-lg btn-outline-primary dropdown-toggle"
              data-toggle="dropdown"
            >
              Add event status
            </button>
            <div class="dropdown-menu">
              <a
                class="dropdown-item text-center"
                style="cursor: pointer"
                v-for="status in statuses"
                :key="status.status"
                @click="changeStatus(status.status)"
              >
                {{ status.label }}
              </a>
            </div>
          </div>
          <div
            class="col-xl-8 mt-2"
            :class="{ 'd-flex justify-content-center': isMobile }"
          >
            <base-badge
              :content="eventStatus"
              :type="'badge'"
              :category-style="badgeStyle(eventStatus)"
            ></base-badge>
          </div>
          <div class="mt-4">
            You can delete the event only if it is set on "Canceled" status.
          </div>
          <div
            v-if="eventStatus === 'Canceled'"
            class="col-xl-2 mt-3 d-flex justify-content-center"
          >
            <button class="btn btn-danger">Delete Event</button>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <button type="submit" class="btn btn-success btn-lg mt-4">
        Update Event
      </button>
    </div>
  </form>
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
      formEventName: this.event.name ? this.event.name : "",
      formEventDescription: this.event.description
        ? this.event.description
        : "",
      formEventVenue: this.event.venue ? this.event.venue : "",
      formEventWebsite: this.event.event_website
        ? this.event.event_website
        : "",
      formEventTickets: this.event.tickets_website
        ? this.event.tickets_website
        : "",
      formEventStartDate: this.event.start_date ? this.event.start_date : "",
      formEventEndDate: this.event.finish_date ? this.event.finish_date : "",
      formEventStartTime: this.event.start_hour ? this.event.start_hour : "",
      formEventEndTime: this.event.finish_hour ? this.event.finish_hour : "",
      nameError: false,
      formError2: false,
      formError3: false,
      categories: [],
      selectedCategories: [],
      statuses: [
        {
          status: "A",
          label: "Available",
        },
        {
          status: "S",
          label: "Scheduled",
        },
        {
          status: "C",
          label: "Canceled",
        },
      ],
      eventStatus: this.computeEventStatus(this.event.status),
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
    changeStatus(status) {
      this.eventStatus = this.computeEventStatus(status);
    },
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
      if (category === "Sport") {
        return "sport";
      }
      if (category === "Other") {
        return "other";
      }
      if (category === "Available") {
        return "available";
      }
      if (category === "Scheduled") {
        return "scheduled";
      }
      if (category === "Canceled") {
        return "canceled";
      }
    },
    computeEventStatus(status) {
      if (status === "A") {
        return "Available";
      } else if (status === "S") {
        return "Scheduled";
      } else if (status === "C") {
        return "Canceled";
      }
      return "";
    },
    validURL(str) {
      var pattern = new RegExp(
        "^(https?:\\/\\/)?" + // protocol
          "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
          "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
          "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
          "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
          "(\\#[-a-z\\d_]*)?$",
        "i"
      ); // fragment locator
      return !!pattern.test(str);
    },
    validateForm() {
      if (!this.formEventName) {
        this.nameError = true;
      }
      const fromDate = new Date(this.formEventStartDate);
      const toDate = new Date(this.formEventEndDate);
      this.formError2 = fromDate > toDate;
      if (this.formEventWebsite) {
        this.formError3 = !this.validURL(this.formEventWebsite);
      }
      if (this.formEventTickets) {
        this.formError3 = !this.validURL(this.formEventTickets);
      }
      console.log(this.nameError, this.formError2, this.formError3)
    },
    submitForm() {
      this.validateForm();
      if (!this.nameError && !this.formError2 && !this.formError3) {
        console.log("submit");
      }
    },
  },
  async created() {
    console.log(this.event);
    let endpoint = "/api/categories/";
    this.categories = await apiService(endpoint);
    this.selectedCategories = this.event.categories;
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
.invalid {
  border: 1px solid red;
}
</style>
