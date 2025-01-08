<template>
  <div class="vh-100 vw-100 overflow-hidden edge_color">
    <div class="row-cols-2 d-flex w-100 h-100" style="padding-top: 2%">
      <div class="col-xxl-1 col-xl-1 col-lg-1 col-md-2 col-sm-3 col-3 edge_color">
        <div class="d-flex h-100 w-100">
          <div class="row-cols-1 ms-auto me-auto h-100">
            <nav class="mt-0 h-100 w-100 align-content-start d-flex flex-column">
              <div class="col d-flex justify-content-center align-content-center " @click="this.setActiveRoute('/'); router().push('/')" role='button' >
                <img src="@/assets/logo_digital.png" class="card-img-top img-fluid" style="object-fit: contain; width: 70%;">
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
            <router-view/>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

import "@material/web/all"
import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';
import router from "@/router";
export default {
  name: 'App',
  data(){
    return{
      activeRoute: '/',
      opened:false
    }
  },
  methods: {
    router() {
      return router
    },
    setActiveRoute(route){
      this.activeRoute = route;
    }
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
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