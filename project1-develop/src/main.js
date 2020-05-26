import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueAgile from 'vue-agile'
import VueResource from 'vue-resource'
import axios from 'axios'
import VueAxios from 'vue-axios'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import App from './App.vue'
import router from './router'


Vue.use(BootstrapVue)
Vue.use(VueAgile)

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
