<template>
  <div class="vh-100 vw-100 overflow-hidden edge_color">
    <div class="row-cols-2 d-flex w-100 h-100" style="padding-top: 2%">
      <div class="col-xxl-1 col-xl-1 col-lg-1 col-md-2 col-sm-3 col-3 edge_color">
        <div class="d-flex h-100 w-100">
          <div class="row-cols-1 ms-auto me-auto h-100">
            <nav class="mt-0 h-100 w-100 align-content-start d-flex flex-column">
              <div class="col d-flex justify-content-center align-content-center">
                <img src="@/assets/LogoV4.png" class="card-img-top img-fluid" style="object-fit: contain; width: 70%;" alt="WildEye Logo" @click="router.push('/'); setActiveRoute('/')">
              </div>
              <div class="overflow-y-auto h-100 flex-grow-1">
                <div class="col mt-3">
                  <router-link to="/" class="text-decoration-none text-reset text-center d-grid" @click="this.setActiveRoute('/')">
                    <md-elevated-button v-if="activeRoute === '/'" class="w-75 ms-auto me-auto"><i class="bi bi-kanban fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto" ><i class="bi bi-kanban fs-3"></i></md-text-button>
                    <p>Team</p>
                  </router-link>
                </div>

                <div class="col mt-3">
                  <router-link to="/about" class="text-decoration-none text-reset text-center d-grid" @click="this.setActiveRoute('/about')">
                    <md-elevated-button v-if="activeRoute === '/about'" class="w-75 ms-auto me-auto"><i class="bi bi-map fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto" ><i class="bi bi-map fs-3"></i></md-text-button>
                    <p>Updates</p>
                  </router-link>
                </div>

                <div class="col mt-3">
                  <router-link to="/picture" class="text-decoration-none text-reset text-center d-grid" @click="this.setActiveRoute('/picture')">
                    <md-elevated-button v-if="activeRoute === '/picture'" class="w-75 ms-auto me-auto"><i class="bi bi-card-checklist icon fs-3"></i></md-elevated-button>
                    <md-text-button v-else class="w-75 ms-auto me-auto" ><i class="bi bi-card-checklist icons fs-3"></i></md-text-button>
                    <p>Meilensteine</p>
                  </router-link>
                </div>
              </div>

            </nav>

          </div>

        </div>
      </div>
      <div class="col-11 ms-auto me-0 edge_color pe-0 ps-0">
        <div class="w-100 h-100 rounded-top-5 rounded-end-0 bg-white me-0 ms-0 pe-0 ps-0">
          <div class="p-3 h-100 me-auto ms-auto" style="max-width: 97%;">
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
export default {
  name: 'App',
  data(){
    return{
      activeRoute: '/',
      router: this.$router
    }
  },
  methods: {
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
  background-color: var(--md-sys-color-surface-container);
}
.edge_color{
  background-color: var(--wildeye-edge-color);
}

.card {
  background-color: var(--wildeye-container-primary);
}

</style>