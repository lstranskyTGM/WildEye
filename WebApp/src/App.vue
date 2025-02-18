<template>
  <div class="vh-100 vw-100 overflow-hidden edge_color">
    <div class="row-cols-2 d-flex w-100 h-100" style="padding-top: 2%">
      <div class="col-xxl-1 col-xl-1 col-lg-1 col-md-2 col-sm-3 col-3 edge_color">
        <div class="d-flex h-100 w-100">
          <div class="row-cols-1 ms-auto me-auto h-100">
            <nav class="mt-0 h-100 w-100 align-content-start d-flex flex-column">
              <div class="col d-flex justify-content-center align-content-center " @click="this.setActiveRoute('/'); router().push('/')" role='button' >
                <img src="@/assets/LogoV4.png" class="card-img-top img-fluid" style="object-fit: contain; width: 70%;" alt="WildEye Logo">
              </div>
              <div class="overflow-y-auto h-100 flex-grow-1">
                <div class="col mt-3">
                  <router-link to="/" class="text-decoration-none text-reset text-center d-grid" @click="this.setActiveRoute('/')">
                    <md-elevated-button v-if="activeRoute === '/'" class="w-75 ms-auto me-auto"><i class="bi bi-kanban fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto" ><i class="bi bi-kanban fs-3"></i></md-text-button>
                    <p>Dashboard</p>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/picture" class="text-decoration-none text-reset text-center d-grid" @click="this.setActiveRoute('/picture')">
                    <md-elevated-button v-if="activeRoute === '/picture'" class="w-75 ms-auto me-auto"><i class="bi bi-images fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto" ><i class="bi bi-images fs-3"></i></md-text-button>
                    <p>Pictures</p>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/map" class="text-decoration-none text-reset text-center d-grid" @click="this.setActiveRoute('/map')">
                    <md-elevated-button v-if="activeRoute === '/map'" class="w-75 ms-auto me-auto"><i class="bi bi-map fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto" ><i class="bi bi-map fs-3"></i></md-text-button>
                    <p>Map</p>
                  </router-link>
                </div>
                <div class="col mt-3">
                  <router-link to="/account" class="text-decoration-none text-reset text-center d-grid"  @click="this.setActiveRoute('/account')">
                    <md-elevated-button v-if="activeRoute === '/account'" class="w-75 ms-auto me-auto"><i class="bi bi-person-rolodex fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto"><i class="bi bi-person-rolodex fs-3"></i></md-text-button>
                    <p>Account</p>
                  </router-link>
                </div>
                <div class="col mt-3 ms-auto me-auto">
                  <div class=" text-center d-grid " @click="this.opened = !this.opened" >
                    <md-fab variant="primary" aria-label="Add new Camera" class="w-75 ms-auto mb-auto">
                      <md-icon slot="icon"><i class="bi bi-plus-circle-dotted"></i></md-icon>
                    </md-fab>
                    <p>Add Camera</p>
                  </div>
                  <md-dialog :open="this.opened" v-on:close="this.opened = false">
                    <div slot="headline">
                      Add new Camera to account
                    </div>
                    <form slot="content" id="form-id" method="dialog">
                      enter the code here or not ok thank you
                    </form>
                    <div slot="actions">
                      <md-text-button form="form-id" @click="this.opened = false">Ok</md-text-button>
                    </div>
                  </md-dialog>
                </div>
              </div>
            </nav>
          </div>
        </div>
      </div>
      <div class="col-11 ms-auto me-0 edge_color p-0" style="background-color: var(--md-sys-color-surface-container-high)">
        <div class="bg-white me-0 ms-0 pe-0 ps-0 w-100 h-100 rounded rounded-5" style="">
          <div class="px-3 h-100 w-100 rounded rounded-3" style="background-color: var(--md-sys-color-surface-container)">
            <router-view v-on:login="this.opened2 = true" v-on:logout="resetData" />
          </div>
          <md-dialog :open="this.opened2" v-on:close="this.opened2 = false">
            <div slot="headline">
              Login
            </div>
            <form slot="content" id="form-id" method="dialog">
              <md-outlined-text-field
                  type="text"
                  label="Username"
                  class="w-100 pb-3 pt-1"
                  v-model="input_username"
              >
              </md-outlined-text-field>
              <md-outlined-text-field
                  type="password"
                  label="Password"
                  class="w-100 pb-3 pt-1"
                  v-model="input_password"
              >
              </md-outlined-text-field>
            </form>
            <div slot="actions">
              <md-text-button form="form-id" @click="this.opened2 = false; completeLoginWithCameras(this.input_username, this.input_password)">Ok</md-text-button>
            </div>
          </md-dialog>
          <md-dialog :open="this.opened3" v-on:close="this.opened3 = false">
            <div slot="headline">
              Welcome to WildEye!
            </div>
            <form slot="content" id="form-id" method="dialog">
              You are not logged in, please log in or register to access the full functionality of WildEye.
              <md-outlined-text-field
                  type="text"
                  label="Username"
                  class="w-100 pb-3 pt-1"
                  v-model="input_username"
                  v-if="register"
              >
              </md-outlined-text-field>
              <md-outlined-text-field
                  type="email"
                  label="email"
                  class="w-100 pb-3 pt-1"
                  v-model="input_email"
              >
              </md-outlined-text-field>
              <md-outlined-text-field
                  type="password"
                  label="Password"
                  class="w-100 pb-3 pt-1"
                  v-model="input_password"
              >
              </md-outlined-text-field>

            </form>
            <div slot="actions">
              <md-text-button form="form-id" @click="this.register = !this.register" v-if="!register">New Here? Register</md-text-button>
              <md-text-button form="form-id" @click="this.register = !this.register" v-if="register">Log in instead</md-text-button>
              <md-text-button form="form-id" @click="this.completeLoginWithCameras(this.input_email, this.input_password)" v-if="!this.register">Continue</md-text-button>
              <md-text-button form="form-id" @click="this.registerWithCameras(this.input_email, this.input_password, this.input_username)" v-if="this.register">Register</md-text-button>
              <md-text-button form="form-id" @click="this.opened3 = false">Cancel</md-text-button>
            </div>
          </md-dialog>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Cookies from "js-cookie";
