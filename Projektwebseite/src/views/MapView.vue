<template>
  <div class="h-100 card col-xxl-12 col-xl-11 col-lg-11 col-md-11 col-sm-12 col-12">
    <div class="card-img-top" style="height: 80vh;">
      <l-map ref="map" class="l-map" v-model:zoom="zoom" :center="[48.31561796122741, 16.58404319905392]" :on-ready="addPOI" @click="addMarker">
        <l-tile-layer
            :url="tiles[currentTileName]"
            layer-type="base"
            name="OpenStreetMap"

        ></l-tile-layer>
        <div v-for="camera in this.cameraPositions">
          <l-marker :lat-lng="latLng(camera.lat, camera.lng)">
            <l-popup :options="popupOptions" class="custom-popup">
              <marker-popup-component :camera="camera"></marker-popup-component>
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
    <div class="card-footer">
      <div class="row">
        <div class="col-2">
          <div class="input-group mb-3" >
            <span class="input-group-text" id="basic-addon1">Zoom</span>
            <input type="number" class="form-control" placeholder="16" aria-label="Zoom" aria-describedby="basic-addon1" v-model="zoom">
          </div>
        </div>
        <div class="dropup-center dropup col-xxl-2 col-xl-2 col-lg-2 col-md-3 col-sm-12 me-4">
          <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            {{currentTileName}}
          </button>
          <ul class="dropdown-menu">
            <li v-for="(url, name) in tiles" :key="name">
              <a class="dropdown-item" @click="selectTile(name)">{{name}}</a>
            </li>
          </ul>
        </div>
        <div class="col-3 form-check-inline">
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1" v-model="POI">
            <label class="form-check-label" for="inlineCheckbox1">Notizen anzeigen</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2" v-model="this.POIsBearbeiten">
            <label class="form-check-label" for="inlineCheckbox2">Notizen Bearbeiten</label>
          </div>
        </div>

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
// import L from "leaflet";
// import "leaflet.heat";
export default {
  name: 'MapView',
  components: {
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
      map: null,
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
      cameraPositions:[
        {
          lat: 48.31561796122741,
          lng: 16.58404319905392,
          type:[
            'camera',
            'thermal'
          ],
          name: 'Camera 1',
          id: 1,
          description: 'This is a camera 1',
          lastCapturePreview: 'https://dummyimage.com/600x400/000/4e5285&text=temp',
          totalCaptures: 10,
          totalSpecies: 5,
        },
        {
          lat: 48.31661796122741,
          lng: 16.58204319905392,
          type:[
            'camera',
          ],
          name: 'Camera 2',
          id: 2,
          description: 'This is a camera 2',
          lastCapturePreview: 'https://dummyimage.com/600x400/000/4e5285&text=temp',
          totalCaptures: 20,
          totalSpecies: 2,
        }
      ],
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
    this.$nextTick(() => {
      console.log(this.$refs.map)
      console.log(this.$refs.map.mapObject)
      this.map = this.$refs.map
    })
    console.log(this.map)
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