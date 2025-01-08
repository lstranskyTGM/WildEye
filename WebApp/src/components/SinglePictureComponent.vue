<template>
  <div>
    <div class="card h-100 w-100 card-background shadow-sm p-0 m-0">
      <div class="position-relative">
        <img class="card-img-top rounded rounded-bottom-3" :src="url" :alt="alt">
        <div @click="toggleHeart" class="heart-icon">
          <i :class="{'bi bi-heart-fill text-danger': hearted, 'bi bi-heart': !hearted}" ></i>
        </div>
      </div>
      <div class="card-body p-0 m-0" @dblclick="toggleHeart">
        <div class="d-flex justify-content-between p-1 m-1">
          <h5 class="card-title">{{ title }} <small class="small">{{ date }}</small></h5>
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
    },
    toggleOpened() {
      console.log('toggleOpened', this.id);
      this.opened = !this.opened;
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