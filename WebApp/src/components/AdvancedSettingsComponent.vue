<template>
  <div class="w-100 " style="min-width: 200px; min-height: 60px;">
    <div v-if="setting.type==='number'" class="w-100 h-100">
      <md-outlined-text-field
          type="number"
          :label="setting.name"
          class="w-100 h-100 py-2 px-1"
          :value="setting.value"
          @input="updateSetting($event.target.value)"
      >
      </md-outlined-text-field>
    </div>
    <div v-else-if="setting.type==='string'" class="w-100 h-100">
      <md-outlined-text-field
          type="text"
          :label="setting.name"
          class="w-100 h-100 py-2 px-1"
          :value="setting.value"
          @input="updateSetting($event.target.value)"
      >
      </md-outlined-text-field>
    </div>
    <div v-if="setting.type === 'select'" class="w-100 h-100">
      <md-outlined-select @change="updateSetting($event.target.value)" :label="setting.name">
        <md-select-option v-for="entry in setting.options" :value="entry" :selected="setting.value===entry">
          <div slot="headline">{{ entry }}</div>
        </md-select-option>
      </md-outlined-select>
    </div>
    <div v-if="setting.type === 'boolean'" class="w-100 h-100">
      {{ setting.name }}
      <md-switch icons show-only-selected-icon :selected="setting.value" @change="updateSetting($event.target.checked)"></md-switch>
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
      this.$emit('update-setting', { name: this.setting.name, value });
    }
  }
}
</script>