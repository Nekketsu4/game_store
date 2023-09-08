<template>
  <div id="app">
    <div class="wrapper">
      <Head />
      <router-view/>

      <Payment />
      <Subscribe />
      <Footer />
    </div>
  </div>
</template>

<style>
  @import 'assets/css/reset.css';
  @import 'assets/css/style.css';
</style>

<script>
  import Head from './components/Head';
  import Payment from './components/Payment';
  import Subscribe from './components/Subscribe.vue';
  import Footer from './components/Footer.vue';
  export default {
    components: {Head, Payment, Subscribe, Footer}
  }
</script>
