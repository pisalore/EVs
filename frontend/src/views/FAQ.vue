<template>
  <div class="text-center py-1">
    <h2 class="title">
      EVS Frequently Asked <br />
      Questions
    </h2>
    <h3 class="subtitle">
      Question or problems? Please, check the following FAQs, or <br />
      <router-link to="/contacts">Contact Us</router-link>
      .
    </h3>
  </div>
  <div class="container p-1">
    <div class="col-12 wrapper">
      <h4>1. What is EVs?</h4>
      <div>
        <p class="pt-4">
          EVs is a webapp developed using Django and Vue.js for the Human
          Computer Interaction course final exam at University of Florence,
          Italy. The idea behind this app is to create a social network for
          event management. The goal is to make users confident about the events
          they participate to.
        </p>
      </div>
    </div>
    <div class="col-12 wrapper">
      <h4>2. How does EVs work?</h4>
      <div>
        <p class="pt-4">
          EVs has for macro areas: an
          <router-link to="/home">Homepage</router-link>
          , where are listed all the most interesting, the most participated and
          the expiring events; an
          <router-link to="/events">Events</router-link> page, where users are
          to filter events by city, date and categories; a detailed event page,
          where is possible to retrieve more detailed information about an
          event; and finally an User profile page, where an user can see all its
          events and an organizer can managed the events created by himself.
        </p>
      </div>
    </div>
    <div class="col-12 wrapper">
      <h4>3. Is Evs safe and secure?</h4>
      <div>
        <p class="pt-4">
          EVs is hosted on Heroku. Please, read
          <a href="https://www.heroku.com/policy/security">
            Heroku Security statement</a
          >
          to know more. Profile images are stored on AWS S3, which is secure and
          safe. safe. All data shared by users are not used for profiling
          activities.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.title {
  font-style: normal;
  font-weight: 400;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  color: #1f6dad;
}

.subtitle {
  font-weight: 100;
  font-size: 36px;
  line-height: 42px;
  text-align: center;
  color: #575757;
  margin-top: 20px;
}

.wrapper {
  margin-top: 40px;
  background: #ffffff;
  box-sizing: border-box;
}

h4 {
  font-style: normal;
  font-weight: 500;
  font-size: 36px;
  line-height: 42px;
  color: #2c98f0;
}

p {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #000000;
  margin-left: 45px;
}
</style>
