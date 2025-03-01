<template>
  <div class="w-100 " style="min-width: 200px; min-height: 60px;">
    <div v-if="setting.type==='number'" class="w-100 h-100">
      <md-outlined-text-field
          type="number"
          :label="setting.name"
          class="w-100 h-100 py-2 px-1"
          :value="setting.value"
          v-model="this.setting.value"
      >
      </md-outlined-text-field>
    </div>
    <div v-else-if="setting.type==='string'" class="w-100 h-100">
      <md-outlined-text-field
          type="text"
          :label="setting.name"
          class="w-100 h-100 py-2 px-1"
          :value="setting.value"
          v-model="this.setting.value"
      >
      </md-outlined-text-field>
    </div>
    <div v-if="setting.type === 'select'" class="w-100 h-100">
      <md-outlined-select @change="this.setting.value = $event.target.value" :label="setting.name" class="w-100 h-100">
        <md-select-option v-for="entry in setting.options" :value="entry" :selected="setting.value===entry">
          <div slot="headline">{{ entry }}</div>
        </md-select-option>
      </md-outlined-select>
    </div>
    <div v-if="setting.type === 'boolean'" class="w-100 h-100 d-flex justify-content-between">
      <md-switch icons show-only-selected-icon
                  :selected="this.setting.value"
                 :id="setting.name"
                 @click="this.setting.value = !this.setting.value"
      >
      </md-switch>
      <label :for="setting.name">{{setting.name}}</label>
    </div>
    <div v-else-if="setting.type==='time'" class="w-100 h-100">
      <md-outlined-text-field
          type="time"
          :label="setting.name"
          class="w-100 h-100 py-2 px-1"
          :value="setting.value"
          @input="updateSetting($event.target.value)"
      >
      </md-outlined-text-field>
    </div>
    <div v-else-if="setting.type==='date'" class="w-100 h-100">
      <md-outlined-text-field
          type="date"
          :label="setting.name"
          class="w-100 h-100 py-2 px-1"
          :value="setting.value"
          @input="updateSetting($event.target.value)"
      >
      </md-outlined-text-field>
    </div>
  </div>

</template>

<script>
export default {
  name: 'AdvancedSettingsComponent',
  props: {
    setting: Object
  },
  methods: {
    updateSetting(value) {
      this.$emit('update-setting', { name: this.setting.name, value: this.setting.value });
    }
  }
}
</script>