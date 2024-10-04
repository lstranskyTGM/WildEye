<template>
  <div class="h-100 card col-xxl-12 col-xl-12 col-lg-12 col-md-11 col-sm-12 col-12" style="max-height: 90vh;">
    <div class="card-body overflow-y-scroll">
      <div class="">
        <div class="row">
          <div class="col-12">
            <div class="masonry">
              <div class="masonry-item" v-for="(img, index) in images" :key="index">
                <img :src="img.url" :alt="img.alt" class="img-fluid" :width="img.width"
                     :style="{height :randomIntFromInterval(Math.min(200, img.height), img.height) +'px', objectFit: 'cover'}">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="card-footer">
      <div class="row w-100">
        <div class="col-6">
          <p class="text-primary-emphasis">
            {{ name }}
          </p>
        </div>
        <div class="col">
          <div class="row">
            <div class="col">
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon2">Suchen</span>
                </div>
                <input type="text" class="form-control" placeholder="Search" aria-label="Search" aria-describedby="basic-addon1">
              </div>
            </div>
            <div class="col">
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon2">Bilder pro Seite</span>
                </div>
                <input type="number" class="form-control" placeholder="25" aria-label="bilder" aria-describedby="basic-addon2">
              </div>
            </div>
            <div class="col">
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon3">Wildkamera</span>
                </div>
                <input type="text" class="form-control" placeholder="1" aria-label="1" aria-describedby="basic-addon3">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
<!--    <div class="">
      <div class="row w-100">
        <div class="col-6">
          <p class="text-primary-emphasis">
            {{ name }}
          </p>
        </div>
        <div class="col">
          <div class="row">
            <div class="col">
              <input type="text" name="" id="">
              <p>Label 1</p>
            </div>
            <div class="col">
              <input type="text" name="" id="">
              <p>Label 2</p>
            </div>
            <div class="col">
              <input type="text" name="" id="">
              <p>Label 3</p>
            </div>
          </div>
        </div>
      </div>
      <div class="">
        <div class="row overflow-y-auto" style="max-height: 100vh; overflow-y: auto; padding-bottom: 6rem;">
          <div class="col-md-4 mb-4" v-for="(img, index) in images" :key="index">
            <div class="card">
              <img :src="img.url" :alt="img.alt" class="card-img-top img-fluid" style="object-fit: cover; height: 200px;">
              <div class="card-body">
                <p class="card-text">Hier können Informationen über das bild stehen, halt wenn diese ai funktionen von julian funktionieren oder einfach Daten über das Bild.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>-->
  </div>
</template>

<script>
// Hier sollte ich auch das setzen von einstellungen über query params erlauben, das kann ich dann gut verbinden mit der karte!!!!!11!!!!!!!!!!!!1!1!
import router from "@/router";

export default {
  name: 'PictureView',
  components: {
  },
  setup() {
  },
  data() {
    return {
      name: 'PictureView',
      images:[
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder1', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder2', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder3', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder4', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder5', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder6', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder7', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder8', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder9', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder10', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder11', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder12', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder13', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder14', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder15', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder16', width: 600, height: 400},
        {url: 'https://dummyimage.com/600x400/000/4e5285&text=Hallo!', alt: 'placeholder17', width: 600, height: 400},
      ],
    }
  },
  methods: {
    randomIntFromInterval(min, max) { // min and max included
      var r = Math.floor(Math.random() * (max - min + 1) + min)
      console.log(r)
      return r
    }
  },
  computed: {
  },
  watch: {
  },
  mounted() {
    console.log(router.currentRoute.value.query)
  },
  beforeDestroy() {
  },
  destroyed() {
  }
}
</script>

<style scoped>
.masonry {
  column-count: 4; /* Number of columns */
  column-gap: 1rem; /* Gap between columns */
}

.masonry-item {
  break-inside: avoid;
  margin-bottom: 1rem;
}
</style>