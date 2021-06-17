<template>
  <div class="mt-3">
    <router-view />
  </div>
</template>

<style>
.spinner {
  position: absolute;
  height: 100px;
  width: 100px;
  top: 50%;
  left: 50%;
  margin-left: -50px;
  margin-top: -50px;
  background-size: 100%;
}
</style>