import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/note/add',
    name: 'Add note',
    component: () => import(/* webpackChunkName: "AddNote" */ '@/views/AddNote')
  },
  {
    path: '/note/:id',
    name: 'Note detail',
    component: () => import(/* webpackChunkName: "NoteInfo" */ '@/views/NoteDetail')
  }
]

const router = new VueRouter({
  routes
})

export default router
