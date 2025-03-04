<template>
  <div class="" style="width: 100%; height: 100%">
    <div class="row ps-3 py-3 h-100 w-100 overflow-scroll" style="max-height: 100%">
      <div class="card h-50 rounded rounded-3 mb-3 px-0 container_color w-100" style="  background-color: var(--wildeye-container-primary); min-height: 300px">
        <div class="h-100 position-relative" style="max-height: 100% !important; width: 100%;">
          <div class="card-header row m-0 w-100 border border-0 mx-0 px-0 d-inline-flex justify-content-between align-items-center" style="height: 30%;">
            <h1 class=" mt-auto mb-auto " style="width:fit-content">Account Overview</h1>
<!--            <i class="bi bi-check-all position-absolute top-0 text-end pe-3 pt-2 fs-3" ></i>
            <p class="position-absolute text-end pe-3 " style="top: 13%">Apply all changes</p>-->
<!--            <md-elevated-button class="me-2" style="max-width: fit-content; max-height: 50%">Apply changes</md-elevated-button>-->
            <div style="max-height: 50%; width: fit-content">
              <md-elevated-button @click="logout" class="mx-2" style="max-height: 50%; width: fit-content">
                Logout
                <svg slot="icon" viewBox="0 0 48 48"><path d="M9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h13.95v3H9v30h30V25.05h3V39q0 1.2-.9 2.1-.9.9-2.1.9Zm10.1-10.95L17 28.9 36.9 9H25.95V6H42v16.05h-3v-10.9Z"/></svg>
              </md-elevated-button>

              <md-elevated-button @click="$emit('login')" class="mx-2" style="max-height: 50%; width: fit-content">
                Switch Account
                <svg slot="icon" viewBox="0 0 48 48"><path d="M9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h13.95v3H9v30h30V25.05h3V39q0 1.2-.9 2.1-.9.9-2.1.9Zm10.1-10.95L17 28.9 36.9 9H25.95V6H42v16.05h-3v-10.9Z"/></svg>
              </md-elevated-button>
            </div>


            <hr class="mt-0 position-absolute" style="top: calc(30% - 0.75px); left: 1%; width: 98%">
          </div>
          <div class="card-body row m-0 p-0 pt-1" style="height: 70%; max-width: 100%">
            <div v-if="this.session!=='0'" class="dashboard-grid overflow-x-auto overflow-y-auto" style="height: 100%; max-width: 100%">
              <SettingComponent name="Username" :value="!accountData? `username`: accountData.username" icon="bi bi-person-vcard" confirm_needed="false" popup="true" style="width: max(25%, 200px); max-height: 100%"></SettingComponent>
              <SettingComponent name="E-Mail" :value="!accountData? `email`: accountData.email" icon="bi bi-envelope-at" confirm_needed="true" popup="true" style="width: max(25%, 200px); max-height: 100%"></SettingComponent>
              <SettingComponent name="Password" value="************" icon="bi bi-asterisk" confirm_needed="true" popup="true" style="width: max(25%, 200px); max-height: 100%"></SettingComponent>
              <DashboardInfoComponent name="Created" value="today" icon="bi bi-clock"></DashboardInfoComponent>

            </div>

          </div>
        </div>
      </div>

      <h1 class="px-0 mx-0">Camera Options</h1>
      <div class="w-100 d-flex overflow-x-scroll ps-0 ms-0 pe-5">
        <div class="mx-0 ps-0" v-for="cam in this.cameraComponentData" style="width: max(45%, 400px) ; min-height: 330px; max-height: 100%;">
          <div class="h-100 w-100 pe-4" style="">
            <CameraComponent :name="cam.name" :info="cam.info" :id="cam.id" :camera="cam" class="w-100"></CameraComponent>
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
import axios from "axios";
import router from "@/router";
import {ref} from "vue";
import Cookies from "js-cookie";
import {createRouter as $router} from "vue-router";
import {routes} from "vue-router/auto-routes";
import DashboardInfoComponent from "@/components/DashboardInfoComponent.vue";

export default{
  components: {DashboardInfoComponent, CameraComponent, SettingComponent},
  inject: ['cameraObjects', "serverIP"],
  name: 'AccountView',
  data(){
    return{
      cameraComponentData: this.cameraObjects,
      session: Cookies.get('session'), // Access session from cookie
      accountData: null
    }
  },
  methods: {
    logout() {
      console.log("logout");
      if (this.session === "0") {
        console.log("No session to logout");
        return;
      }
      Cookies.set('session', '0');
      this.session = '0';
      this.$router.push({name: 'dashboard'});
      location.reload();
    },
    getAccountData(){
      if (this.session == "0") {
        console.log("No session available");
        return;
      }
      axios.get(this.serverIP + '/api/users/me')
          .then(response => {
            if (response) {
              console.log(response.data);
              this.accountData = response.data;
            }
          })
          .catch(error => {
            console.log(error);
          });
    }
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  },
  mounted() {
    console.log("Account View mounted");
    // get account data
    this.getAccountData();
  },
  computed: {

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