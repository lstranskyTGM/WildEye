<template>
  <div class="w-100 h-100" >
    <div class="ratio ratio-16x9 card w-100 h-100 card_background">
      <div class="h-100 position-relative" style="max-height: 100% !important; top: -100%">
        <div class="card-header row m-0 mx-0 px-0 border border-0 d-flex align-items-center justify-content-between" style="height: 30%;">
          <h3 class="card-title">{{ this.camera.name }}</h3>
          <div class="position-absolute top-0 text-end pe-3 pt-3 fs-3">
            <i :class="{'bi bi-heart-fill text-danger pe-2': camera.hearted, 'bi bi-heart pe-2': !camera.hearted}" @click="toggleHeart"></i>
            <i class="bi bi-images pe-2" @click="launchPictureView(camera.id)"></i>
            <i class="bi bi-pencil-square " @click="console.log('hallo')"></i>
          </div>
          <hr class="mt-0 position-absolute" style="top: calc(30% - 0.75px); left: 2%; width: 96%">
        </div>
        <div class="card-body d-inline-flex p-3 pt-1 m-0" style="height: 75%">
          <div class="w-50 h-100 pt-0 mt-auto mb-auto" >
            <DashboardInfoComponent name="Battery" value="86%" icon="bi bi-battery-half" class="w-100 pt-0 mt-0"></DashboardInfoComponent>
            <DashboardInfoComponent name="Last Synchronization" value="01.12.2024 09:31" icon="bi bi-cloud-upload" class="w-100 pt-2"></DashboardInfoComponent>
          </div>
          <div class="w-50 h-100 ps-2 pt-0 mt-0">
            <b>Last Capture:</b>
            <img :src="camera.lastCapturePreview" :alt="camera.name" class="rounded rounded-3 img-fluid ">
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import "@material/web/all"
import {styles as typescaleStyles} from "@material/web/typography/md-typescale-styles";
import DashboardInfoComponent from "@/components/DashboardInfoComponent.vue";
import SinglePictureComponent from "@/components/SinglePictureComponent.vue";

export default {
  name: 'MarkerPopupMaterialComponent',
  props: {
    camera: {
      type: Object,
      required: true
    }
  },
  components: {
    SinglePictureComponent,
    DashboardInfoComponent
  },
  setup() {
  },
  data() {
    return {
      name: 'MarkerPopupComponent',
    }
  },
  methods: {
    launchPictureView(id){
      console.log("launching pictureVire for camera with id: "+id);
      this.$router.push({name: 'pictures', query: {id: id}});
    },
    toggleHeart() {
      console.log('toggleHeart', this.camera.id);
      this.$emit('update_hearted', {to: !this.camera.hearted, id: this.camera.id});
    }
  },
  computed: {
  },
  watch: {
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  },
  mounted() {
  },
  beforeDestroy() {
  },
  destroyed() {
  }
}
</script>

<style scoped>
.card_background {
  background-color: var(--wildeye-container-primary);
}
</style>