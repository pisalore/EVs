<template>
  <div class="p-5">
    <h1 class="title">Something bad happened...<br />Error 404</h1>
    <h1 class="subtitle mt-5">
      Please,
      <router-link to="/contacts" class="link">Contact Us</router-link> for any
      request <br />
      or come back <router-link to="/" class="link">home</router-link>
    </h1>
    .
  </div>
</template>

<script>
export default {
  name: "NotFound",
  created() {
    const body = document.getElementById("mainContent");
    body.classList.add("not-found");
  },
  unmounted() {
    const body = document.getElementById("mainContent");
    body.classList.remove("not-found");
  },
};
</script>

<style>
.not-found {
  background: #2c98f0;
}

.title {
  top: 150px;
  font-style: normal;
  font-weight: 500;
  font-size: 48px;
  line-height: 56px;
  color: #ffffff;
}

.subtitle {
  top: 527px;
  font-style: normal;
  font-weight: 200;
  font-size: 48px;
  line-height: 56px;

  color: #ffffff;
}

.link {
  font-weight: 500;
  color: #ffffff;
}
</style>
