<template>
  <a
    v-if="showArrow"
    @click="scrollToTop()"
    id="myBtn"
    title="Go to top"
    class="top-arrow"
    ><i class="material-icons" style="font-size: 28px; color: #1e347b"
      >arrow_upward</i
    ></a
  >
</template>

<script>
export default {
  name: "ScrollToTopArrow",
  data() {
    return {
      showArrow: false,
    };
  },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    showArrowToTop() {
      if (!this.isMobile) {
        this.showArrow = window.scrollY > 200;
      } else {
        this.showArrow = window.scrollY > 400;
      }
    },
  },
  created() {
    window.addEventListener("scroll", this.showArrowToTop);
  },
  unmounted() {
    window.removeEventListener("scroll", this.showArrowToTop);
  },
};
</script>

<style scoped>
.top-arrow {
  display: block;
  position: fixed;
  bottom: 160px;
  cursor: pointer;
  z-index: 99;
  right: 30px;
}
</style>