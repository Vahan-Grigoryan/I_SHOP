import { createStore } from 'vuex'

export default createStore({
  state: {
    categoriesInCrambs: ['GG','WP'],
    profile_content: 'orders'
  },
  getters: {
  },
  mutations: {
    setCategoriesInCrambs(state, crumbs){
      state.categoriesInCrambs = crumbs
    },
    setProfileContent(state, profile_content_value){
      state.profile_content = profile_content_value
    }
  },
  actions: {
  },
  modules: {
  }
})
