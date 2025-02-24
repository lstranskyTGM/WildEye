<template>
  <div>
    <div class="card h-100 w-100 card-background shadow-sm p-0 m-0">
      <div class="position-relative">
        <div class="carousel slide card-img-top" :id="`carousel${url}`">
          <div class="carousel-inner " style="aspect-ratio: 16 / 9 !important;">
            <div class="carousel-item active " style="aspect-ratio: 16 / 9 !important;">
              <img class=" rounded rounded-bottom-3 d-block w-100" :src="`${serverIP}${url}`" :alt="alt" @click="this.opened = !this.opened">
            </div>
            <div class="carousel-item ratio-16x9" style="aspect-ratio: 16 / 9 !important;">
              <img class=" rounded rounded-bottom-3 d-block w-100" :src="`${serverIP}${AIurl}`" :alt="alt" @click="this.opened = !this.opened">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" :data-bs-target="`#carousel${url}`" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" :data-bs-target="`#carousel${url}`" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>

        </div>
        <div @click="toggleHeart" class="heart-icon z-3">
          <i :class="{'bi bi-heart-fill text-danger': hearted, 'bi bi-heart': !hearted}" ></i>
        </div>
      </div>
      <div class="card-body p-0 m-0" @dblclick="toggleHeart">
        <div class="d-flex justify-content-between p-1 m-1">
          <h5 class="card-title">{{ title }}</h5>
          <small class="small">{{ date }}</small>
        </div>
        <div class="w-100 h-100">
          <div class="d-flex overflow-x-auto px-2" style="max-height: 50px">
            <div v-for="tag in tags" :key="tag" class="me-2 mb-2 p-0">
              <md-assist-chip :label="tag" has-icon="true">
                <md-icon slot="icon"><i :class="tag.icon"></i></md-icon>
              </md-assist-chip>
            </div>
          </div>
        </div>

      </div>
      <md-dialog :open="this.opened" v-on:close="this.opened = false" style="width: 50%;">
        <div slot="headline" class="mb-0 pb-0" style="max-height: 60%!important;">
          <div class="carousel slide w-100" :id="`carouselPopup${url}`">
            <div class="carousel-inner overflow-scroll" style="max-height: 50vh !important;">
              <div class="carousel-item active">
                <img style="min-width: 100% !important;" class=" rounded rounded-bottom-3 d-block w-100 img-fluid" :src="`${serverIP}${url}`" :alt="alt"  >
              </div>
              <div class="carousel-item">
                <img style="min-width: 100% !important;" class=" rounded rounded-bottom-3 d-block w-100 img-fluid" :src="`${serverIP}${AIurl}`" :alt="alt">
              </div>
            </div>
            <button class="carousel-control-prev" type="button" :data-bs-target="`#carouselPopup${url}`" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" :data-bs-target="`#carouselPopup${url}`"  data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>

          </div>
        </div>
        <div slot="content" id="content" class="row mt-2 pt-0" style="max-height: 20vh">
          <div class="d-flex justify-content-between col-12 align-items-center">
            <h1>{{title}}</h1>
            <div @click="toggleHeart" class="">
              <i :class="{'bi bi-heart-fill fs-4 text-danger ': hearted, 'bi bi-heart fs-4 ': !hearted}" ></i>
            </div>
          </div>
          <div class="col-12 h-100 w-100 p-0 m-0">
            <div class="d-flex overflow-x-auto px-2" style="max-height: 50px">
              <div v-for="tag in tags" :key="tag" class="me-2 mb-2 p-0">
                <md-assist-chip :label="tag" has-icon="true">
                  <md-icon slot="icon"><i :class="tag.icon"></i></md-icon>
                </md-assist-chip>
              </div>
            </div>
          </div>
        </div>
        <div slot="actions" style="max-height: 10vh">
          <md-text-button form="form-id" @click="this.opened = false">Close</md-text-button>
        </div>
      </md-dialog>
    </div>
  </div>
</template>

<script>
import "@material/web/all"
import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';

export default {
  name: 'SinglePictureComponent',
  inject: ['serverIP'],
  props: {
    id: Number,
    url: String,
    AIurl: String,
    alt: String,
    title: String,
    date: String,
    hearted: Boolean,
    cameraName: String,
    tags: Array
  },
  setup() {
  },
  data() {
    return {
      opened: false,
      tagMap:{
        "person": {icon: "bi bi-person"},
        "camera": {icon: "bi bi-camera"},
        "lat": {icon: "bi bi-geo-alt"},
        "Deer": {icon: "bi bi-deer"},
        "Goat": {icon: "bi bi-goat"},
        "Bird": {icon: "bi bi-bird"},
        "Dog": {icon: "bi bi-dog"},
        "Cat": {icon: "bi bi-cat"},
        "Horse": {icon: "bi bi-horse"},
        "Rabbit": {icon: "bi bi-rabbit"},
        "Mouse": {icon: "bi bi-mouse"},
        "Cow": {icon: "bi bi-cow"},
        "Elephant": {icon: "bi bi-elephant"},
        "Bear": {icon: "bi bi-bear"},
        "Wild Boar": {icon: "bi bi-pig"},
      }
    }
  },
  methods: {
    toggleHeart() {
      console.log('toggleHeart', this.id);
      this.$emit('update_hearted', {to: !this.hearted, id: this.id});
    }
  },
  created() {

  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  }
}
</script>

<style>
.text-danger {
  color: red;
}

.position-relative {
  position: relative;
}

.heart-icon {
  position: absolute;
  top: 8px;
  right: 8px;
  cursor: pointer;
}

</style>