<template>
  <div class="chip mx-2 my-2" :class="categoryStyle">
    <div class="row justify-content-around">
      <div v-if="category">
        {{ category.category }}
      </div>
      <div v-else>
        {{ content }}
      </div>
      <div
        v-if="type !== 'badge'"
        class="material-icons"
        style="margin-top: 9px"
        @click="close"
      >
        close
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["close-chip"],
  props: ["category", "categoryStyle", "type", "content"],
  methods: {
    close() {
      this.$emit("close-chip", this.category);
    },
  },
};
</script>

<style scoped>
.chip {
  display: inline-block;
  padding: 0 25px;
  line-height: 40px;
  text-align: center;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 18px;
}

.material-icons {
  cursor: pointer;
}

.music {
  background: #ffcad0;
  border: 1px solid #fa4a43;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 22px;
  color: #fa4a43;
  width: 150px;
}

.sport {
  background: #ffe8c6;
  border: 1px solid #ffbb33;
  color: #8c5d00;
  width: 150px;
}

.art {
  background: #d1d9ff;
  border: 1px solid #1f6dad;
  color: #1f6dad;
  width: 150px;
}

.food {
  background: #9aeb94;
  border: 1px solid #13572f;
  color: #575757;
  width: 150px;
}

.other {
  background: #d6d6d6;
  border: 1px solid #575757;
  color: #575757;
  width: 150px;
}
.base-mobile {
  border: 0.5px solid #1f6dad;
  color: #1f6dad;
  font-weight: 500;
  max-width: 90px;
}
.base {
  border: 0.5px solid #1f6dad;
  color: #1f6dad;
  font-weight: 500;
  width: 200px;
}
.available {
  color: #3db834;
  font-weight: 500;
}
.scheduled {
  color: #ffbb33;
  font-weight: 500;
}
.canceled {
  color: #e32822;
  font-weight: 500;
}
</style>
