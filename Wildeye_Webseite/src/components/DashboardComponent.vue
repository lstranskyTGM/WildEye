<template>
  <div class="card h-25" style="width: 97%">
    <div class="row g-0 h-100" style="min-height: 100%">
      <div class="col-md-4 border-end border-3 " style="min-height: 100%">
        <l-map ref="map" class="l-map" v-model:zoom="zoom" :center="[48.31561796122741, 16.58404319905392]" :options="mapOptions">
          <l-tile-layer
              :url="'https://tile.openstreetmap.org/{z}/{x}/{y}.png'"
              layer-type="base"
              name="OpenStreetMap"
          ></l-tile-layer>
          <l-marker :lat-lng="latLng(lat, lng)"></l-marker>
        </l-map>
      </div>
      <div class="col-md-8 h-100 position-relative" style="max-height: 100% !important;">
        <div class="card-header row m-0" style="height: 30%;">
          <h1 class="card-title">{{ this.camera.name }}</h1>
          <p class="card-subtitle"> {{ this.camera.id }}</p>
          <i class="bi bi-pencil-square position-absolute top-0 text-end pe-5 pt-3 fs-3" v-on:click="$emit('edit', this.camera.id)"></i>
        </div>
        <div class="card-body row overflow-y-auto" style="max-height: 70%">
          <div class="ms-auto me-auto row col-12 list-group-grid overflow-y-auto" style="max-height: 100%">
            <ul class="list-group list-group-horizontal   mb-2">
              <li class="list-group-item flex-fill">An item</li>
              <li class="list-group-item flex-fill">A second item</li>
            </ul>
            <ul class="list-group list-group-horizontal  mb-2">
              <li class="list-group-item flex-fill">An item</li>
              <li class="list-group-item flex-fill">A second item</li>
            </ul>
            <ul class="list-group list-group-horizontal  mb-2">
              <li class="list-group-item flex-fill">An item</li>
              <li class="list-group-item flex-fill">A second item</li>
            </ul>
            <ul class="list-group list-group-horizontal  mb-2">
              <li class="list-group-item flex-fill">An item</li>
              <li class="list-group-item flex-fill">A second item</li>
            </ul>
            <ul class="list-group list-group-horizontal  mb-2">
              <li class="list-group-item flex-fill">An item</li>
              <li class="list-group-item flex-fill">A second item</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import POIFormPopupComponent from "@/components/POIFormPopupComponent.vue";
import MarkerPopupComponent from "@/components/MarkerPopupComponent.vue";
import {LCircleMarker, LIcon, LMap, LMarker, LPopup, LTileLayer} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import {latLng, LatLng} from "leaflet/src/geo";

export default {
  /*
  * camera object looks like this:
  * {
          name: "Wildkamera 3",
          id: 'dfjk43kb92022',
          battery: 100,
          signal: 100,
          lastPicture: 'https://www.wildeye.de/wp-content/uploads/2021/08/IMG_20210806_123456.jpg',
          lastPictureDate: '2021-08-06 12:34:56',
          numPictures: 9,
          lastSync: '2021-08-06 12:34:56',
          lat: 48.31561796122741,
          lng: 16.58404319905392,
        }
  */

  name: 'DashboardComponent',
  props: {
    camera:Object
  },
  methods: {latLng},
  components: {
    MarkerPopupComponent,
    POIFormPopupComponent,
    LIcon,
    LCircleMarker,
    LMarker,
    LPopup,
    LMap,
    LTileLayer
  },
  data() {
    return {
      map: null,
      lat: 48.31561796122741,
      lng: 16.58404319905392,
      zoom: 17,
      mapOptions: {
        zoomControl: false,
        boxZoom: false,
        doubleClickZoom: false,
        dragging: false,
        keyboard: false,
        scrollWheelZoom: false,
        touchZoom: false,
      }
    }
  }
}
</script>

<style>
.list-group-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
}
</style>