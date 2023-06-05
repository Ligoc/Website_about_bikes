<template>
  <div>
    <form @submit.prevent="searchBikes">
      <input type="text" v-model="searchText" placeholder="Search">
      <button type="submit">Search</button>
    </form>

    <ul v-if="bikes.length > 0">
      <li v-for="bike in bikes" :key="bike.id">
        {{ bike.brand }} - {{ bike.bike_model }}
      </li>
    </ul>
    <p v-else>No results found.</p>
  </div>
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
