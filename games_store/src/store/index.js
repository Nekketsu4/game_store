import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)


const store = new Vuex.Store({
  state: {
    backendUrl: "http://31.129.103.72/api/v1"
  },
  mutations: {},
  actions: {},
  modules: {},
  getters: {
    getServerUrl: state => {
      return state.backendUrl
    }
  }
})


export default store