import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueSession)

new Vue({
  router,
  store,
  render: h => h(App) // render function
}).$mount('#app')  // el:'#app' 과 동일한 문법
