<template>
  <form>
    <div class="form-row">
      <div class="form-group col-md-6">
        <label for="name">Name</label>
        <input type="text" class="form-control" id="name" placeholder="Name" />
      </div>
      <div class="form-group col-md-6">
        <label for="surname">Surname</label>
        <input
          type="text"
          class="form-control"
          id="surname"
          placeholder="Surname"
        />
      </div>
    </div>
    <div class="row">
      <div class="form-group col-md-6">
        <label for="birthday">Birthday</label>
        <input type="date" class="form-control" id="birthday" />
      </div>
      <div class="form-group col-md-6">
        <label for="city">City</label>
        <input type="text" class="form-control" id="city" placeholder="City" />
      </div>
    </div>
    <div class="form-group">
      <label for="email">Email</label>
      <input type="email" class="form-control" id="email" placeholder="Email" />
    </div>
    <div class="d-flex justify-content-center mt-4">
      <button type="submit" class="btn btn-lg btn-primary">
        Update Profile
      </button>
    </div>
  </form>
</template>

<script>
export default {
  name: "UserEditForm",
  props: ["user"],
};
</script>

<style scoped></style>
