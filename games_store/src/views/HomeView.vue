<template>
  <div id="toTheMoon"  class="home" >
    <div class="content ">
      <div  class="container">

        <div class="content-row">
          <nav class="content__nav-row">
            
            <ul>
              <li v-for="genre in listGenres" :key="genre.id"><a href="#" @click="wrongLink()">{{ genre.title }}</a></li>
            </ul>
          </nav>
          <div class="content__body">
            <div><a class="back" id="take" href="#"></a></div>
            <div class="content__head ">Каталог</div>
            <div class="content__item-row">
              <div v-for="game in listGames" :key="game.id" @click="wrongLink()" class="content__column">
                <div class="content__item">
                  <img ref="imgs" :src="game.main_image" alt="">
                </div>
                <div class="content__title">{{ game.title}}</div>
                <div class="content__genre">{{ game.genre }}</div>
                <div class="content__price">{{ game.price }} Р</div>
                <div class="content__buy-button"><a href="#">Купить</a></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'HomeView',
    data() {
      return {
        listGames: [],
        listGenres: [],
        page: 1,
        hasNext: true,
      }
    },
    components: {},

    computed: {},

    created() {
      this.loadListGames()
      this.loadListGenres()
      this.wrongLink
      
      window.onscroll = () => {
        let scrollTop = document.documentElement.scrollTop
        let innerHeight = window.innerHeight
        let scrollHeight = document.documentElement.scrollHeight
        let scrollToBottom = scrollTop +  innerHeight === scrollHeight
        
        if (scrollToBottom && this.hasNext) {
          this.page += 1
          this.loadListGames()
        }
      }


    },

    methods: {
      async loadListGames() {
        this.listGames = await fetch(
          `${this.$store.getters.getServerUrl}/list_games?page=${this.page}`
          ).then(response => response.json()
          ).then(response => {

            this.hasNext = false

            setTimeout(() => {
              if (response.links.next) {
              this.hasNext = true
            }
            }, 1000);
            
            for (let i = 0; i < response.results.length; i++) {
              this.listGames.push(response.results[i])  
            }
            return this.listGames
          })
      },
      async loadListGenres() {
          this.listGenres = await fetch(
          `${this.$store.getters.getServerUrl}/list_genres`
          ).then(response => response.json())
      },
      wrongLink() {
        alert('Сайт находится на стадии разработки. Страница по этой ссылке либо не существует, либо отсутствует необходимый функционал для ее работы!')
      },
    }
  }


</script>

<style scoped>

  .back {
    width: 60px;
    height: 60px;
    display: block;
    position: fixed;
    z-index: 10;
    /* background-color: green; */
    background-image: url(../assets/img/up-arrow.png);
    background-repeat: no-repeat;
    background-size: contain;
    right: 360px;
    top: 600px;
    cursor: pointer;
    opacity: 0.5;
  }
</style>
