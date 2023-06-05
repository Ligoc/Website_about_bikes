import { createApp } from 'vue'
import store from './store/store.js';
import App from './App.vue'
import { createAppWithAxios } from './plugins/axios'
import router from './router'

const app = createApp(App)

app.config.globalProperties.$filters = {
    formatPrice(value) {
      if (typeof value !== 'number') {
        value = Number(value);
      }
      return value.toLocaleString('en-US');
    }
};

createAppWithAxios(app)
app.use(router)
app.use(store)
app.mount('#app')