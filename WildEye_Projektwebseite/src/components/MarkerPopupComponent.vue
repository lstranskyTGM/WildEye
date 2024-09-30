<template>
<div class="w-100 h-100">
  <div class="card shadow">
    <div class="card-body">
      <div class="row">
        <div class="col-12 row">
          <div class="col-6">
            <img :src="camera.lastCapturePreview" alt="lastCapturePreview" class="img-fluid rounded-2 shadow">
          </div>
          <div class="col-6">
            <h1>{{camera.name}}</h1>
            <h3>{{camera.description}}</h3>
          </div>
        </div>
        <div class="col-12 row">
          <div class="col-6">
            <p>Anzahl Aufnahmen: {{camera.totalCaptures}}</p>
            <p>Lat: {{camera.lat}}</p>
            <p>Lng: {{camera.lng}}</p>
          </div>
          <div class="col-6">
            <p>Anzahl Spezies: {{camera.totalSpecies}}</p>
            <button class="btn btn-primary" @click="launchPictureView(camera.id)">Zu den Bildern</button>
          </div>
        </div>
      </div>
    </div>
<!--    <div class="card-img-top h-50">
      <img :src="cameraPosition.lastCapturePreview" alt="Preview of the last Capture" class="w-50">
    </div>
    <div class="card-body">
      <div class="row-cols-2">
        <div class="col">
          <div class="row-cols-2">
            <div class="col">
              <p>{{cameraPosition.name}}</p>
            </div>
            <div class="col">
              <p>{{cameraPosition.description}}</p>
            </div>
          </div>
          <div class="row-cols-2">
            <div class="col">
              <p>{{cameraPosition.totalCaptures}}</p>
            </div>
            <div class="col">
              <p>{{cameraPosition.totalSpecies}}</p>
            </div>
          </div>
        </div>
        <div class="col-3">
          <button class="btn btn-primary">Zu den Bildern</button>
        </div>
      </div>
    </div>-->
  </div>
</div>
</template>

<script>
export default {
  name: 'MarkerPopupComponent',
  props: {
    camera: {
      type: Object,
      required: true
    }
  },
  components: {
  },
  setup() {
  },
  data() {
    return {
      name: 'MarkerPopupComponent',
    }
  },
  methods: {
    launchPictureView(id){
      console.log("launching pictureVire for camera with id: "+id);
      this.$router.push({name: 'pictures', query: {id: id}});
    }
  },
  computed: {
  },
  watch: {
  },
  mounted() {
  },
  beforeDestroy() {
  },
  destroyed() {
  }
}
</script>

<style scoped>

</style>