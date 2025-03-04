<template>
  <div class="setting-component m-0 p-0 roboto-font d-flex flex-column mt-2 h-100 w-100" style="font-family: Roboto, sans-serif;">
    <md-outlined-text-field :value="value" readonly=true :label="name" class="mt-1 color-bg roboto-font rounded-3" style="font-family: Roboto, sans-serif">
      <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
    </md-outlined-text-field>

    <div v-if="!popup">
      <md-outlined-text-field v-model="newValue" label="Change to..." class="mt-1 color-bg roboto-font rounded-2" style="font-family: Roboto, sans-serif">
        <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
      </md-outlined-text-field>
      <div v-if="confirm_needed==='true'">
        <md-outlined-text-field v-model="confirmValue" label="Confirm Input" class="mt-1 color-bg roboto-font rounded-2" style="font-family: Roboto, sans-serif">
          <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
        </md-outlined-text-field>
      </div>
    </div>
    <div v-else>
      <div class=" text-center d-grid mt-2" @click="this.opened = !this.opened" >
        <md-outlined-button>
          Change
          <md-icon slot="icon"><i class="bi bi-pencil-square"></i></md-icon>
        </md-outlined-button>
      </div>
      <md-dialog :open="this.opened" v-on:close="this.opened = false">
        <div slot="headline">
          Change Value of {{name}}
        </div>
        <form slot="content" id="form-id" method="dialog">
          <md-outlined-text-field v-model="newValue" label="Change to..." class="mt-1 color-bg roboto-font rounded-2" style="font-family: Roboto, sans-serif">
            <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
          </md-outlined-text-field>
          <div v-if="confirm_needed==='true'">
            <md-outlined-text-field v-model="confirmValue" label="Confirm Input" class="mt-1 color-bg roboto-font rounded-2" style="font-family: Roboto, sans-serif">
              <md-icon slot="leading-icon"><i :class="icon"></i></md-icon>
            </md-outlined-text-field>
          </div>
        </form>
        <div slot="actions">
          <md-text-button form="form-id" @click="this.opened = false">Save</md-text-button>
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
  name: 'SettingComponent',
  props: {
    name: String,
    value: String,
    icon: String,
    popup: false,
    confirm_needed: false
  },
  data() {
    return {
      newValue: "",
      confirmValue: "",
      opened: false
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