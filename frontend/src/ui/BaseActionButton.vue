<template>
  <button
    class="button"
    :class="{
      'primary-btn': isPrimary && !userGoing,
      'like-btn': isLike && !userInterested,
      'is-going-btn': userGoing && isPrimary,
      'is-interested-btn': userInterested && isLike,
    }"
  >
    <div class="row justify-content-around">
      <div class="mt-2">
        {{ buttonLabel }}
      </div>
      <div>
        <i class="material-icons">{{ icon }}</i>
      </div>
    </div>
  </button>
</template>

<script>
export default {
  name: "BaseActionButton",
  props: ["label", "icon", "userGoing", "userInterested"],
  computed: {
    buttonLabel() {
      if (this.label === "Going") {
        if (!this.userGoing) {
          return this.label;
        } else {
          return "Ungoing";
        }
      } else if (this.label === "Like") {
        if (!this.userInterested) {
          return this.label;
        } else {
          return "Unlike";
        }
      }
      return this.label;
    },
    isPrimary() {
      return this.label === "Going" || this.label === "Edit";
    },
    isLike() {
      return this.label === "Like";
    },
  },
};
</script>

<style scoped>
.button {
  background: #ffffff;
  border: 0.5px solid #1f6dad;
  box-sizing: border-box;
  border-radius: 30px;
  width: 150px;
  height: 40px;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  line-height: 16px;
  outline: none;
  cursor: pointer;
}

.primary-btn {
  color: #2c98f0;
}

.like-btn {
  color: #e32822;
}

.is-going-btn {
  color: white;
  background-color: #2c98f0;
}
.is-interested-btn {
  color: white;
  background-color: #e32822;
}

.is-interested-btn:hover {
  background: white;
  color: #e32822;
}

.is-going-btn:hover {
  background: white;
  color: #2c98f0;
}

.like-btn:hover {
  background: #e32822;
  color: white;
}

.primary-btn:hover {
  background: #2c98f0;
  color: white;
}
</style>