import "@material/web/all"
import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';
import router from "@/router";
import axios from "axios";
import {provide} from "vue";

// Add a request interceptor
axios.interceptors.request.use(function (config) {
  // Log the request to the console
  console.log('Request:', config);
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});

export default {
  name: 'App',
  data() {
    return {
      input_username: "",
      input_password: "",
      input_email: "",
      activeRoute: '/',
      opened: false,
      serverIP: "https://strapi.wildeye.tech",
      cameraObjects: [],
      session: Cookies.get('session') || "0", // Get session from cookie or default to "0"
      opened2: false,
      opened3: false,
      register: false
    }
  },
  provide() {
    return {
      serverIP: this.serverIP,
      cameraObjects: this.cameraObjects,
      session: this.session_computed
    };
  },
  methods: {
    router() {
      return router
    },
    setActiveRoute(route) {
      this.activeRoute = route;
    },
    getCameraObjectsFromAPI() {
      var that = this
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
    },
    login(email, password) {
      var that = this;
      console.log("Logging in with: "+email+" : "+password);
      return axios.post(this.serverIP + '/api/auth/local', {
        password: password,
        identifier: email
      }).catch(function (error) {
        console.log(error);
      }).then((response) => {
        console.log(response);
        if(response){
          if ( response.data.jwt !== false){
            // wenn es hwt ist, sonst session genannt
            this.session = response.data.jwt;
            Cookies.set('session', this.session); // Save session as a cookie
            axios.defaults.headers.common['Authorization'] = `Bearer ${this.session}`;
            console.log("Login complete, session: "+that.session);
            this.opened3 = false;
            return true
          }
          else{
            console.log("Login failed");
            alert("Login failed: "+response.data.error);
            return false
          }
        }
        else{
          return false;
        }

      });
    },
    completeLoginWithCameras(email, password){
      this.resetData();
      this.login(email, password).then((loginSuccess) => {
        if (loginSuccess) {
          this.getCameraObjectsFromAPI();
        }
      });
    },
    registerFunc(email, password, username){
      var that = this;
      console.log("Registering with: "+email+" : "+password + " : "+username);
      return axios.post(this.serverIP + '/api/auth/local/register',
          {
            username: username,
            email: email,
            password: password
          }
      ).catch(function (error) {
        console.log(error);
      }).then(function (response) {
        console.log(response);
        if(response){
          if (response.data.jwt){
            // wenn es hwt ist, sonst session genannt
            that.session = response.data.jwt;
            Cookies.set('session', that.session); // Save session as a cookie
            axios.defaults.headers.common['Authorization'] = `Bearer ${that.session}`;
            console.log("Register complete, session: "+that.session);
            that.opened3 = false;
          }
          else{
            console.log("Register failed");
            alert("Register failed: "+response.data.error);
          }
        }
      });
    },
    registerWithCameras(email, password, username){
      this.resetData();
      this.registerFunc(email, password, username).then((loginSuccess) => {
        if (loginSuccess) {
          this.getCameraObjectsFromAPI();
        }
      });
    },
    resetData(){
      this.cameraObjects.splice(0, this.cameraObjects.length);
      this.session = "0";
      Cookies.set('session', this.session); // Save session as a cookie
    }
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  },
  mounted() {
    // check if session is valid
    if (this.session!= "0"){
      // get confirmation from API, if false, reset session
      /*axios.post(this.serverIP + '/checkSession',
          {
            session: this.session
          }
      ).catch(function (error) {
        console.log("Error in checkSession")
        console.log(error);
      }).then( (response) => {
        console.log(response);
        if (response.data.authorized === false){
          this.session = "0";
          Cookies.set('session', this.session); // Save session as a cookie
          this.opened3 = true;
        }
        else{
          axios.defaults.headers.common['Authorization'] = `Bearer ${this.session}`;
          this.getCameraObjectsFromAPI();
        }
      });
      return;*/
    }
    if (this.session == "0"){
      this.opened3 = true;
    }

    else{
      axios.defaults.headers.common['Authorization'] = `Bearer ${this.session}`;
      this.getCameraObjectsFromAPI();
    }


  },
  computed: {
    session_computed() {
      return this.session
    }
  },
  watch: {
    session_computed: {
      handler: function (val) {
        console.log('session changed', val);
      },
      deep: true
    }
  }
}

</script>

<style>
@import "../css/treeGreen.css";
#app, html, body {
  font-family: Roboto, sans-serif;
  /*background-color: var(--md-sys-color-surface-container);*/
}
.edge_color{
  background-color: var(--md-sys-color-surface-container-high);
}

</style>