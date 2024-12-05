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

            <hr class="mt-0 position-absolute" style="top: 30%; left: 1%; width: 98%">
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

      <h1>Camera Options</h1>
      <div class="card h-50 rounded rounded-3 container_color "  style="width: 45% ; background-color: var(--wildeye-container-primary); min-height: 300px">

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

export default{
  components: {SettingComponent},
  name: 'AccountView',
  data(){
    return{

    }
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  }
}
</script>

<style>

.container_color, .card{
  background-color: var(--wildeye-container-primary);
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: minmax(min-content, min-content);
  gap: 10px;
  height: 100%;
  grid-auto-flow: column;
  white-space: nowrap;
}

</style>