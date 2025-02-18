<template>
  <div>
    <div class="card h-100 w-100 card-background shadow-sm p-0 m-0">
      <div class="position-relative">
        <div class="carousel slide card-img-top">
          <div class="carousel-inner">
            <div class="carousel-item">
              <img class=" rounded rounded-bottom-3 d-block w-100" :src="url" :alt="alt" @click="this.opened = !this.opened">
            </div>
            <div class="carousel-item">
              <img class=" rounded rounded-bottom-3 d-block w-100" :src="AIurl" :alt="alt" @click="this.opened = !this.opened">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>

        </div>
        <div @click="toggleHeart" class="heart-icon">
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
            <div v-for="tag in tags" :key="tag.icon" class="me-2 mb-2 p-0">
              <md-assist-chip :label="tag.text" has-icon="true">
                <md-icon slot="icon"><i :class="tag.icon"></i></md-icon>
              </md-assist-chip>
            </div>
          </div>
        </div>

      </div>
      <md-dialog :open="this.opened" v-on:close="this.opened = false" style="width: 50%;">
        <div slot="headline" class="mb-0 pb-0">
          <img class="img-fluid h-50 rounded-3" :src="url" :alt="alt">
        </div>
        <div slot="content" id="content" class="row mt-2 pt-0">

          <div class="d-flex justify-content-between col-12 align-items-center">
            <h1>{{title}}</h1>
            <div @click="toggleHeart" class="">
              <i :class="{'bi bi-heart-fill fs-4 text-danger ': hearted, 'bi bi-heart fs-4 ': !hearted}" ></i>
            </div>
          </div>
          <div class="col-12 h-100 w-100 p-0 m-0">
            <div class="d-flex overflow-x-auto px-2" style="max-height: 50px">
              <div v-for="tag in tags" :key="tag.icon" class="me-2 mb-2 p-0">
                <md-assist-chip :label="tag.text" has-icon="true">
                  <md-icon slot="icon"><i :class="tag.icon"></i></md-icon>
                </md-assist-chip>
              </div>
            </div>
          </div>
        </div>
        <div slot="actions">
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
      opened: false
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