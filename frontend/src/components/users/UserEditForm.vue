<template>
  <form v-if="user.id" @submit.prevent="updateUser">
    <div class="form-group">
      <label for="username">Username</label>
      <input
        v-model.trim="username"
        type="text"
        class="form-control"
        id="username"
        placeholder="Email"
        required
      />
    </div>
    <div v-if="user.is_organizer" class="form-group">
      <label for="organization">Organization Name</label>
      <input
        v-model="organizationName"
        type="text"
        class="form-control"
        id="organization"
        placeholder="Organization name"
        required
      />
    </div>
    <div class="form-row">
      <div class="form-group col-md-6">
        <label for="name">Name</label>
        <input
          v-model="firstName"
          type="text"
          class="form-control"
          id="name"
          placeholder="Name"
          required
        />
      </div>
      <div class="form-group col-md-6">
        <label for="surname">Surname</label>
        <input
          v-model="lastName"
          type="text"
          class="form-control"
          id="surname"
          placeholder="Surname"
          required
        />
      </div>
    </div>
    <div class="row">
      <div class="form-group col-md-6">
        <label for="birthday">Birthday</label>
        <input
          v-model="birthday"
          type="date"
          class="form-control"
          id="birthday"
          required
        />
      </div>
      <div class="form-group col-md-6">
        <label for="city">City</label>
        <input
          v-model="city"
          type="text"
          class="form-control"
          id="city"
          placeholder="City"
          required
        />
      </div>
    </div>
    <div class="form-group">
      <label for="email">Email</label>
      <input
        v-model.trim="email"
        type="email"
        class="form-control"
        id="email"
        placeholder="Email"
        required
      />
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
  emits: ["update-user"],
  data() {
    return {
      username: this.user.username,
      organizationName: this.user.organization_name,
      firstName: this.user.first_name,
      lastName: this.user.last_name,
      birthday: this.user.birthday,
      city: this.user.city,
      email: this.user.email,
    };
  },
  methods: {
    updateUser() {
      let formData = new FormData();
      formData.append("first_name", this.firstName);
      formData.append("last_name", this.lastName);
      formData.append("organization_name", this.organizationName);
      formData.append("city", this.city);
      formData.append("birthday", this.birthday);
      formData.append("username", this.username);
      formData.append("email", this.email);

      this.$emit("update-user", formData);
    },
  },
};
</script>

<style scoped></style>
