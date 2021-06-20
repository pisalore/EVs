<template>
  <div class="col-xl-12">
    <h1 class="title">Edit your account info</h1>
    Your city will make us able to suggest events near you.
    <hr />
    <user-edit-form v-if="user.id" :user="user"></user-edit-form>
  </div>
  <div class="mt-5 col-xl-12">
    <hr />
    <h1 class="title">Delete your account</h1>
    <p>This action is not reversible. You will lost all your saved EVs.</p>
    <div class="d-flex justify-content-center">
      <button type="button" class="btn btn-lg btn-danger">
        Delete Account
      </button>
    </div>
  </div>
</template>

<script>
import UserEditForm from "./UserEditForm";
export default {
  name: "ProfileOverviewEdit",
  components: { UserEditForm },
  props: ["user"],

};
</script>

<style scoped>
.title {
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  color: #1f6dad;
}
p {
  font-weight: bold;
}
</style>
