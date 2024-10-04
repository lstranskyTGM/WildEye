import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PictureView from "@/views/PictureView.vue";
import MapView from "@/views/MapView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/picture',
    name: 'pictures',
    component: PictureView
  },
  {
    path: '/map',
    name: 'map',
    component: MapView
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
