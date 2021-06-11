<template>
  <div class="mt-5 py-4" :class="background">
    <div class="p-3">
      <h2 class="slot-title">{{ title }}</h2>
    </div>
    <div class="col">
      <div class="d-flex justify-content-center row">
        <slot></slot>
      </div>
    </div>
    <div
      class="d-flex justify-content-end px-4 mt-2 discover"
      @click="loadNextEvents"
    >
      <p>Discover more...</p>
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
  methods: {
    async loadNextEvents() {
      await this.$store.dispatch("events/loadNextEvents", {
        endpoint: this.next,
        type: this.nextType,
      });
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

p {
  text-decoration: none;
}

p:hover {
  color: #2c98f0;
  cursor: pointer;
}

.discover {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
}
</style>
