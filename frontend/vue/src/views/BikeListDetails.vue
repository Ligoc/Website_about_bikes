<template>
    <div v-if="bike">
        <Header /><br><br><br>
        <div class="mx-5 my-4">
            <img class="img-list img-fluid" style="--bs-gap 5rem;" :src="getImageUrl(bike.bikes_id)" alt="">
            <div class="col my-4"> 
                <h1>{{ bike.bikes.bike_model }}</h1>
                <div class="h4">{{ bike.bikes.price | $filters.formatPrice }} zł</div>
            </div>
            <div class="row my-1" v-if="bike.bikes.color">
                <div class="col-2 fw-semibold"><span>Color:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.bikes.color }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.frame">
                <div class="col-2 fw-semibold"><span>Frame:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.frame }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.fork">
                <div class="col-2 fw-semibold"><span>Fork:  </span></div> 
                <div class="col-9 mx-3"><span>{{ bike.fork }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.handlebar">
                <div class="col-2 fw-semibold"><span>Handlebar:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.handlebar }}</span></div>    
            </div>
            <div class="row my-1" v-if="bike.handle_tape">
                <div class="col-2 fw-semibold"><span>Handle Tape:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.handle_tape }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.stem">
                <div class="col-2 fw-semibold"><span>Stem:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.stem }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.seatpost">
                <div class="col-2 fw-semibold"><span>Seatpost:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.seatpost }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.saddle">
                <div class="col-2 fw-semibold"><span>Saddle:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.saddle }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.shift"> 
                <div class="col-2 fw-semibold"><span>Shift:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.shift }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.front_derailleur">
                <div class="col-2 fw-semibold"><span>Front Derailleur:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.front_derailleur }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.rear_derailleur">
                <div class="col-2 fw-semibold"><span>Rear Derailleur:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.rear_derailleur }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.brake">
                <div class="col-2 fw-semibold"><span>Brake:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.brake }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.brake_lever">
                <div class="col-2 fw-semibold"><span>Brake Lever:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.brake_lever }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.cassette">
                <div class="col-2 fw-semibold"><span>Cassette:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.cassette }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.chain">
                <div class="col-2 fw-semibold"><span>Chain:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.chain }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.crankset">
                <div class="col-2 fw-semibold"><span>Crankset:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.crankset }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.bottom_bracket">
                <div class="col-2 fw-semibold"><span>Bottom Bracket:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.bottom_bracket }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.wheel">
                <div class="col-2 fw-semibold"><span>Wheel:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.wheel }}</span></div>
            </div>
            <div class="row my-1" v-if="bike.thru_axle">
                <div class="col-2 fw-semibold"><span>Thru axle:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.thru_axle }}</span> </div>       
            </div>
            <div class="row my-1" v-if="bike.tyre">
                <div class="col-2 fw-semibold"><span>Tyre:  </span></div>
                <div class="col-9 mx-3"><span>{{ bike.tyre }}</span></div> 
            </div>
            <div class="row my-1" v-if="bike.bikes.weight">
                <div class="col-2 fw-semibold"><span>Weight:  </span></div>
                <div class="col-9 mx-3"><span class="fw-semibold">{{ bike.bikes.weight }} kg</span></div> 
            </div>
        </div>
    </div>
</template>
<script>
import Header from '../components/Header.vue';

export default {
    props: ['id'],
    components: {
        Header
    },
    data() {
        return {
            bike: null
        }
    },
    mounted() {
      fetch('http://127.0.0.1:8000/api/all_bikes/' + this.id + '/')
      .then(response => response.json())
      .then(data => this.bike = data)
      .catch(error => console.error(error))
    },
    methods: {
      getImageUrl(bikeId) {
        return `/bikes/bike${bikeId}.jpg`
      }
    }
}

</script>
<style scoped>
.img-list {
    max-height: 500px;
}
</style>