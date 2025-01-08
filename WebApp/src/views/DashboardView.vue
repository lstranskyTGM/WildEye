<template>
  <div class="h-100 w-100 col-xxl-12 col-xl-12 col-lg-12 col-md-11 col-sm-12 col-12 overflow-y-auto d-grid overflow-x-hidden ps-0 py-3" style="max-height: 100%;">
    <div v-for="camera in this.cameraObjects" :key="camera.id" class="px-0 py-2 ms-auto me-auto" style="height: 100%; min-height: 250px; width: 98%">
      <DashboardMaterialComponent :camera="camera" class="w-100 h-100 shadow" v-on:update_hearted="updateHearted" v-on:navigateToSettings="$router.push('/account')"></DashboardMaterialComponent>
    </div>
  </div>
</template>

<script>
import DashboardComponent from "@/components/DashboardComponent.vue";
import InputModal from "@/components/InputModal.vue";
import DashboardMaterialComponent from "@/components/DashboardMaterialComponent.vue";

export default {
  name: 'DashboardView',
  components: {
    DashboardMaterialComponent,
    InputModal,
    DashboardComponent
  },
  data() {
    return {
      cameraObjects:[
        {
          name: "Wildkamera 1",
          id: 'dfjk43kb92020',
          battery: 100,
          signal: 100,
          lastPicture: 'https://www.wildeye.de/wp-content/uploads/2021/08/IMG_20210806_123456.jpg',
          lastPictureDate: '2021-08-06 12:34:56',
          lastPictureLocation: 'Berlin',
          numPictures: 69,
          lastSync: '2021-08-06 12:34:56',
          lat: 48.4262157636489,
          lng: 16.61251026756385,
          hearted:false

        },
        {
          name: "Wildkamera 2",
          id: 'dfjk43kb92021',
          battery: 100,
          signal: 100,
          lastPicture: 'https://www.wildeye.de/wp-content/uploads/2021/08/IMG_20210806_123456.jpg',
          lastPictureDate: '2021-08-06 12:34:56',
          lastPictureLocation: 'Deutsch-Wagram',
          numPictures: 69,
          lastSync: '2021-08-06 12:34:56',
          lat: 48.42558212563766,
          lng: 16.61130863793849,
          hearted:false

        },
        {
          name: "Wildkamera 3",
          id: 'dfjk43kb92022',
          battery: 100,
          signal: 100,
          lastPicture: 'https://www.wildeye.de/wp-content/uploads/2021/08/IMG_20210806_123456.jpg',
          lastPictureDate: '2021-08-06 12:34:56',
          lastPictureLocation: 'Deutsch-Wagram',
          numPictures: 9,
          lastSync: '2021-08-06 12:34:56',
          lat: 48.42568212563766,
          lng: 16.61140863793849,
          hearted:false
        }
      ]
    }
  },
  methods: {
    showModal() {
      this.$refs.inputModal.showModal();
    },
    handleModalSubmit(serialCode) {
      console.log('Serial Code:', serialCode);
      // Handle the serial code, e.g., send it to the backend
    },
    showEditModal() {
      this.$refs.editModal.showModal();
    },
    handleEditModalSubmit(changes) {
      console.log('Serial Code:', changes);
      // Handle the serial code, e.g., send it to the backend
    },
    updateHearted(payload) {
      console.log('updateHearted', payload);
      const index = this.cameraObjects.findIndex(img => img.id === payload.id);
      this.cameraObjects[index].hearted = payload.to;
    }
  },
  mounted() {
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