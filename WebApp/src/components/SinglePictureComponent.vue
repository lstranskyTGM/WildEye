<template>
  <div >
    <div class="card h-100 w-100 card-background shadow-sm p-0 m-0">
      <div class="position-relative">
        <img class=" rounded rounded-bottom-3 d-block w-100" :src="`${serverIP}${showAI? AIurl : url}`" :alt="alt" @click="this.opened = !this.opened">
        <div @click="toggleHeart" class="heart-icon z-3">
          <i :class="{'bi bi-heart-fill text-danger': hearted, 'bi bi-heart': !hearted}" ></i>
        </div>
      </div>
      <div class="card-body p-0 m-0" @dblclick="toggleHeart">
        <div class="d-flex justify-content-between p-1 m-1 overflow-x-hidden">
          <h5 class="card-title">{{ title }}</h5>
          <small class="small">{{ date }}</small>
        </div>
        <div class="w-100 h-100">
          <div class="d-flex overflow-x-auto px-2" style="max-height: 50px">
            <div v-for="set in taggedTags" :key="set.tag" class="me-2 mb-2 p-0">
              <md-assist-chip :label="set.label" :has-icon="set.icon">
                <md-icon slot="icon" v-if="set.icon"><i :class="set.icon"></i></md-icon>
              </md-assist-chip>
            </div>
          </div>
        </div>

      </div>
      <md-dialog :open="this.opened" v-on:close="this.opened = false" style="width: 50%;">
        <div slot="headline" class="mb-0 pb-0" style="max-height: 50%!important;">
          <img style="max-height: 50vh!important;" class=" rounded rounded-bottom-3 d-block img-fluid ms-auto me-auto" :src="`${serverIP}${showAI? AIurl : url}`" :alt="alt"  >
        </div>
        <div slot="content" id="content" class="row mt-2 pt-0" style="max-height: 20vh">
          <div class="d-flex justify-content-between col-12 align-items-center">
            <h1 style="max-width: 80%">{{title}}</h1>
            <div class="d-inline-flex">
              <div @click="this.opened2 = true" class="me-2">
                <i class="bi bi-pencil-square fs-4 text-primary" ></i>
              </div>
              <div @click="toggleHeart" class="">
                <i :class="{'bi bi-heart-fill fs-4 text-danger ': hearted, 'bi bi-heart fs-4 ': !hearted}" ></i>
              </div>
            </div>

          </div>
          <div class="col-12 h-100 w-100 p-0 m-0">
            <div class="d-flex overflow-x-auto px-2" style="max-height: 50px">
              <div v-for="set in taggedTags" :key="set.tag" class="me-2 mb-2 p-0">
                <md-assist-chip :label="set.label" :has-icon="set.icon" >
                  <md-icon slot="icon" v-if="set.icon"><i :class="set.icon"></i></md-icon>
                </md-assist-chip>
              </div>
            </div>
          </div>
        </div>
        <div slot="actions" style="max-height: 10vh">
          <md-text-button form="form-id" @click="this.opened = false">Close</md-text-button>
        </div>
      </md-dialog>
      <!--Dialog for change of title-->
      <md-dialog :open="this.opened2" v-on:close="onChangeTitle" style="--md-dialog-container-color: var(--md-sys-color-secondary-container); max-width: 75vh" >
        <div slot="headline" class="overflow-x-hidden" >
          Change Value of {{this.title}}
        </div>
        <form slot="content" id="form-id" method="dialog">
          <md-outlined-text-field v-model="this.setTitle" label="Change to..." class="mt-1 color-bg roboto-font rounded-2" style="font-family: Roboto, sans-serif">
            <md-icon slot="leading-icon"><i class="bi bi-pencil-square"></i></md-icon>
          </md-outlined-text-field>
        </form>
        <div slot="actions">
          <md-text-button form="form-id" @click="onChangeTitle">Save</md-text-button>
          <md-text-button form="form-id" @click="this.opened2 = false;">Close</md-text-button>
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
    tags: Array,
    showAI: Boolean
  },
  setup() {
  },
  data() {
    return {
      opened: false,
      opened2: false,
      setTitle: "",
      tagMap:{
        "person": {icon: "bi bi-person"},
        "camera": {icon: "bi bi-camera"},
        "lat": {icon: "bi bi-geo-alt"},
        "Deer": {icon: "bi bi-gitlab"},
        "Goat": {icon: "bi bi-gitlab"},
        "Bird": {icon: "bi bi-feather"},
        "Dog": {icon: "bi bi-gitlab"},
        "Cat": {icon: "bi bi-gitlab"},
        "Horse": {icon: "bi bi-gitlab"},
        "Rabbit": {icon: "bi bi-gitlab"},
        "Mouse": {icon: "bi bi-gitlab"},
        "Cow": {icon: "bi bi-gitlab"},
        "Elephant": {icon: "bi bi-gitlab"},
        "Bear": {icon: "bi bi-gitlab"},
        "Wild Boar": {icon: "bi bi-gitlab"},
      },
      taggedTags: {}
    }
  },
  methods: {
    toggleHeart() {
      console.log('toggleHeart', this.id);
      this.$emit('update_hearted', {to: !this.hearted, id: this.id});
    },
    onChangeTitle() {
      this.opened2 = false;
      console.log('onChangeTitle', this.setTitle? this.setTitle : this.title);
      this.$emit('update_title', {to: this.setTitle? this.setTitle : this.title, id: this.id});
    }
  },
  created() {

  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
  },
  computed: {
    // Add computed property for taggedTags
    taggedTags() {
      if (Array.isArray(this.tags)) {
        return this.tags.map(tag => {
          if (!this.tagMap[tag.toLowerCase()]) {
            return {label: tag, icon: ""}
          }
          return {label: tag, icon: this.tagMap[tag.toLowerCase()].icon}
        });
      }
      return [];
    }
  },
  mounted() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];
    // Remove the tag processing code from here
  },
  afterMount() {
    this.setTitle = this.title;
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