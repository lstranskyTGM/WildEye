<template>
  <div class="card h-25">
    <div class="row g-0 h-100" style="min-height: 100%">
      <div class="col-md-4 border-end border-3 " style="min-height: 100%">
        <l-map ref="map" class="l-map" v-model:zoom="zoom" :center="[48.31561796122741, 16.58404319905392]">
          <l-tile-layer
              :url="'https://tile.openstreetmap.org/{z}/{x}/{y}.png'"
              layer-type="base"
              name="OpenStreetMap"
          ></l-tile-layer>
          <l-marker :lat-lng="latLng(lat, lng)"></l-marker>
        </l-map>
      </div>
      <div class="col-md-8 h-100">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
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
          notes: 'Notes über ie Wildkamera'
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
      zoom: 17
    }
  }
}
</script>

<style>

</style>