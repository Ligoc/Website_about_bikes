<template>
    <div class="mx-5">
        <Header /><br><br>
        <h1 class="my-3">Rodzaje rowerów: </h1>  
        <ul>
            <li v-for="bikeType in bikeTypes" :key="bikeType.id">
                <p class="h5 my-4">{{ bikeType.type }}</p>
                <p>{{ bikeType.description }}</p>
            </li>
        </ul>
    </div>

</template>
<script>
import Header from '../components/Header.vue';
export default {
    components: {
        Header
    },
    computed: {
        bikeTypes() {
            return this.$store.state.bikeTypes;
        }

    }
}

</script>