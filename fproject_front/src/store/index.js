import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    categoriesInCrambs: ['GG','WP'],
    profile_content: 'orders',
    server_href: 'http://localhost:8000/'
  },
  getters: {
    fetchCategories: state => async (categories_position=false) => {
      const categories = await axios.get(
        `${state.server_href}categories?categories_position=${categories_position}`
      )
      return categories.data
    },
    fetchProductDetail: state => async product_id => {
      const product = await axios.get(`${state.server_href}products/${product_id}`)
      return product.data
    },
    fetchProductsBySaleNewHit: state => async sale_new_hit => {
      const products = await axios.get(`${state.server_href}products_index?sale_new_hit=${sale_new_hit}`)
      return products.data
    },
    getImageUrl: state => after_server_domain => {
      return state.server_href + 'media/' + after_server_domain
    },
    fetchBrandsIndex: state => async () => {
      const brands = await axios.get(`${state.server_href}brands_index`)
      return brands.data
    },
    fetchBlogsIndex: state => async () => {
      const blogs = await axios.get(`${state.server_href}blogs_index`)
      return blogs.data
    },

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
