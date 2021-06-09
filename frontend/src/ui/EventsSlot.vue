<template>
  <div class="mt-5 py-4" :class="background">
    <div class="p-3">
      <h2 class="slot-title">{{ title }}</h2>
    </div>
    <div class="row d-flex justify-content-around col-xl-12">
      <slot></slot>
    </div>
    <div class="d-flex justify-content-end px-4 mt-2 discover">
      <a href="www.google.com">Discover more...</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "EventsSlot",
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

.slot-title {
  font-style: normal;
  font-weight: 300;
  font-size: 36px;
  line-height: 42px;
  color: #575757;
}

a {
  text-decoration: none;
}

.discover {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #575757;
}
</style>
