<template>
  <div class="" style="width: 100%; height: 100%">
    <div class="row ps-3 pb-3 h-100 w-100 overflow-scroll" style="max-height: 100%">
      <div class="card h-50 rounded rounded-3 mb-3 px-0 container_color w-100" style="  background-color: var(--wildeye-container-primary); min-height: 300px">
        <div class="h-100 position-relative" style="max-height: 100% !important; width: 100%;">
          <div class="card-header row m-0 border border-0 mx-0 px-0 d-felx" style="height: 30%;">
            <h1 class="card-title mt-auto mb-auto">Account Overview</h1>
<!--            <i class="bi bi-check-all position-absolute top-0 text-end pe-3 pt-2 fs-3" ></i>
            <p class="position-absolute text-end pe-3 " style="top: 13%">Apply all changes</p>-->
            <div class="d-flex position-absolute top-0 end-0 pe-3 pt-2" style="right: 0;">
              <md-fab variant="primary" aria-label="apply" class="fs-3 ms-auto mt-auto mb-auto">
                <md-icon slot="icon"><i class="bi bi-check-all"></i></md-icon>
              </md-fab>
            </div>

            <hr class="mt-0 position-absolute" style="top: calc(30% - 0.75px); left: 1%; width: 98%">
          </div>
          <div class="card-body row m-0 p-0 pt-1" style="height: 70%; max-width: 100%">
            <div class="dashboard-grid overflow-x-auto overflow-y-auto" style="height: 100%; max-width: 100%">
              <SettingComponent name="Username" value="WildEyeFan1" icon="bi bi-person-vcard" confirm_needed="false" style="width: max(25%, 200px); max-height: 100%"></SettingComponent>
              <SettingComponent name="E-Mail" value="Wil*****@gmail.com" icon="bi bi-envelope-at" confirm_needed="true" style="width: max(25%, 200px); max-height: 100%"></SettingComponent>
              <SettingComponent name="Password" value="WildEyeFan1" icon="bi bi-person-vcard" confirm_needed="true" style="width: max(25%, 200px); max-height: 100%"></SettingComponent>
            </div>
          </div>
        </div>
      </div>

      <h1 class="px-0 mx-0">Camera Options</h1>
      <div class="w-100 d-flex overflow-x-scroll ps-0 ms-0 pe-5">
        <div class="mx-0 ps-0" v-for="cam in this.cameraComponentData" style="width: 45% ; min-height: 330px; max-height: 100%;min-width: 45%">
          <div class="pe-4 h-100">
            <CameraComponent :name="cam.name" :info="cam.info"></CameraComponent>
          </div>
        </div>
      </div>

    </div>
    <div>

    </div>
  </div>
</template>

<script>

import "@material/web/all"
import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';
import SettingComponent from "@/components/SettingComponent.vue";
import CameraComponent from "@/components/CameraComponent.vue";

export default{
  components: {CameraComponent, SettingComponent},
  name: 'AccountView',
  data(){
    return{
      cameraComponentData:[
        {
          name: "Wildkamera 1",
          info: "This is a test camera. MP: 12, Battery: 100%, SD-Card: 32GB, Nightvision: True, 20m"
        },
        {
          name: "Wildkamera 2",
          info: "This is a test camera. MP: 12, Battery: 100%, SD-Card: 32GB, Nightvision: True, 20m"
        },
        {
          name: "Wildkamera 3",
          info: "This is a test camera. MP: 12, Battery: 100%, SD-Card: 32GB, Nightvision: True, 20m"
        }
      ]
    }
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  }
}
</script>

<style scoped>
.container_color, .card {
  background-color: var(--wildeye-container-primary);
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: minmax(min-content, min-content);
  gap: 10px;
  height: 100%;
  grid-auto-flow: row; /* Change this to row */
  white-space: nowrap;
}
hr{
  color: var(--md-sys-color-scrim) !important;
  border-width: 1.5px;
  background-color: var(--md-sys-color-scrim) !important;
  opacity: 0.5;
  border-radius: 5px;
}
</style>