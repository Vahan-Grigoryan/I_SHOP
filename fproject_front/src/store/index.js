import { createStore } from 'vuex'

export default createStore({
  state: {
    categoriesInCrambs: ['GG','WP']
  },
  getters: {
  },
  mutations: {
    setCategoriesInCrambs(state, crumbs){
      state.categoriesInCrambs = crumbs
    }
  },
  actions: {
  },
  modules: {
  }
})
