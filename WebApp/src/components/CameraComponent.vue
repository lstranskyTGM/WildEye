<template>
  <div class="card h-100 rounded rounded-3 px-0">
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
</template>

<script>

  import SettingComponent from "@/components/SettingComponent.vue";

  export default {
    name: 'CameraComponent',
    components: {SettingComponent},
    data(){
      return{

      }
    },
    props: {
      name: String,
      info: String
    }
  }
</script>

<style>
hr{
  color: var(--md-sys-color-scrim) !important;
  border-width: 1.5px;
  background-color: var(--md-sys-color-scrim) !important;
  opacity: 0.5;
  border-radius: 5px;
}
</style>