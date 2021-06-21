<template>
  <form>
    <div class="form-div">
      <div class="p-4">
        <h1 class="title" id="form1">1. Add ev’s main information.</h1>
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
            required
            :class="{ invalid: nameError }"
            @focus="nameError = false"
          />
          <p v-if="nameError" style="color: red">
            Please, insert a valid name.
          </p>
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
    <div id="form2" class="form-div mt-3">
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
            required
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
                @focus="formError2 = false"
              />
              <p v-if="formError2" style="color: red">
                An event can not finish before start!
              </p>
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
            :class="{ invalid: websiteError }"
            @focus="websiteError = false"
          />
          <p v-if="websiteError" style="color: red">
            Please insert a valid URL. It must contain also the used protocol
            (http or https, for example: https://google.com).
          </p>
        </div>
        <div class="form-group">
          <label for="evTickets">Tickets</label>
          <input
            v-model="formEventTickets"
            type="text"
            class="form-control"
            id="evTickets"
            placeholder="Event tickets..."
            :class="{ invalid: ticketsError }"
            @focus="ticketsError = false"
          />
          <p v-if="ticketsError" style="color: red">
            Please insert a valid URL. It must contain also the used protocol
            (http or https, for example: https://google.com).
          </p>
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
                style="cursor: pointer"
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
            <button
              type="button"
              class="btn btn-danger"
              @click="showDeleteModal"
            >
              Delete Event
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <button
        v-if="event"
        type="button"
        class="btn btn-success btn-lg mt-4"
        @click="showUpdateModal"
      >
        Update Event
      </button>
      <button
        v-else
        type="button"
        class="btn btn-success btn-lg mt-4"
        @click="submitForm"
      >
        Create Event
      </button>
    </div>
  </form>
  <base-modal
    v-if="showModal"
    @cancel-modal="showModal = false"
    @confirm-modal="confirmModal"
    :title="modalTitle"
    :message="modalMessage"
    :confirm="modalConfirm"
    :cancel="modalCancel"
    :action="modalAction"
  ></base-modal>
</template>

<script>
import { apiService } from "../../common/api.service";
import BaseBadge from "../../ui/BaseBadge";
import BaseModal from "../../ui/BaseModal";

export default {
  name: "EventForm",
  components: { BaseBadge, BaseModal },
  props: ["event", "organizer", "isCreate"],
  emits: ["update-event", "delete-event", "create-event"],
  data() {
    return {
      modalTitle: "",
      modalMessage: "",
      modalAction: "",
      modalConfirm: "",
      modalCancel: "",
      formEventName: this.event ? this.event.name : "",
      formEventDescription: this.event ? this.event.description : "",
      formEventVenue: this.event ? this.event.venue : "",
      formEventWebsite: this.event ? this.event.event_website : "",
      formEventTickets: this.event ? this.event.tickets_website : "",
      formEventStartDate: this.event ? this.event.start_date : null,
      formEventEndDate: this.event ? this.event.finish_date : null,
      formEventStartTime: this.event ? this.event.start_hour : null,
      formEventEndTime: this.event ? this.event.finish_hour : null,
      nameError: false,
      formError2: false,
      websiteError: false,
      ticketsError: false,
      showModal: false,
      isModalUpdate: false,
      isModalDelete: false,
      categories: [],
      selectedCategories: this.event ? this.event.categories : [],
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
      eventStatus: this.event
        ? this.computeEventStatus(this.event.status)
        : "Scheduled",
      selectedStatus: this.event ? this.event.status : "S",
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
    confirmModal() {
      if (this.isModalUpdate) {
        this.isModalUpdate = false;
        this.submitForm();
      } else if (this.isModalDelete) {
        this.isModalDelete = false;
        this.deleteEvent();
      }
    },
    showUpdateModal() {
      this.isModalUpdate = true;
      this.modalAction = "confirm";
      this.modalTitle = "Event update";
      this.modalMessage = "Are you sure to update your event?";
      this.modalConfirm = "Confirm";
      this.modalCancel = "Cancel";
      this.showModal = true;
    },
    showDeleteModal() {
      this.isModalDelete = true;
      this.modalAction = "delete";
      this.modalTitle = "Event delete";
      this.modalMessage =
        "Are you sure to delete your event? This operation is not reversible";
      this.modalConfirm = "Confirm";
      this.modalCancel = "Cancel";
      this.showModal = true;
    },
    changeStatus(status) {
      this.selectedStatus = status;
      this.eventStatus = this.computeEventStatus(status);
    },
    addCategory(category) {
      let existing = this.selectedCategories.filter((c) => {
        return c.id === category.id;
      });
      if (!existing.length) {
        this.selectedCategories.push(category);
      }
    },
    removeCategory(category) {
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
      return "Scheduled";
    },
    validURL(url) {
      try {
        new URL(url);
      } catch (e) {
        return false;
      }
      return true;
    },
    validateForm() {
      if (!this.formEventName) {
        this.nameError = true;
        document
          .getElementById("form1")
          .scrollIntoView({ block: "start", behavior: "smooth" });
      }
      const fromDate = new Date(this.formEventStartDate);
      const toDate = new Date(this.formEventEndDate);
      this.formError2 = fromDate > toDate;
      if (this.formError2) {
        document
          .getElementById("form2")
          .scrollIntoView({ block: "start", behavior: "smooth" });
      }

      if (this.formEventWebsite) {
        this.websiteError = !this.validURL(this.formEventWebsite);
      }
      if (this.formEventTickets) {
        this.ticketsError = !this.validURL(this.formEventTickets);
      }
    },
    submitForm() {
      this.showModal = false;
      this.validateForm();
      if (
        !this.nameError &&
        !this.formError2 &&
        !this.websiteError &&
        !this.ticketsError
      ) {
        let formData = {
          name: this.formEventName,
          description: this.formEventDescription,
          status: this.selectedStatus,
          venue: this.formEventVenue,
          start_date: this.formEventStartDate,
          finish_date: this.formEventEndDate,
          start_hour: this.formEventStartTime,
          finish_hour: this.formEventEndTime,
          event_website: this.formEventWebsite,
          tickets_website: this.formEventTickets,
          organizer: this.organizer.id,
          categories: this.selectedCategories,
        };
        if (this.isCreate) {
          this.$emit("create-event", formData);
        } else {
          this.$emit("update-event", formData);
        }
      }
    },
    deleteEvent() {
      this.$emit("delete-event");
    },
  },
  async created() {
    let endpoint = "/api/categories/";
    this.categories = await apiService(endpoint);
    this.selectedCategories = this.event ? this.event.categories : [];
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
