<template>
  <div class="col-12 col-md-6 col-lg-3 mb-4 d-flex flex-grow-1">
    <div class="card h-100 shadow w-100 mh-100">
      <img :src="`${publicPath}${entry.pic}`" class="card-img-top" :alt="entry.name">
      <div class="card-body overflow-y-auto">
        <h5 class="card-title">{{ entry.name }}</h5>
        <p v-if="entry.extra != null" class="card-subtitle">{{entry.extra}}</p>
        <p class="card-text">{{ entry.c }}</p>
        <p class="card-text">{{ entry.topic }}</p>
      </div>
      <div class="card-footer">
        <small class="text-nowrap overflow-scroll">{{ entry.email }}</small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props:{
    entry: Object
  },
  data(){
    return{
      publicPath: process.env.BASE_URL
    }
  }
}
</script>

<style scoped>
.card-img-top {
  object-fit: cover;
  min-height: 200px;
  height: 33%;
}
</style>