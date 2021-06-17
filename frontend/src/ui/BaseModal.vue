<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="container modal-container">
          <div class="modal-header title">
            <slot name="header"> {{ title }} </slot>
          </div>

          <div class="modal-body message m-4">
            <slot name="body"> {{ message }} </slot>
          </div>

          <div class="col-xl-12">
            <slot name="footer">
              <div class="d-flex justify-content-around">
                <div class="col-xl-4">
                  <button
                    class="btn btn-outline-secondary col text-center"
                    @click="$emit('cancel-modal')"
                  >
                    Cancel
                  </button>
                </div>
                <div class="col-xl-4">
                  <button
                    class="btn col text-center"
                    :class="{
                      'btn-primary': action === 'confirm',
                      'btn-danger': action === 'delete',
                    }"
                    @click="$emit('confirm-modal')"
                  >
                    Confirm
                  </button>
                </div>
              </div>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "BaseModal",
  props: ["action", "title", "message", "confirm", "cancel"],
  created() {
    console.log(this.title)
  }
};

</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.title {
  font-style: normal;
  font-weight: normal;
  font-size: 28px;
  line-height: 42px;
  text-align: center;
  color: #1f6dad;
}

.message {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 42px;
  text-align: center;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
