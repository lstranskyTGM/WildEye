<template>
  <div class="w-100 h-100 ps-2 py-3">
    <div class="h-100 card col-xxl-12 col-xl-12 col-lg-12 col-md-11 col-sm-12 col-12 rounded-3">
      <div class="card-img-top" style="height: 80vh;">
        <l-map ref="map" class="l-map rounded rounded-3" v-model:zoom="zoom" :center="this.centerStart" :on-ready="addPOI" @click="addMarker">
          <l-tile-layer
              :url="tiles[currentTileName]"
              layer-type="base"
              name="OpenStreetMap"

          ></l-tile-layer>
          <div v-for="camera in this.cameraPositions">
            <l-marker :lat-lng="latLng(camera.lat, camera.lng)">
              <l-popup :options="popupOptions" class="custom-popup ratio ratio-16x9">
                <MarkerPopupMaterialComponent :camera="camera" v-on:update_hearted="updateHearted"></MarkerPopupMaterialComponent>
              </l-popup>
            </l-marker>
          </div>
          <div >
            <l-marker ref="marker" :lat-lng="marker" :options="markerOptions">
              <l-icon :icon-size= [1,1] icon-url="icon.png"> </l-icon>
              <l-popup ref="popup" :options="POIPopupOptions">
                <POIFormPopupComponent v-on:savePOI="addPOI" :cords="this.latestCords"></POIFormPopupComponent>
              </l-popup>
            </l-marker>
          </div>
          <div v-for="i in this.POIs" v-show="notizen">
            <l-circle-marker :lat-lng="latLng(i.lat, i.lng)" :radius="10" >
              <!--Also add a Popup for each custom POI-->
            </l-circle-marker>
          </div>
        </l-map>
      </div>
      <div class="card-footer border border-0 d-flex justify-content-end m-2 overflow-x-auto text-nowrap" style="min-height: 50px; background-color: white; ">
        <md-outlined-text-field label="Zoom" type="Number" value="17" v-model="zoom" class="pe-3">
        </md-outlined-text-field>
        <md-outlined-select class="pe-3" label="Choose Map">
          <md-select-option value="Default" @click="selectTile('OpenStreetMap')" selected>Default</md-select-option>
          <md-select-option v-for="(url, name) in tiles" :key="url" :value="name" @click="selectTile(name)">{{name}}</md-select-option>
        </md-outlined-select>
      </div>
    </div>
  </div>



</template>

