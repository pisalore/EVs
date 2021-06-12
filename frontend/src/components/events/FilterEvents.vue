<template>
  <div class="p-4">
    <form>
      <div class="container-fluid">
        <div class="row justify-content-around">
          <div class="col-xl-2 mt-4">
            <span class="title">Filter by:</span>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <input type="text" class="form-control" id="inlineFormInputGroup" placeholder="Enter a city...">
            </div>
          </div>
          <div class="input-group-lg col-xl-3 my-3">
            <select id="inputState" class="form-control">
              <option selected>Categories...</option>
              <option>...</option>
            </select>
          </div>
          <div class="col-xl-3 my-3">
            <div class="input-group-lg">
              <input class="form-control" type="date" id="example-date-input1">
            </div>
            <div class="input-group-lg my-3">
              <input class="form-control" type="date" id="example-date-input2">
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "FilterEvents",
};
</script>

<style scoped>
.title {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;

  color: #000000;
}
</style>
