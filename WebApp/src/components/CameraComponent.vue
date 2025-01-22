<template>
  <div class="card h-100 rounded rounded-3 px-0 container_color w-100" style="min-width: 400px">
    <div class="h-100 position-relative" style="max-height: 100% !important; width: 100%;">
      <div class="card-header row m-0 border border-0 mx-0 px-0 d-inline-flex justify-content-between align-items-center w-100" style="height: 30%;">
        <h2 class="card-title mt-auto mb-auto " style="width:fit-content">{{ name }}</h2>
        <!--            <i class="bi bi-check-all position-absolute top-0 text-end pe-3 pt-2 fs-3" ></i>
                    <p class="position-absolute text-end pe-3 " style="top: 13%">Apply all changes</p>-->
<!--        <div class="d-flex position-absolute top-0 end-0 pe-3 pt-2" style="right: 0;">-->
<!--          <md-fab variant="primary" aria-label="apply" class="fs-3 ms-auto mt-auto mb-auto">-->
<!--            <md-icon slot="icon"><i class="bi bi-check-all"></i></md-icon>-->
<!--          </md-fab>-->
<!--        </div>-->
        <md-elevated-button @click="openSettingsDialog" class="mx-2" style="max-height: 50%; width: fit-content">
          Settings
          <svg slot="icon" viewBox="0 0 48 48"><path d="M9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h13.95v3H9v30h30V25.05h3V39q0 1.2-.9 2.1-.9.9-2.1.9Zm10.1-10.95L17 28.9 36.9 9H25.95V6H42v16.05h-3v-10.9Z"/></svg>
        </md-elevated-button>
        <hr class="mt-0 position-absolute" style="top: calc(30% - 0.75px); left: 1%; width: 98%">
      </div>
      <div class="card-body row m-0 p-0 pt-2" style="height: 70%; max-width: 100%">
<!--        <div class="w-50 h-100 border border-top-0 border-bottom-0 border-start-0 border-end-3" style="min-width: 150px">-->
<!--&lt;!&ndash;          <SettingComponent name="Name" :value="name" confirm_needed="false" icon="bi bi-camera"></SettingComponent>&ndash;&gt;-->

<!--        </div>-->
        <div class="w-100 h-100" style="min-width: 150px;">
          <md-outlined-text-field
              type="textarea"
              label="General Information"
              readonly="true"
              class="w-100 h-100 py-2 px-1"
              :value="info"
            style="resize: none"
          >
          </md-outlined-text-field>
        </div>
      </div>
    </div>
  </div>
  <md-dialog :open="this.opened" v-on:close="this.onCloseSettingsDialog" style="min-height: 50px; background-color: white; ">
    <div slot="headline">
      Settings for {{this.name}}
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
      <md-text-button form="form-id" @click="this.opened = false">Ok</md-text-button>
    </div>
  </md-dialog>
</template>

<script>

  import SettingComponent from "@/components/SettingComponent.vue";
  import "@material/web/all"
  import AdvancedSettingsComponent from "@/components/AdvancedSettingsComponent.vue";
  import axios from "axios";
  import Cookies from "js-cookie";

  export default {
    inject: ['serverIP'],
    name: 'CameraComponent',
    components: {AdvancedSettingsComponent, SettingComponent},
    data(){
      return{
        text:"kjdfghlskdjfgh",
        opened:false,
        settings:null,
        session: Cookies.get('session')
      }
    },
    props: {
      name: String,
      info: String,
      id: Number
    },
    methods: {
      openSettingsDialog(){
        this.opened = true;
        if(this.settings === null){
          this.getSettings();
        }
        console.log(this.settings)
      },
      getSettings(){
        // eventually, make a request to the server to get the advanced settings.
        axios.post(this.serverIP+'/advancedSettings', {session: this.session, id: this.id})
            .then(response => {
              this.settings = response.data;
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
      }
    }
  }
</script>

<style scoped>
hr{
  color: var(--md-sys-color-scrim) !important;
  border-width: 1.5px;
  background-color: var(--md-sys-color-scrim) !important;
  opacity: 0.5;
  border-radius: 5px;
}

.container_color, .card {
  background-color: var(--md-sys-color-secondary-container) !important;
}
</style>