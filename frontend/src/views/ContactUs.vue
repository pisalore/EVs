<template>
  <snackbar
    v-if="showSnackbar"
    :is_error="isError"
    :color="snackBarColor"
    :message="snackbarMessage"
    @close="snackbarFalse"
  ></snackbar>
  <div class="container">
    <h2 class="title">Contact Us</h2>
    <h3 class="subtitle">
      Hello <span class="username">@{{ username }}</span
      >! Please, read our
      <router-link to="/faq">FAQ</router-link>
      , otherwise contact us compiling the above form, we will answer as soon
      possible.
    </h3>
  </div>
  <div>
    <div class="mt-5 container">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ firstName }} {{ lastName }}</h5>
          <h5 class="card-title">{{ userEmail }}</h5>
          <form @submit.prevent="sendHelpRequest">
            <div v-if="username === 'visitor'" class="form-group">
              <label for="inputEmail1">Email address</label>
              <input
                type="email"
                class="form-control"
                v-model="userEmailForm"
                id="inputEmail1"
                aria-describedby="emailHelp"
                placeholder="Enter your email"
              />
              <small id="emailHelp" class="form-text text-muted"
                >We'll never share your email with anyone else.</small
              >
            </div>
            <div class="form-group">
              <textarea
                class="form-control"
                v-model="userMessage"
                placeholder="Describe your doubts or problems here..."
                rows="7"
              ></textarea>
            </div>
            <div class="d-flex justify-content-center">
              <button type="submit" class="btn btn-lg btn-primary">
                Email Us!
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
import Snackbar from "../ui/Snackbar";

export default {
  name: "ContactUs",
  components: { Snackbar },
  data() {
    return {
      isError: false,
      snackbarMessage: "",
      userMessage: "",
      userEmailForm: "",
      snackBarColor: "",
      showSnackbar: false,
    };
  },
  methods: {
    async loadUserInfo() {
      await this.$store.dispatch("user/loadUserInfo", null);
    },
    async sendHelpRequest() {
      let content = {
        user_email: this.userEmail ? this.userEmail : this.userEmailForm,
        username: this.username,
        user_message: this.userMessage,
      };
      try {
        let endpoint = "api/contactus/";
        await apiService(endpoint, "POST", content);
        this.snackbarMessage = "Message sent correctly.";
        this.snackBarColor = "#3DB834";
        this.showSnackbar = true;
        this.userMessage = "";
      } catch (error) {
        this.isError = true;
        this.snackbarMessage = error;
        this.snackBarColor = "#E32822";
        this.showSnackbar = true;
      }
    },
    snackbarFalse() {
      this.showSnackbar = false;
      this.isError = false;
      this.snackbarMessage = "";
      this.snackBarColor = "";
    },
  },
  computed: {
    username() {
      const username = this.$store.getters["user/getUserInfo"].username;
      if (username) {
        return username;
      } else {
        return "visitor";
      }
    },
    firstName() {
      return this.$store.getters["user/getUserInfo"].first_name;
    },
    lastName() {
      return this.$store.getters["user/getUserInfo"].last_name;
    },
    userEmail() {
      return this.$store.getters["user/getUserInfo"].email;
    },
  },
  created() {
    this.loadUserInfo();
  },
};
</script>

<style scoped>
.card {
  background-color: #dfebf9;
  border-radius: 30px;
}

.form-control {
  border-radius: 10px;
}

.title {
  font-style: normal;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  color: #1f6dad;
}

.subtitle {
  font-weight: 100;
  font-size: 36px;
  line-height: 42px;
  color: #575757;
}

.username {
  font-style: normal;
  font-weight: normal;
  font-size: 36px;
  line-height: 42px;

  /* Grey_1 */

  color: #575757;
}
</style>
