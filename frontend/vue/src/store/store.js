import { createStore } from 'vuex';
import axios from 'axios'
import { bikeTypes } from './bikeTypes.js';
import { trailparks } from './trailparks.js';
import { singletracks } from './singletracks.js'


export default createStore({
    bikeTypes,
    singletracks,
    state: {
      all_bikes: [],
      bikeTypes: bikeTypes,
      trailparks: trailparks,
      singletracks: singletracks,
    },
    mutations: {
      setAllBikes(state, bikes) {
        state.all_bikes = bikes;
      }
    },
    actions: {
      loadBikes(context) {
        axios.get('http://127.0.0.1:8000/api/all_bikes')
        .then(res => {
          context.commit('setAllBikes', res.data);
        })
        .catch(error => {
          console.error(error);
        });
      },
    },  
    modules: {
    },
    getters: {
      getAllBikes: state => state.all_bikes,
    }
});
