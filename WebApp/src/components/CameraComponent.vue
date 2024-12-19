<template>
  <div class="card h-100 rounded rounded-3 px-0 container_color">
    <div class="h-100 position-relative" style="max-height: 100% !important; width: 100%;">
      <div class="card-header row m-0 border border-0 mx-0 px-0 d-felx" style="height: 30%;">
        <h2 class="card-title mt-auto mb-auto ">{{ name }}</h2>
        <!--            <i class="bi bi-check-all position-absolute top-0 text-end pe-3 pt-2 fs-3" ></i>
                    <p class="position-absolute text-end pe-3 " style="top: 13%">Apply all changes</p>-->
        <div class="d-flex position-absolute top-0 end-0 pe-3 pt-2" style="right: 0;">
          <md-fab variant="primary" aria-label="apply" class="fs-3 ms-auto mt-auto mb-auto">
            <md-icon slot="icon"><i class="bi bi-check-all"></i></md-icon>
          </md-fab>
        </div>

        <hr class="mt-0 position-absolute" style="top: calc(30% - 0.75px); left: 1%; width: 98%">
      </div>
      <div class="card-body row m-0 p-0 pt-2" style="height: 70%; max-width: 100%">
        <div class="w-50 h-100 border border-top-0 border-bottom-0 border-start-0 border-end-3" style="min-width: 150px">
          <SettingComponent name="Name" :value="name" confirm_needed="false" icon="bi bi-camera"></SettingComponent>
          <md-outlined-button @click="this.opened= true">
            Open advanced settings
            <svg slot="icon" viewBox="0 0 48 48"><path d="M9 42q-1.2 0-2.1-.9Q6 40.2 6 39V9q0-1.2.9-2.1Q7.8 6 9 6h13.95v3H9v30h30V25.05h3V39q0 1.2-.9 2.1-.9.9-2.1.9Zm10.1-10.95L17 28.9 36.9 9H25.95V6H42v16.05h-3v-10.9Z"/></svg>
          </md-outlined-button>
        </div>
        <div class="w-50 h-100" style="min-width: 150px; ">
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
  <md-dialog :open="this.opened" v-on:close="this.opened = false">
    <div slot="headline">
      {{this.text}}
    </div>
    <form slot="content" id="form-id" method="dialog">
      A simple dialog with free-form content.
    </form>
    <div slot="actions">
      <md-text-button form="form-id" @click="this.opened = false">Ok</md-text-button>
    </div>
  </md-dialog>
</template>

<script>

  import SettingComponent from "@/components/SettingComponent.vue";
  import "@material/web/all"

  export default {
    name: 'CameraComponent',
    components: {SettingComponent},
    data(){
      return{
        text:"kjdfghlskdjfgh",
        opened:false
      }
    },
    props: {
      name: String,
      info: String
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