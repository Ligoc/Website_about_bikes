<template>
    <div class="about mx-5 my-4">
        <Header /><br><br><br>
        <h2>O nas</h2>
        <p class="my-3">
            Witaj! Jestem Grzegorz, pasjonat rowerów górskich i twórca tej strony.
            Pragnę podzielić się z Tobą swoją wiedzą i doświadczeniem o rowerach.
        </p>
        <p>
            Na tej stronie znajdziesz nie tylko imponującą kolekcję rowerów gravelowych,
            ale także szczegółowe dane techniczne każdego z nich. Warto wiedzieć,
            że dostępne są różne typy rowerów, a na stronie będę się starał przybliżyć
            Ci różnice i pomóc w znalezieniu twojego pierwszego idealnego rowru.
        </p>
        <p>
            Dodatkowo, zapraszam Cię do skorzystania z porównywarki rowerów 
            (powstanie w przyszłości =] ), która umożliwi Ci bezpośrednie porównanie
            różnych modeli i ich specyfikacji. Dzięki temu będziesz mógł dokonać świadomego wyboru.
        </p>
        <p>
            Ta strona jest dla mnie czymś więcej niż tylko projektem do portfolio.
            To moje osobiste zaangażowanie w promowanie rowerów gravelowych i
            dzielenie się pasją z innymi entuzjastami. Mam nadzieję,
            że czerpiesz z niej radość i inspirację do odkrywania nowych przygód na dwóch kółkach!
        </p>
    </div>
    
</template>
<script>
import Header from '../components/Header.vue';
export default {
    name: 'About',
    components: {
        Header
    },
}
</script>
