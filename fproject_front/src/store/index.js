import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    pagesInCrumbs: new Set(),
    profile_content: 'orders',
    cookies: document.cookie.split('; ').map( raw_cookie => raw_cookie.split('=') ),
    server_href: 'http://localhost:8000/',
    headers: async () => {
      return {'Authorization': `JWT ${(await cookieStore.get('access')).value}`}
    },
  },
  getters: {
    getImageUrl: state => after_server_domain => {
      if (after_server_domain.includes('http') || after_server_domain.includes('https')) {
        return after_server_domain
      }
      else if (!after_server_domain.includes('media')) {
        return state.server_href + 'media/' + after_server_domain
      } else {
        return state.server_href + after_server_domain.slice(1)
      }
    },
    getUser: state => async () => {
      if (await cookieStore.get('user_id')) {
        return {
          id: (await cookieStore.get('user_id')).value,
          first_name: (await cookieStore.get('user_first_name')).value,
          photo: (await cookieStore.get('user_photo')).value,
          liked_products_count: (await cookieStore.get('user_liked_products_count')).value,
          ordered_products_count: (await cookieStore.get('user_ordered_products_count')).value,
        } 
      }
      return null
      
    },
    // delCookie: state => key => {
    //   const cookie = state.cookies.find(cookie => cookie[0] === key)
    //   const [lIndex, rIndex] = [document.cookie.indexOf(cookie[0])-1, document.cookie.indexOf(cookie[1])+cookie[1].length+1]
    //   const [lSide, rSide] = [document.cookie.slice(0, lIndex), document.cookie.slice(rIndex)];
    //   document.cookie = lSide+rSide
    // },
    
  },
  mutations: {
    setProfileContent(state, profile_content_value){
      state.profile_content = profile_content_value
    },
    // updateHeaders(state, token_type='JWT'){
    //   state.headers = {'Authorization': `${token_type} ${localStorage.getItem('access')}`}
    // },
    
  },
  actions: {
    async updateUser({state}){
      const current_user = JSON.parse(localStorage.getItem('current_user'))
      const user = await axios.get(`${state.server_href}users_mini_info?id=${current_user.id}`, {
        headers: state.headers
      })
      localStorage.setItem('current_user', JSON.stringify(user.data))
    },
    async fetchBrandsIndex({state}){
      const brands = await axios.get(`${state.server_href}brands_index`)
      return brands.data
    },
    async fetchProductsBySaleNewHit({state}, sale_new_hit){
      const products = await axios.get(`${state.server_href}products_index?sale_new_hit=${sale_new_hit}`)
      return products.data
    },
    async fetchProductDetail({state}, product_id){
      const product = await axios.get(`${state.server_href}products/${product_id}`)
      return product.data
    },
    async fetchCategoryProducts({state}, {category_name, product_id}){
      let products;
      if (product_id) {
        products = await axios.get(
          `${state.server_href}category_products/${category_name}?current_product_id=${product_id}`
        )
      }else{
        products = await axios.get(
          `${state.server_href}category_products/${category_name}`
        )
      }
      return products.data
    },
    async fetchCategories({state}, categories_position=false){
      const categories = await axios.get(
        `${state.server_href}categories?categories_position=${categories_position}`
      )
      return categories.data
    },
    async fetchBlogsIndex({state}){
      const blogs = await axios.get(`${state.server_href}blogs_index`)
      return blogs.data
    },
    async fetchBlogs({state}, urlParams){
      const blogs = await axios.get(`${state.server_href}blogs?${urlParams}`)
      return blogs.data
    },
    async fetchBlog({state}, id){
      const blogs = await axios.get(`${state.server_href}blogs/${id}`)
      return blogs.data
    },
    async fetchBlogCategories({state}){
      const categories = await axios.get(`${state.server_href}blog_categories`)
      return categories.data
    },
    async fetchAvailableFilters({state}){
      const filters = await axios.get(`${state.server_href}available_filters`)
      return filters.data
    },
    async fetchFilteredProducts({state}, filtering_url_params){
      const filteredProducts = await axios.get(`${state.server_href}filter_products${filtering_url_params}`)
      return filteredProducts.data
    },
    async commonGETRequestWithAuth({state}, url_after_server_domain){
      if (await cookieStore.get('access')) {
        try{
          const page = await axios.get(state.server_href + url_after_server_domain, {
            headers: await state.headers()
          })
          return page.data
        }catch(err){
          return err
        }
      }else{
        return
      }
    },
    async commonPOSTRequestWithAuth({state}, {url_after_server_domain, post_data}){
      if (await cookieStore.get('access')) {
        try{
          const page = await axios.post(state.server_href + url_after_server_domain, post_data, {
            headers: await state.headers()
          })
          return page.data
        }catch(err){
          return err
        }
      }else{
        return 
      }
    },
  },
  modules: {
  }
})
