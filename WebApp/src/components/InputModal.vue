<template>
  <div class="modal fade" tabindex="-1" ref="modal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ header }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>{{ text }}</p>
          <input type="text" v-model="inputValue" class="form-control" :placeholder="hint" v-on:keydown.enter="this.saveChanges">
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="saveChanges">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap';
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

export default {
  name: 'InputModal',
  props: {
    header: String,
    text: String,
    hint: String
  },
  data() {
    return {
      inputValue: ''
    };
  },
  methods: {
    showModal() {
      const modal = new Modal(this.$refs.modal);
      modal.show();
    },
    saveChanges() {
      this.$emit('submit', this.inputValue);
      const modal = Modal.getInstance(this.$refs.modal);
      modal.hide();
      this.inputValue = '';
    }
  }
}
</script>

<style>
/* Add any custom styles here */
</style>