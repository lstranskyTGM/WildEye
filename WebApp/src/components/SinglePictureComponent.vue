<template>
  <div>
    <div class="card h-100 w-100 card-background shadow-sm">
      <img class="card-img-top rounded rounded-bottom-3" :src="url" :alt="alt">
      <div class="card-body p-1 m-1" @dblclick="toggleHeart">
        <div class="d-flex justify-content-between">
          <h5 class="card-title">{{ title }} <small class="small">{{ date }}</small></h5>
          <div @click="toggleHeart">
            <i :class="{'bi bi-heart-fill text-danger': hearted, 'bi bi-heart': !hearted}" ></i>
          </div>
        </div>
        <div class="d-flex overflow-x-auto" style="max-height: 50px">
          <div v-for="tag in tags" :key="tag.icon" class="me-2 mb-2">
            <md-assist-chip :label="tag.text" has-icon="true">
              <md-icon slot="icon"><i :class="tag.icon"></i></md-icon>
            </md-assist-chip>
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
  name: 'SinglePictureComponent',
  props: {
    id: Number,
    url: String,
    alt: String,
    title: String,
    date: String,
    hearted: Boolean,
    tags: Array
  },
  setup() {
  },
  data() {
    return {
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
</style>