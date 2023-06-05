<template>
    <nav class="navbar navbar-expand-lg bg-dark fixed-top">
        <div class="container-fluid ">
            <router-link class="navbar-brand text-light" to="/"><i class="bi bi-house-door-fill"></i> Home</router-link>
            <router-link class="navbar-brand text-light" to="/bikelist"><i class="bi bi-bicycle"></i> Bikes</router-link>
            <router-link class="navbar-brand text-light" to="/biketypes"><i class="bi bi-file-earmark-richtext"></i> Bikes Types</router-link>
            <router-link class="navbar-brand text-light" to="/biketrails"><i class="bi bi-signpost-split"></i> Trails</router-link>
            <router-link class="navbar-brand text-light me-auto" to="/about">About</router-link>
            <form class="d-flex" role="search" @submit.prevent="searchBikes">
                <input class="form-control me-2" type="search" v-model="searchText" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-light" type="submit">Search</button>
            </form>
        </div>
    </nav>

</template>
<script>
export default {
  data() {
    return {
      searchText: '',
      bikes: [],
    };
  },
  methods: {
    searchBikes() {
      this.axios
        .get('http://127.0.0.1:8000/api/bike-search/', {
          params: {
            search: this.searchText,
          },
        })
        .then(response => {
          this.bikes = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>

</style>
