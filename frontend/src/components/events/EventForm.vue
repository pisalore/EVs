<template>
  <div class="form-div">
    <div class="p-4">
      <h1 class="title">1. Add ev’s main information.</h1>
      <h2 class="subtitle">
        Provide an evocative name and information you think are useful for
        potential partecipants. For example: age range, restrictions, how to get
        ev location, services...
      </h2>
      <div class="form-group">
        <label for="evName">Event name</label>
        <input
          type="text"
          class="form-control"
          id="evName"
          placeholder="Event name..."
        />
      </div>
      <div class="form-group">
        <label for="evDescription">Ev description</label>
        <textarea
          class="form-control"
          id="evDescription"
          rows="5"
          placeholder="Description here..."
        ></textarea>
      </div>
    </div>
  </div>
  <div class="form-div mt-5">
    <div class="p-4">
      <h1 class="title">2. Add ev’s venue and date.</h1>
      <h2 class="subtitle">
        Provide the venue for your Ev and fill date and hour field.
      </h2>
      <div class="form-group">
        <label for="evVenue">Event venue</label>
        <input
          type="text"
          class="form-control"
          id="evVenue"
          placeholder="Event venue..."
        />
      </div>
      <div class="col-xl-12">
        <div class="row my-2">
          <div class="col-xl-4 mt-2"><span>Start date and hour</span></div>
          <div class="col-xl-8">
            <input
              class="form-control"
              type="datetime-local"
              value="2011-08-19T13:45:00"
              id="startDate"
            />
          </div>
        </div>
        <div class="row my-2">
          <div class="col-xl-4 mt-2"><span>Finish date and hour</span></div>
          <div class="col-xl-8">
            <input
              class="form-control"
              type="datetime-local"
              value="2011-08-19T13:45:00"
              id="endDate"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EventForm",
};
</script>

<style scoped>
.form-div {
  background: #fbfbfb;
  border: 1px solid #f0f2f5;
  box-sizing: border-box;
  border-radius: 30px;
}
.title {
  font-style: normal;
  font-weight: normal;
  font-size: 36px;
  line-height: 42px;
  color: #575757;
}
.subtitle {
  font-style: normal;
  font-weight: 300;
  font-size: 24px;
  line-height: 28px;
  color: #575757;
}
</style>
