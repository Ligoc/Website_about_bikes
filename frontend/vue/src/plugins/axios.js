import axios from 'axios'

export function createAppWithAxios(app) {
  app.config.globalProperties.axios = axios
}
