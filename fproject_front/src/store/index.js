import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    pagesInCrumbs: new Set(),
    profile_content: 'orders',
    server_href: 'http://localhost:8000/',
    headers: {'Authorization': `JWT ${localStorage.getItem('access')}`},
  },
  getters: {
    fetchCategories: state => async (categories_position=false) => {
      const categories = await axios.get(
        `${state.server_href}categories?categories_position=${categories_position}`
      )
      return categories.data
    },
    fetchCategoryProducts: state => async (category_name, product_id) => {
      const products = await axios.get(
        `${state.server_href}category_products/${category_name}?current_product_id=${product_id}`
      )
      return products.data
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
      if (!after_server_domain.includes('media')) {
        return state.server_href + 'media/' + after_server_domain
      } else {
        return state.server_href + after_server_domain.slice(1)
      }
      
    },
    fetchBrandsIndex: state => async () => {
      const brands = await axios.get(`${state.server_href}brands_index`)
      return brands.data
    },
    fetchBlogsIndex: state => async () => {
      const blogs = await axios.get(`${state.server_href}blogs_index`)
      return blogs.data
    },
    fetchUserProfileInfo: state => async id => {
      const user = await axios.get(`${state.server_href}users_profile/${id}`)
      return user.data
    },
    commonGETRequestWithAuth: state => async url_after_server_domain => {
      try{
        const page = await axios.get(state.server_href + url_after_server_domain, {
          headers: state.headers
        })
        return page.data
      }catch(err){
        return
      }

    },
    commonPOSTRequestWithAuth: state => async (url_after_server_domain, post_data) => {
      if (localStorage.getItem('access')) {
        try{
          const page = axios.post(state.server_href + url_after_server_domain, post_data, {
            headers: state.headers
          })
          return page.data
        }catch(err){
          localStorage.removeItem('access')
          return
        }
      }
    },
    
  },
  mutations: {
    setProfileContent(state, profile_content_value){
      state.profile_content = profile_content_value
    },
    updateHeaders(state){
      state.headers = {'Authorization': `JWT ${localStorage.getItem('access')}`}
    }

  },
  actions: {
    async updateUser({state}){
      const current_user = JSON.parse(localStorage.getItem('current_user'))
      const user = await axios.get(`${state.server_href}users_mini_info?id=${current_user.id}`, {
        headers: state.headers
      })
      localStorage.setItem('current_user', JSON.stringify(user.data))
    }
  },
  modules: {
  }
})
