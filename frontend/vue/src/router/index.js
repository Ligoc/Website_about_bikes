
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "About" */ '../views/About.vue'),
  },
  {
    path: '/bikelist',
    name: 'BikeList',
    component: () => import(/* webpackChunkName: "BikeList" */ '../views/BikeList.vue'),
  },
  {
    path: '/bikelist/:id',
    name: 'BikeListDetails',
    component: () => import(/* webpackChunkName: "BikeListDetails" */ '../views/BikeListDetails.vue'),
    props: true
  },
  {
    path: '/biketypes',
    name: 'BikeTypes',
    component: () => import(/* webpackChunkName: "BikeTypes" */ '../views/BikeTypes.vue'),
  },
  {
    path: '/biketrails',
    name: 'BikeTrails',
    component: () => import(/* webpackChunkName: "BikeTrails" */ '../views/BikeTrails.vue'),
  },
  {
    path: '/:catchAll(.*)',
    name: 'Page404',
    component: () => import(/* webpackChunkName: "Page404" */ '../views/Page404.vue'), 
  },

]
const router = createRouter({
    history: createWebHistory(),  // (process.env.BASE_URL)
    routes
})

export default router


