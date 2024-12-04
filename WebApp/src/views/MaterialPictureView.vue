<template>
  <div class="" style="height: 100%; width: 100%">
    <div class="card h-100 w-100 shadow-sm">
      <div class="card-body overflow-y-auto rounded rounded-3 card_background" style="height: 93%">
        <div class="row">
          <div class="col-12">
            <div class="grid">
              <div class="grid-item " v-for="(img, index) in images" :key="index">
                <SinglePictureComponent :id="img.id" :url="img.url" :alt="img.alt" :title="img.title" :date="img.date" :hearted="img.hearted" :tags="img.tags" v-on:update_hearted="updateHearted"></SinglePictureComponent>
              </div>
            </div>
            <div class="fab-container">
              <md-fab variant="primary" aria-label="left">
                <md-icon slot="icon"><i class="bi bi-arrow-left-circle"></i></md-icon>
              </md-fab>
              <md-fab variant="primary" aria-label="right">
                <md-icon slot="icon"><i class="bi bi-arrow-right-circle"></i></md-icon>
              </md-fab>
            </div>
          </div>

        </div>

      </div>
      <div class="card-footer border border-0 d-flex justify-content-between m-2 overflow-x-auto text-nowrap" style="min-height: 50px; background-color: white; ">
        <div class=" pe-3" style="min-width: max(25%, 100px)">
          <md-filled-text-field label="Search for" value="" v-model="searchValue">
          </md-filled-text-field>
        </div>
        <div>
          <md-outlined-select class="pe-3" label="Specify Camera">
            <md-select-option aria-label="All Cameras" value="all" selected>All Cameras</md-select-option>
            <md-select-option v-for="camera in cameras" :key="camera.value" :value="camera.value">{{camera.headline}}</md-select-option>
          </md-outlined-select>

          <md-outlined-select class="pe-3" label="Sort By">
            <md-select-option aria-label="DESC" value="desc" selected>Descending</md-select-option>
            <md-select-option aria-label="ACS" value="acs" >Ascending</md-select-option>
          </md-outlined-select>

          <md-outlined-text-field label="Start Date" type="date" v-model="startDate" class="pe-3"></md-outlined-text-field>
          <md-outlined-text-field label="End Date" type="date" v-model="endDate"></md-outlined-text-field>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {defineComponent} from "vue";
import SinglePictureComponent from "@/components/SinglePictureComponent.vue";

export default defineComponent({
  name: 'MaterialPictureView',
  components: {
    SinglePictureComponent
  },
  methods: {
    updateHearted(payload) {
      console.log('updateHearted', payload);
      const index = this.images.findIndex(img => img.id === payload.id);
      this.images[index].hearted = payload.to;
    }
  },
  data(){
    return{
      searchValue: "",
      startDate: "",
      endDate: "",
      cameras:[
        {value: "camera1", headline: "Camera 1"},
        {value: "camera2", headline: "Camera 2"},
        {value: "camera3", headline: "Camera 3"},
        {value: "camera4", headline: "Camera 4"},
      ],
      images: [
        {
          id: 0,
          url: "https://www.w3schools.com/w3images/lights.jpg",
          alt: "Lights",
          title: "Lights",
          date: "2021-09-01",
          hearted: false,
          tags: [
            {icon: "bi bi-person", text: "Person"},
            {icon: "bi bi-camera", text: "Camera"}
          ]
        },
        {
          id: 1,
          url: "https://www.w3schools.com/w3images/lights.jpg",
          alt: "Lights",
          title: "Lights",
          date: "2021-09-01",
          hearted: false,
          tags: [
            {icon: "bi bi-person", text: "Person"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"}

          ]
        },
        {
          id: 2,
          url: "https://www.w3schools.com/w3images/lights.jpg",
          alt: "Lights",
          title: "Lights",
          date: "2021-09-01",
          hearted: false,
          tags: [
            {icon: "bi bi-person", text: "Person"},
            {icon: "bi bi-camera", text: "Camera"}
          ]
        },
        {
          id: 3,
          url: "https://www.w3schools.com/w3images/lights.jpg",
          alt: "Lights",
          title: "Lights",
          date: "2021-09-01",
          hearted: false,
          tags: [
            {icon: "bi bi-person", text: "Person"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"},
            {icon: "bi bi-camera", text: "Camera"}

          ]
        },

      ]
    }
  }
})
</script>

<style>
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.grid-item {
  break-inside: avoid;
  margin-bottom: 1rem;
}

.card_background {
  background-color: var(--wildeye-container-primary);
}
.fab-container {
  position: absolute;
  bottom: min(19%, 130px);
  right: 16px;
  display: flex;
  gap: 8px; /* Adjust the gap between FABs as needed */
}
</style>