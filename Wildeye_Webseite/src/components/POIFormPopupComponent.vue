<template>
  <div class="w-100 h-100">
    <div class="card shadow">
      <div class="card-body">
        <div class="row">
          <div class="col-12">
            <h1>Neuen POI hinzufügen:</h1>
          </div>
          <div class="col-12">
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">Name</span>
              <input type="text" class="form-control" placeholder="POI1" aria-label="POI1" aria-describedby="basic-addon1" v-model="name2">
            </div>
            <div class="input-group">
              <span class="input-group-text">Beschreibung</span>
              <textarea class="form-control" aria-label="desc" v-model="desc"></textarea>
            </div>
            <div class="d-flex w-100 align-items-center align-content-around">
              <p>{{cords}}</p>
<!--              <p class="me-auto">{{Number((cords.lat).toFixed(5))}}, {{Number((cords.lng).toFixed(5))}}</p>-->
              <button class="btn btn-primary ms-auto" @click="$emit('savePOI', {name: name2, desc: this.desc, cords: cords})">Speichern</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {LatLng} from "leaflet/src/geo";

export default {
  props:{
    cords: {
      type: Object,
      required: true
    }
  },
  name: 'POIFormPopupComponent',
  components: {
  },
  setup() {
  },
  data() {
    return {
      name: 'POIFormPopupComponent',
      name2: '',
      desc: ''
    }
  },
  methods: {
  },
  computed: {
  },
  watch: {
  },
  mounted() {
  },
  beforeDestroy() {
  },
}
</script>

<style scoped>

</style>