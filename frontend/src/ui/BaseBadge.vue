<template>
  <div class="chip" :class="categoryStyle">
    <div class="row justify-content-around">
      <div>
        {{ category }}
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
      this.$emit("close-chip", this.category);
    },
  },
  mounted() {
    console.log(this.categoryStyle)
  }
};
</script>

<style scoped>
.chip {
  display: inline-block;
  padding: 0 25px;
  font-size: 16px;
  line-height: 50px;
  border-radius: 25px;
  text-align: center;
  width: 200px;
}

.music {
  background: #ffcad0;
  border: 1px solid #fa4a43;
  box-sizing: border-box;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 14px;
  line-height: 16px;
  color: #fa4a43;
}

.sport {
  background: #ffe8c6;
  border: 1px solid #ffbb33;
  box-sizing: border-box;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 14px;
  line-height: 16px;
  color: #8c5d00;
}

.art {
  background: #d1d9ff;
  border: 1px solid #1f6dad;
  box-sizing: border-box;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 14px;
  line-height: 16px;
  color: #1f6dad;
}

.food {
  background: #9aeb94;
  border: 1px solid #13572f;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 22px;
  color: #13572f;
}

.other {
  background: #d6d6d6;
  border: 1px solid #13572f;
  box-sizing: border-box;
  border-radius: 40px;
  font-style: normal;
  font-weight: 300;
  font-size: 14px;
  line-height: 16px;
  color: #575757;
}
</style>
