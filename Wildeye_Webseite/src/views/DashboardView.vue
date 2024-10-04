<template>
  <div class="h-100 w-100 col-xxl-12 col-xl-12 col-lg-12 col-md-11 col-sm-12 col-12 overflow-y-auto" style="max-height: 100%;">
    <div v-for="camera in this.cameraObjects" class="py-2" style="height: 26%; min-height: 300px;">
      <DashboardComponent :camera="camera" class="w-100 h-100 shadow" ></DashboardComponent>
    </div>
  </div>
</template>

<script>
import DashboardComponent from "@/components/DashboardComponent.vue";

export default {
  name: 'DashboardView',
  components: {
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
          lat: 48.31561796122741,
          lng: 16.58404319905392,
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
          lat: 48.31561796122741,
          lng: 16.58404319905392,
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
          lat: 48.31561796122741,
          lng: 16.58404319905392,
        }
      ]
    }
  },
  methods: {

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