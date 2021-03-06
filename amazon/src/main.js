import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueSession from 'vue-session'

Vue.config.productionTip = false

Vue.use(VueSession)


new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
