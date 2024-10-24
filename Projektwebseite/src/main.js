import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import '../public/bootstrap-5.3.3-dist_/css/bootstrap.min.css'
// import '../public/bootstrap-5.3.3-dist_/js/bootstrap.bundle.min.js'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import 'bootstrap-icons/font/bootstrap-icons.css';

createApp(App).use(router).mount('#app')
