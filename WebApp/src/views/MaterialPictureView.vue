<template>
  <div class=" col-xxl-12 col-xl-12 col-lg-12 col-md-11 col-sm-10 col-10" style="height: 100%; width: 100%">
    <div class="ps-2 py-3 w-100 h-100">
      <div class="card h-100 w-100 shadow-sm rounded-3">
        <div class="card-body overflow-y-auto rounded rounded-3 card_background" style="height: 93%">
          <div class="row">
            <div class="col-12">
<!--              <p v-if="session === '0'">Log in to display Images for your account. {{session}}</p>-->
              <p v-if="images.length===0">No Images to display.</p>
              <div class="grid">
                <div class="grid-item " v-for="(img, index) in images" :key="index">
                  <SinglePictureComponent :id="img.id" :url="img.original.url" :alt="img.alternativeText" :title="img.titel" :date="this.formatDate(img.createdAt)" :hearted="img.hearted" :tags="img.tags" :cameraName="img.cameraName" :AIurl="img.analyzed.url"  v-on:update_hearted="updateHearted" :showAI="this.showAI"></SinglePictureComponent>
                </div>
              </div>
              <div class="fab-container">
                <md-fab variant="primary" aria-label="left" v-on:click="this.page = Math.max(0, this.page-1); this.getImages(); console.log('page-1 '+ this.page)">
                  <md-icon slot="icon"><i class="bi bi-arrow-left-circle"></i></md-icon>
                </md-fab>
                <md-fab variant="primary" aria-label="right" v-on:click="this.page = Math.max(0, this.page+1); this.getImages();console.log('page+1+ '+this.page)">
                  <md-icon slot="icon"><i class="bi bi-arrow-right-circle"></i></md-icon>
                </md-fab>
              </div>
            </div>

          </div>

        </div>
        <div class="card-footer border border-0 d-flex justify-content-between m-2 overflow-x-auto text-nowrap" style="min-height: 50px; background-color: white; ">
          <p class="fs-2 text-center justify-content-start p-0 m-0">Page: {{this.page}}</p>
          <div>
            <label class="pe-2 pt-2">
              Show AI analysis
              <md-switch :checked="this.showAI" @click="this.showAI = !this.showAI"></md-switch>

            </label>

            <md-elevated-button @click="openSettingsDialog">
              Settings (Popup)
              <i class="bi bi-search" slot="icon"></i>
            </md-elevated-button>
          </div>


          <md-dialog :open="this.opened" v-on:close="this.onCloseSettingsDialog" class="" style="min-width: 40%; max-height: 80%">
            <div slot="headline">
              Image search settings
            </div>
            <form slot="content" id="form-id" method="dialog">
              <div v-if="this.settings==null">
                Please note that content might need some time to load
                <br>
                <md-circular-progress four-color indeterminate ></md-circular-progress>
              </div>
              <div v-else>
                <div v-for="section in this.settings">
                  <p class="fs-2">{{section.sectionName}}</p>
                  <md-divider></md-divider>
                  <AdvancedSettingsComponent v-for="setting in section.sectionSettings" :setting="setting" @update-setting="updateSetting" class="pb-3 pt-1"></AdvancedSettingsComponent>
                </div>
              </div>
            </form>
            <div slot="actions">
              <md-text-button form="form-id" @click="this.opened = false; ">Ok</md-text-button>
              <md-text-button form="form-id" @click="getSettings">Reset</md-text-button>
            </div>
          </md-dialog>
<!--          <div>
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
          </div>-->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "@material/web/all"
import {defineComponent} from "vue";
import SinglePictureComponent from "@/components/SinglePictureComponent.vue";
import AdvancedSettingsComponent from "@/components/AdvancedSettingsComponent.vue";
import axios from "axios";
import Cookies from "js-cookie";
export default defineComponent({
  name: 'MaterialPictureView',
  inject: ['serverIP'],
  components: {
    AdvancedSettingsComponent,
    SinglePictureComponent
  },
  methods: {
    updateHearted(payload) {
      console.log('updateHearted', payload);
      const index = this.images.findIndex(img => img.id === payload.id);
      this.images[index].hearted = payload.to;
    },
    openSettingsDialog(){
      this.opened = true;
      if(this.settings === null){
        this.getSettings();
      }
      console.log(this.settings)
    },
    getSettings(){
      if(this.session === null){
        console.log("No session available")
        return;
      }
      // eventually, make a request to the server to get the advanced settings.
      axios.post(this.serverIP+'/imageSearchSettings', {session: this.session, id: this.name})
          .then(response => {
            if(response){
              this.settings = response.data;

            }
          })
          .catch(error => {
            console.log(error);
          });
    },
    updateSetting(updatedSetting) {
      const setting = this.settings.find(s => s.name === updatedSetting.name);
      if (setting) {
        setting.value = updatedSetting.value;
      }
    },

    onCloseSettingsDialog(){
      this.opened = false;
      console.log(this.settings)
      // when connected to the server, send the updated settings to the server.
      // The changes are already in the settings object.
    },
    getImages(){

      /*
      * var that = this
      console.log("get cameras from api : "+this.serverIP + " : " + this.session)
      // provide('session', this.session);
      // get camera objects from API
      axios.get(this.serverIP + '/api/wild-cameras'
      ).catch(function (error) {
        console.log(error);
      }).then(function (response) {
        console.log(response);
        that.cameraObjects.push(...response.data.data);
      });
      * */

      var that = this
      console.log("get images from api : "+this.serverIP + " : " + this.session)
      axios.get(this.serverIP+'/api/wild-cameras?populate[pictures][populate]=*'
      ).catch(function (error) {
        console.log(error);
      }).then(function (response) {
        console.log(response);
        if(response){
          // clear images
          that.images = [];
          const cameras = response.data.data
          // each entry has an array `images`, add that to the images array
          cameras.forEach(camera => {
            that.images.push(...camera.pictures);
          });

        }

      });
    },
    formatDate(date){
      return new Date(date).toLocaleDateString();
    }
  },
  data(){
    return{
      opened: false,
      settings: null,
      searchValue: "",
      startDate: "",
      endDate: "",
      images: [],
      page: 0,
      session: Cookies.get('session') || "0",
      showAI: false
    }
  },
  mounted(){
    if (this.session === "0") {
      console.log("No session to display images")
      return
    }
    this.getSettings();
    this.getImages();
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