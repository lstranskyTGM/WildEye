<template>
  <div class="card h-25 rounded rounded-3" style="width: 97%">
    <div class="row g-0 h-100 container_color rounded rounded-3" style="min-height: 100%">
      <div class="container_color rounded rounded-3" style="min-height: 100%; width: 23%; height: 25%">
        <l-map ref="map" class="l-map rounded rounded-3 container_color" v-model:zoom="zoom" :center="[camera.lat, camera.lng]" :options="mapOptions">
          <l-tile-layer
              :url="'https://tile.openstreetmap.org/{z}/{x}/{y}.png'"
              layer-type="base"
              name="OpenStreetMap"
              class="container_color"
          ></l-tile-layer>
          <l-marker :lat-lng="latLng(camera.lat, camera.lng)"></l-marker>
        </l-map>
      </div>
      <div class="h-100 position-relative" style="max-height: 100% !important; width: 77%;">
        <div class="card-header row m-0 mx-0 px-0 border border-0 d-flex align-items-center justify-content-between" style="height: 30%;">
          <h1 class="card-title">{{ this.camera.name }}</h1>
          <div class="position-absolute top-0 text-end pe-3 pt-3 fs-3">
            <i :class="{'bi bi-heart-fill text-danger pe-1': camera.hearted, 'bi bi-heart pe-1': !camera.hearted}" @click="toggleHeart"></i>
            <i class="bi bi-pencil-square " @click="$emit('navigateToSettings')"></i>
          </div>
          <hr class="mt-0 position-absolute" style="top: calc(30% - 0.75px); left: 2%; width: 96%">
        </div>
        <div class="card-body row overflow-hidden" style="height: 70%">
          <div class="dashboard-grid " style="height: 100%">
            <DashboardInfoComponent name="position" value="121212" icon="bi bi-pin-map" ></DashboardInfoComponent>
            <DashboardInfoComponent name="Battery" value="86%" icon="bi bi-battery-half"></DashboardInfoComponent>
            <DashboardInfoComponent name="Last Synchronization" value="01.12.2024 09:31" icon="bi bi-cloud-upload"></DashboardInfoComponent>
            <DashboardInfoComponent name="Last Activity" value="13.12.2024, 07:36" icon="bi bi-clock"></DashboardInfoComponent>
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
import DashboardInfoComponent from "@/components/DashboardInfoComponent.vue";
import router from "@/router";

export default {
  name: 'DashboardMaterialComponent',
  props: {
    camera:Object
  },
  methods: {
    router() {
      return router
    },
    latLng,
    toggleHeart() {
      console.log('toggleHeart', this.camera.id);
      this.$emit('update_hearted', {to: !this.camera.hearted, id: this.camera.id});
    }
  },
  components: {
    DashboardInfoComponent,
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
  },

}
</script>

<style scoped>

html, body, #app, DashboardInfoComponent {
  font-family: Roboto, sans-serif;

}

.card{
  background-color: var(--wildeye-container-primary);
}

hr{
  color: var(--md-sys-color-scrim) !important;
  border-width: 1.5px;
  background-color: var(--md-sys-color-scrim) !important;
  opacity: 0.5;
}

.container_color{
  background-color: var(--wildeye-container-primary);
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: minmax(min-content, min-content);
  gap: 10px;
  grid-auto-flow: unset ;
  border-radius: 5px;
}

.text-danger {
  color: red;
}
.icon-container {
  display: flex;
  gap: 10px; /* Adjust the gap as needed */
  position: relative;
  z-index: 10; /* Ensure the icons are on top */
  width: min-content;
}

.icon-container i {
  cursor: pointer;
}
</style>