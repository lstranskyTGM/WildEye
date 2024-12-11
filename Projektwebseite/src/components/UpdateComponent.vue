<template>
  <div class="card m-3 shadow">
    <div class="card-img-top img-fluid d-flex ">
      <img :src="image" :alt="alt" class="ms-auto me-auto mw-100 mh-100 rounded rounded-3">
    </div>
    <div class="card-header">
      <div>
        <p class="fs-5">{{title}}</p>
      </div>
    </div>
  </div>
</template>

<script >
export default {
  props:{
    image: String,
    alt: String,
    title: String,
  }
}
</script>

<style scoped>

</style>