<template>
  <div class="col-12 col-md-6 col-lg-3 mb-4 d-flex flex-grow-1">
    <div class="card h-100 mh-100 w-100">
      <div class="card-img-top w-100 ">
        <img :src="`${publicPath}${entry.pic}`" :alt="entry.title" class="img-fluid" style="width: 80%; height: 80%" id="color-tint">
      </div>
      <div class="card-header">
        <h5 class="card-title">{{ entry.title }}</h5>
        <p class="card-subtitle"> {{entry.date}}</p>
      </div>
      <div class="card-body overflow-y-auto">
        <p class="card-text">{{ entry.desc }}</p>
      </div>
      <div class="card-footer">
        <div class="progress" role="progressbar" aria-label="Animated striped example" :aria-valuenow="entry.progress" aria-valuemin="0" aria-valuemax="100">
          <div class="progress-bar progress-bar-striped progress-bar-animated" id="prog"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MilestoneComponent',
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
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

#color-tint{
  transition: 0.5s;
}

#prog{
  width: v-bind('entry.progress');
}
</style>