<script>
import {LCircleMarker, LIcon, LMap, LMarker, LPopup, LTileLayer} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import {latLng, LatLng} from "leaflet/src/geo";
import MarkerPopupComponent from "@/components/MarkerPopupComponent.vue";
import POIFormPopupComponent from "@/components/POIFormPopupComponent.vue";
import MarkerPopupMaterialComponent from "@/components/MarkerPopupMaterialComponent.vue";
// import L from "leaflet";
// import "leaflet.heat";
export default {
  name: 'MapView',
  inject: ['cameraObjects'],
  components: {
    MarkerPopupMaterialComponent,
    POIFormPopupComponent,
    LIcon,
    LCircleMarker,
    MarkerPopupComponent,
    LMarker,
    LPopup,
    LMap,
    LTileLayer
  },
  setup() {
  },
  data() {
    return {
      name: 'MapView',
      cameraPositions: this.cameraObjects,
      map: null,
      centerStart: [48.4262157636489, 16.61251026756385],
      marker: [0,0],
      markerOptions: {opacity: 0, width:"1px", height:"1px"},
      zoom: 17,
      POI: true,
      POIsBearbeiten: false,
      latestCords: [0,0],
      currentTile: "OpenStreetMap",
      tiles: {
        "OpenStreetMap": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        "CyclOSM":"https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png",
        "Transport": "https://tile.memomaps.de/tilegen/{z}/{x}/{y}.png"
      },
      // Hier kann man noch viele andere Daten hinzufügen, wie zb der Akkustand, das letzte Update, usw...
      /*cameraPositions:[
        {
          lat: 48.4262157636489,
          lng: 16.61251026756385,
          name: 'Camera 1',
          id: 1,
          description: 'This is a camera 1',
          lastCapturePreview: 'https://www.w3schools.com/w3images/lights.jpg',
          hearted: false,
          date: "2021-09-01",
          tags: [
            {icon: "bi bi-person", text: "Person"},
            {icon: "bi bi-camera", text: "Camera"}
          ]
        },
        {
          lat: 48.42558212563766,
          lng: 16.61130863793849,
          type:[
            'camera',
          ],
          name: 'Camera 2',
          id: 2,
          description: 'This is a camera 2',
          lastCapturePreview: 'https://www.w3schools.com/w3images/lights.jpg',
          totalCaptures: 20,
          totalSpecies: 2,
          date: "2021-09-01",
          hearted: false,
          tags: [
            {icon: "bi bi-person", text: "Person"},
            {icon: "bi bi-camera", text: "Camera"}
          ]
        }
      ],*/
      mapOptions:{
        doubleClickZoom: false
      },
      popupOptions:{
        maxWidth: 900,
        minWidth: 300,
        maxHeight: 1000000,
        closeButton: false
      },
      POIPopupOptions:{
        maxWidth: 900,
        minWidth: 300,
        maxHeight: 1000000,
        closeButton: true
      },
      POIs:[
        /*{
          lat: 48.31461796122741,
          lng: 16.58204319905392,
          title: 'Interest 1',
          desc: 'This is an interest point'
        }*/
      ]
      /*heatmapData: [
        [48.31561796122741, 16.58404319905392, 0.5], // [latitude, longitude, intensity]

      ]*/
    }
  },
  methods: {
    latLng,
    selectTile(name) {
      this.currentTile = name;
    },
    // This adds an invisible marker to the map used to display a popup.
    // The popup contains a form to add a POI to the map.
    addMarker(e) {
      if(this.POIsBearbeiten){
        // set marker at latlng position
        this.marker = e.latlng;
        console.log(this.marker)
        this.latestCords = e.latlng;

        // open popup on marker with a delay of 100 ms
        setTimeout(() =>
            this.$refs.marker.leafletObject.openPopup(), 100);
      }

    },
    addPOI(POI){
      // hopefully i can solve it like this:
      // Problem: I want to be able to add POIs to the map by double-clicking on the map.
      // How: Open a Popup with a form to add a POI to the map.
      console.log(POI)
      this.POIs.push({
        lat: POI.cords.lat,
        lng: POI.cords.lng,
        title: POI.name,
        desc: POI.desc
      });
      console.log(this.POIs)
    },
    updateHearted(payload) {
      console.log('updateHearted', payload);
      const index = this.cameraPositions.findIndex(img => img.id === payload.id);
      this.cameraPositions[index].hearted = payload.to;
    }
    /*onMapReady() {
      this.addHeatmapLayer();
    },
    addHeatmapLayer() {
      const map = this.$refs.map.mapObject;
      L.heatLayer(this.heatmapData, { radius: 25 }).addTo(map);
    }*/
  },

  computed: {
    currentTileName() {
      return this.currentTile;
    }
  },
  watch: {
  },
  mounted() {
    // load data from server, if not already loaded. if loaded, save data to a json file.
    // so that the data can be loaded faster next time the user visits the page.
    // sometimes the data is not loaded from the server. also add intervall to reload the data every minute.
    // Also add refresh button to reload the data from the server again.
    // when loaded, set the center of the map so that all cameras are visible.

    // here is just placeholder until i can get the data from the server:

    this.$nextTick(() => {
      console.log(this.$refs.map)
      console.log(this.$refs.map.mapObject)
      this.map = this.$refs.map
    })
    console.log(this.map)
    // this.centerStart = [41.31661796122741, 16.59404319905392]
  },
  beforeDestroy() {
  },
  destroyed() {
  }
}

</script>

<style scoped>
@media (min-width: 576px) {
  .custom-popup {
    width: 80vw;
    height: auto;
  }
}

@media (min-width: 768px) {
  .custom-popup {
    width: 60vw;
    height: auto;
  }
}

@media (min-width: 992px) {
  .custom-popup {
    width: 45vw;
    height: auto;
  }
}

@media (min-width: 1200px) {
  .custom-popup {
    width: 30vw;
    height: auto;
  }
}

@media (min-width: 1400px) {
  .custom-popup {
    width: 25vw;
    height: auto;
  }
}

</style>