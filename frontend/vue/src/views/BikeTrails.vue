<template>
    <div>
        <Header /><br><br>
        <img src="/img/single02.jpg"  class="img-fluid max-height-100" alt="Image">
        <div class="container my-5">
          <h1>Singletracki:</h1>
          <div class="row justify-content-between">
            <div class="col-5 my-5" v-for="singletrack in singletracks" :key="singletrack.id">
                <a :href="singletrack.url"><img class="img-fixed-size img-fluid" style="--bs-gap 5rem;" :src="getImgSing(singletrack.img)" alt=""></a>  
              <div class="row">
                  <div class="col my-3">
                    <span class="fw-semibold">{{ singletrack.title }} </span><br>
                    <span class="fw-semibold">{{ singletrack.location }}</span><br>
                  </div>
              </div>
            </div>
          </div>
        </div>
        <img src="/img/dh01.jpg"  class="img-fluid max-height-100" alt="Image">
        <div class="container my-5">
            <h1>Bike parki:</h1>
            <div class="row justify-content-between">
                <div class="col-5 my-5" v-for="trailpark in trailparks" :key="trailpark.id">
                    <a :href="trailpark.url"><img class="img-fixed-size img-fluid" style="--bs-gap 5rem;" :src="getImgTrail(trailpark.img)" alt=""></a>
                <div class="row">
                    <div class="col my-3">
                        <span class="fw-semibold">{{ trailpark.title }} </span><br>
                        <span class="fw-semibold">{{ trailpark.location }}</span><br>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>
    

</template>

<script>
import Header from '../components/Header.vue';
export default {
    components: {
        Header
    },
    computed: {
        singletracks() {
            return this.$store.state.singletracks;
        },
        trailparks() {
            return this.$store.state.trailparks;
        }
    },
    methods: {
      getImgTrail(imgTrail) {
        return `/trailparks/${imgTrail}`
      },
      getImgSing(imgSin) {
        return `/singletracks/${imgSin}`
      }
    }
}
</script>
<style scoped>

.img-fixed-size {
    width: 200px; 
    height: 200px; 
}
</style>
