<template>
    <div>
      <Header /><br><br>
      <img class="img-fluid" style="" src="https://www.australiangeographic.com.au/wp-content/uploads/2023/03/Generic-VIC-High-Country_Tourism-VIC_130220-56web-1800x1013.jpg" alt="">
      <h1 class="text-center my-4">Choose your gravel bike</h1>
      <div class="container">
          <div class="row justify-content-between">
            <div class="col-5 my-5" v-for="bike in all_bikes" :key="bike.bikes_id">
              <div class="row" >
                <router-link :to="{ name: 'BikeListDetails', params: {id: bike.bikes_id }}">
                  <img class="img-fluid" style="--bs-gap 5rem;" :src="getImageUrl(bike.bikes_id)" alt="">
                </router-link>
                  <div class="col-2 my-3">
                    <span>Price:</span><br>
                    <span>Brand:</span><br>
                    <span>Model:</span><br>
                    <span>Weight:</span><br>
                  </div>
                  <div class="col my-3">
                    <span class="mx-3 fw-semibold">{{bike.bikes.price}} zł</span><br>
                    <span class="mx-3 fw-semibold">{{bike.bikes.brand}}</span><br>
                    <span class="mx-3 fw-semibold">{{bike.bikes.bike_model}}</span><br>
                    <span class="mx-3 fw-semibold">{{bike.bikes.weight}} kg</span><br>
                  </div>
              </div>
            </div>
          </div>
      </div>
    </div>
  </template>
  <script>
  import {mapActions, mapGetters, mapState } from 'vuex'
  import Header from '../components/Header.vue'

  export default {
    name: 'App',
    components: { Header },
    computed: {
      ...mapState(['all_bikes'])
    },
    created() {
      this.$store.dispatch('loadBikes')
    },
    methods: {
      getImageUrl(bikeId) {
        return `/bikes/bike${bikeId}.jpg`
      }
    }
  }
  </script>
  <style scoped>

  </style>


