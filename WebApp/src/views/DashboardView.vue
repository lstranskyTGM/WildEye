<template>
  <div class="h-100 col-xxl-12 col-xl-12 col-lg-12 col-md-11 col-sm-10 col-10 overflow-y-auto d-grid overflow-x-hidden ps-0 py-3" style="max-height: 100%;">
    <div v-for="camera in this.cameraObjects" :key="camera.id" class="px-0 py-2 ms-auto me-auto" style="height: 100%; min-height: 300px; width: 98%">
      <DashboardMaterialComponent :camera="camera" class="w-100 h-100 shadow" v-on:update_hearted="updateHearted" v-on:navigateToSettings="$router.push('/account')" ></DashboardMaterialComponent>
    </div>
  </div>
</template>

<script>
import DashboardComponent from "@/components/DashboardComponent.vue";
import InputModal from "@/components/InputModal.vue";
import DashboardMaterialComponent from "@/components/DashboardMaterialComponent.vue";
import axios from "axios";

export default {
  name: 'DashboardView',
  inject: ['cameraObjects', "session", "serverIP"],
  components: {
    DashboardMaterialComponent,
    InputModal,
    DashboardComponent
  },
  data() {
    return {
      opened:false,
      cameraObjects: this.cameraObjects
    }
  },
  methods: {
    showModal() {
      this.$refs.inputModal.showModal();
    },
    updateHearted(payload) {
      console.log('updateHearted', payload);
      const index = this.cameraObjects.findIndex(img => img.id === payload.id);
      const documentId = this.cameraObjects[index].documentId;
      console.log(documentId);
      axios.put(`${this.serverIP}/api/wild-cameras/${documentId}`, {data:{hearted: payload.to}})
          .catch(
              err => console.error(err)
          )
          .then(res => {
            console.log(res);
          });
      this.cameraObjects[index].hearted = payload.to;

    }
  },
  mounted() {
    console.log(this.cameraObjects);
  },
  created() {
  },
  destroyed() {
  },
  updated() {
  },
  computed: {
  },
}
</script>

<style>

</style>