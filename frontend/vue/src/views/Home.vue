<template>
    <div class="home">
        <Header /><br><br>
        <h1 class="text-center fs-1 m-4">With passion for bikes</h1>
        <img class="image" src="https://img5.goodfon.com/original/1600x900/b/2d/velosiped-doroga-gora.jpg" alt="">
        <h1 class="text-center fs-1 m-4">We offer you best bikes</h1>
        <img class="image" src="/img/img02.jpg" alt="">
        <h1 class="text-center fs-1 m-4">Best trails</h1>
        <img class="image" src="https://wallpapercave.com/wp/wp2889098.jpg" alt="">
        <h2 class="text-center fs-1 m-4">And a lot information as you want.</h2>
    </div> 

</template>
<script>

import Header from '../components/Header.vue';

export default {
    name: 'Home',
    components: { Header},
}
</script>
<style scoped>
    .home {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
