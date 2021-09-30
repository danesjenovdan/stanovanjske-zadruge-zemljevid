import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { createWebHistory, createRouter } from "vue-router";


const routes = [
    { path: '/', component: App },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

createApp(App).use(VueAxios, axios).use(router).mount('#app')
