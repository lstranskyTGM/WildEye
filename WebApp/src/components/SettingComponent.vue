<template>
  <div class="setting-component m-0 p-0 roboto-font d-flex flex-column mt-1" style="font-family: Roboto, sans-serif;">
    <md-filled-text-field :value="value" readonly=true :label="name" class="mt-1 color-bg roboto-font" style="font-family: Roboto, sans-serif">
      <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
    </md-filled-text-field>
    <md-outlined-text-field v-model="newValue" label="Change to..." class="mt-1 color-bg roboto-font" style="font-family: Roboto, sans-serif">
      <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
    </md-outlined-text-field>
    <div v-if="confirm_needed==='true'">
      <md-outlined-text-field v-model="newValue" label="Confirm Input" class="mt-1 color-bg roboto-font" style="font-family: Roboto, sans-serif">
        <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
      </md-outlined-text-field>
    </div>
  </div>
</template>

<script>
import "@material/web/all"
import {styles as typescaleStyles} from '@material/web/typography/md-typescale-styles.js';

export default {
  name: 'SettingComponent',
  props: {
    name: String,
    value: String,
    icon: String,
    confirm_needed: false
  },
  data() {
    return {
      newValue: ""
    }
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
.setting-component {
  max-height: 100%; /* Adjust as needed */
  overflow-y: auto;
}
</style>