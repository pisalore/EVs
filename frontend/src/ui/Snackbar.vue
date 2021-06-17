<template>
  <div class="d-flex justify-content-center">
    <div id="snackbar" :style="{ backgroundColor: color }">
      <div class="text-center mt-2">
        <i v-if="!is_error" class="fa fa-check fa-5x" aria-hidden="true"></i>
        <i v-else class="fa fa-times fa-5x" aria-hidden="true"></i>
        <span>{{ message }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["close"],
  props: ["is_error", "color", "message"],
  name: "Snackbar",
  mounted() {
    var that = this;
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function () {
      x.className = x.className.replace("show", "");
      that.$emit("close");
    }, 3000);
  },
};
</script>

<style scoped>
#snackbar {
  visibility: hidden; /* Hidden by default. Visible on click */
  min-width: 350px;
  min-height: 60px; /* Set a default minimum width */
  color: white; /* White text color */
  text-align: center; /* Centered text */
  border-radius: 10px; /* Rounded borders */
  position: fixed; /* Sit on top of the screen */
  z-index: 1; /* Add a z-index if needed */
  bottom: 30px; /* 30px from the bottom */
}

/* Show the snackbar when clicking on a button (class added with JavaScript) */
#snackbar.show {
  visibility: visible; /* Show the snackbar */
  -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

/* Animations to fade the snackbar in and out */
@-webkit-keyframes fadein {
  from {
    bottom: 0;
    opacity: 0;
  }
  to {
    bottom: 30px;
    opacity: 1;
  }
}

@keyframes fadein {
  from {
    bottom: 0;
    opacity: 0;
  }
  to {
    bottom: 30px;
    opacity: 1;
  }
}

@-webkit-keyframes fadeout {
  from {
    bottom: 30px;
    opacity: 1;
  }
  to {
    bottom: 0;
    opacity: 0;
  }
}

@keyframes fadeout {
  from {
    bottom: 30px;
    opacity: 1;
  }
  to {
    bottom: 0;
    opacity: 0;
  }
}
</style>
