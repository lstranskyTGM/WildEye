<template>
  <div class="m-0 p-0 roboto-font" style="font-family: Roboto, sans-serif">
    <md-outlined-text-field :value="value" readonly=true :label="name" class="mt-1 color-bg roboto-font" style="font-family: Roboto, sans-serif">
      <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
    </md-outlined-text-field>
  </div>
</template>

<script>



import "@material/web/all"
import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';
export default {
  name: 'DashboardInfoComponent',
  props: {
    name: String,
    value: String,
    icon: String
  },
  beforeMount() {
    document.adoptedStyleSheets = [typescaleStyles.styleSheet];

  },
  mounted() {
  },
  created() {

  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

@import "../../css/treeGreen.css";



.color-bg {
  background-color: white;
}
</style>