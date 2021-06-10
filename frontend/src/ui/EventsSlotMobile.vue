<template>
  <div class="mt-5 py-4" :class="background">
    <div class="p-3">
      <h2 class="slot-title">{{ title }}</h2>
    </div>
    <div class="col">
      <div class="d-flex justify-content-center row">
        <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
          <div class="carousel-inner">

              <slot></slot>
          </div>
          <a
            class="carousel-control-prev"
            href="#carouselExampleControls"
            role="button"
            data-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            href="#carouselExampleControls"
            role="button"
            data-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      </div>
    </div>
    <div
        class="d-flex justify-content-end px-4 mt-2 discover"
    >
      <p>Discover more...</p>
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
  },

}
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
</style>