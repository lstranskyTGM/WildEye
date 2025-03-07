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
                <div class="grid-item" v-for="(img, index) in images" :key="index">
                  <SinglePictureComponent
                      :id="img.id"
                      :url="img.original.url"
                      :alt="img.alternativeText"
                      :title="img.title"
                      :date="this.formatDate(img.createdAt)"
                      :hearted="img.hearted"
                      :tags="img.tags ? img.tags : []"
                      :cameraName="img.cameraName"
                      :AIurl="img.analyzed ? img.analyzed.url : img.original.url"
                      v-on:update_hearted="updateHearted"
                      :showAI="this.showAI">
                  </SinglePictureComponent>
                </div>
              </div>
              <div class="fab-container">
                <md-fab variant="primary" aria-label="left" v-on:click="this.page = Math.max(1, this.page-1); this.onCloseSettingsDialog(); console.log('page: '+ this.page)">
                  <md-icon slot="icon"><i class="bi bi-arrow-left-circle"></i></md-icon>
                </md-fab>
                <md-fab variant="primary" aria-label="right" v-on:click="this.page = Math.max(1, this.page+1); this.onCloseSettingsDialog();console.log('page: '+this.page)">
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
                  <AdvancedSettingsComponent v-for="setting in section.sectionSettings" :setting="setting" class="pb-3 pt-1"></AdvancedSettingsComponent>
                </div>
              </div>
            </form>
            <div slot="actions">
              <md-text-button form="form-id" @click="this.opened = false; ">Ok</md-text-button>
            </div>
          </md-dialog>
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

import settingsFile from "../assets/imageSearchSettings.json";

export default defineComponent({
  name: 'MaterialPictureView',
  inject: ['serverIP', "cameraObjects"],
  components: {
    AdvancedSettingsComponent,
    SinglePictureComponent
  },
  methods: {
    updateHearted(payload) {
      console.log('updateHearted', payload);
      const index = this.images.findIndex(img => img.id === payload.id);
      const documentId = this.images[index].documentId;
      console.log(documentId);
      axios.put(`${this.serverIP}/api/pictures/${documentId}`, {data:{hearted: payload.to}})
          .catch(
              err => console.error(err)
          )
          .then(res => {
            console.log(res);
          });
      this.images[index].hearted = payload.to;
      //sort images by hearted
      this.images.sort((a, b) => (a.hearted < b.hearted) ? 1 : -1)
    },
    openSettingsDialog(){
      this.opened = true;
      if(this.settings === null){
        this.getSettings();
      }
      console.log(this.settings)
    },
    getSettings(){
      console.log("get settings")
      this.settings = settingsFile;
      console.log("settings: ",this.settings)
      console.log("cameras: ",this.computedCameraObjects)
      if (!Array.isArray(this.computedCameraObjects)) {
        console.log("No cameras available")
        return;
      }
      const sectionIndex = this.settings.findIndex(s => s.sectionName === "Cameras");
      console.log("sectionIndex: ",sectionIndex)
      if (sectionIndex !== -1) {
        var newSection = [];
        this.computedCameraObjects.forEach(camera => {
          console.log("camera: ",camera)
          newSection.push({
            name: camera.name,
            value: true,
            type: "boolean",
            required: true
          });
        });
        console.log("newSectionSettings: ",newSection)
        this.settings[sectionIndex].sectionSettings = newSection;
        console.log("settings: ",this.settings)
      }
      /*if(this.session === null){
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
          });*/
    },

    onCloseSettingsDialog(){
      this.opened = false;
      var that = this;
      console.log("getting new images based on settings", this.settings)
      var url = this.serverIP+'/api/pictures?populate=*&sort='+
          this.settings[2].sectionSettings[2].value+':'+this.settings[2].sectionSettings[3].value+''+
          (this.settings[3].sectionSettings[0].value? '&filters[hearted]=true':'')+''+
          (this.settings[0].sectionSettings[0].value? '&filters[title]='+this.settings[0].sectionSettings[0].value:'')+''+
          ('&filters[createdAt][$gte]='+this.settings[2].sectionSettings[0].value)+''+
          ('&filters[createdAt][$lte]='+this.settings[2].sectionSettings[1].value)+''+
          (this.settings[3].sectionSettings[1].value? '&pagination[pageSize]='+this.settings[3].sectionSettings[1].value : '')+''+
          ('&pagination[page]='+this.page)
      for(let i=0; i<=this.settings[1].sectionSettings.length-1; i++){
        console.log("iterator",i)
        console.log("setting",this.settings[1].sectionSettings[i])
        const setting = this.settings[1].sectionSettings[i]
        if(setting.value){
          url += '&filters[$or]['+i+'][wild_camera][name][$eq]='+setting.name
        }
      }
      axios.get(
          url
      ).catch(function (error) {
        console.log(error);
      }).then(function (response) {
        console.log(response);
        if(response){
          // remove all images that have the original tag set to undefined
          var temp = []
          response.data.data.forEach((item) => {
            if (item.original !== null) {
              temp.push(item);
            }
          })
          console.log(temp)
          // clear images
          that.images = [];
          // set images
          that.images = temp
        }

      });
    },
    getImages(){
      var that = this
      console.log("get images from api : "+this.serverIP + " : " + this.session)
      axios.get(this.serverIP+'/api/pictures?populate=*&sort=hearted:desc'
      ).catch(function (error) {
        console.log(error);
      }).then(function (response) {
        console.log(response);
        if(response){
          // remove all images that have the original tag set to undefined
          var temp = []
          response.data.data.forEach((item) => {
            if (item.original !== null) {
              temp.push(item);
            }
          })
          console.log(temp)
          // clear images
          that.images = [];
          // set images
          that.images = temp
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
      page: 1,
      session: Cookies.get('session') || "0",
      showAI: false
    }
  },
  mounted(){
    if (this.session === "0") {
      console.log("No session to display images")
      return
    }
    this.getImages()
  },
  watch: {
    cameraObjects: {
      handler(newVal) {
        console.log("cameraObjects changed: ", newVal)
        if (newVal) {
          //this.getSettings();
          //this.getImages()
        }
      },
      immediate: true
    }
  },
  computed:{
    computedCameraObjects() {
      return this.cameraObjects;
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