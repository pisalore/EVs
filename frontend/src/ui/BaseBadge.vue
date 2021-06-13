<template>
  <div class="chip mx-2 my-2" :class="categoryStyle">
    <div class="row justify-content-around">
      <div>
        {{ category.category }}
      </div>
      <div class="material-icons" style="margin-top: 11px" @click="close">
        close
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["close-chip"],
  props: ["category", "categoryStyle"],
  methods: {
    close() {
      console.log(this.category)
      this.$emit("close-chip", this.category);
    },
  },
};
</script>

<style scoped>
.chip {
  display: inline-block;
  padding: 0 25px;
  line-height: 50px;
  text-align: center;
  width: 150px;
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
}

.sport {
  background: #ffe8c6;
  border: 1px solid #ffbb33;
  color: #8c5d00;
}

.art {
  background: #d1d9ff;
  border: 1px solid #1f6dad;
  color: #1f6dad;
}

.food {
  background: #9aeb94;
  border: 1px solid #13572f;
  color: #575757;
}

.other {
  background: #d6d6d6;
  border: 1px solid #575757;
  color: #575757;
}
</style>
