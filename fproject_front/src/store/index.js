import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    pagesInCrumbs: new Set(),
    profile_content: 'orders',
    server_href: 'http://localhost:8000/',
    liked_products_names: new Set(),
    ordered_products_names: new Set(),
  },
  getters: {
    getImageUrl: state => after_server_domain => {
      // after_server_domain = raw image url(user photo)
      // after treatment give ready image url 
      const image_url = after_server_domain.at(0) === '"' ? after_server_domain.slice(1, -1) : after_server_domain
      if (image_url.includes('http') || image_url.includes('https')) {
        return image_url
      }
      else if (!image_url.includes('media')) {
        return state.server_href + 'media/' + image_url
      } else {
        return state.server_href + image_url.slice(1)
      }
    },
    setTokensInLS: state => tokens => {

      localStorage.setItem('access', tokens['access'])
      localStorage.setItem('refresh', tokens['refresh'])
    },
    setUserInLS: state => user => {
      localStorage.setItem('current_user', JSON.stringify(user))
    },
    delAllDataFromLocalStorage: state => () => {
      // Del all local data about user
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('current_user')
      state.liked_products_names = new Set()
      state.ordered_products_names = new Set()
    },
    calculatePagesCount: state => (count, entities_per_view=4) => {
      return Math.ceil(count/entities_per_view)
    }
  },
  mutations: {
    setProfileContent(state, profile_content_value){
      // Set /prifile/:id page content by profile_content_value, choises are:
      //  orders, liked, sales, register
      state.profile_content = profile_content_value
    },
    pushLikedProduct(state, product_name){
      state.liked_products_names.add(product_name)
    },
    delLikedProduct(state, product_name){
      state.liked_products_names.delete(product_name)
    },
    pushOrderedProduct(state, product_name){
      state.ordered_products_names.add(product_name)
    },
    delOrderedProduct(state, product_name){
      state.ordered_products_names.delete(product_name)
    },
  },
  actions: {
    async fetchBrandsIndex({state}){
      // Brands for index page brands part - 12 brands
      const brands = await axios.get(`${state.server_href}brands_index`)
      return brands.data
    },
    async fetchBrands({state}, pg=1){
      // Brands for brands page
      const brands = await axios.get(`${state.server_href}brands?pg=${pg}`)
      return brands.data
    },
    async fetchProductsBySaleNewHit({state}, sale_new_hit){
      // Filter products by sale_new_hit
      const products = await axios.get(`${state.server_href}products_index?sale_new_hit=${sale_new_hit}`)
      return products.data
    },
    async fetchProduct({state}, product_id){

      const product = await axios.get(`${state.server_href}products/${product_id}`)
      return product.data
    },
    async fetchCategoryProducts({state}, {category_name, product_id}){
      // Return products of category, if product_id pointed exclude it from products
      // Used in pages: mega_category, product_detail
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
    async fetchPositionCategories({state}, categories_position='center'){
      // Return formated categories(for header) or only center categories(for index)
      const categories = await axios.get(
        `${state.server_href}categories?categories_position=${categories_position}`
      )
      return categories.data
    },
    async fetchBlogsIndex({state}){
      // Blogs for blogs slide - 6 blogs
      const blogs = await axios.get(`${state.server_href}blogs_index`)
      return blogs.data
    },
    async fetchBlogs({state}, urlParams){
      // Blogs for blog page with few filtering opportunity
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
      // Get available filters for filters page(brands, colors)
      const filters = await axios.get(`${state.server_href}available_filters`)
      return filters.data
    },
    async fetchFilteredProducts({state}, filtering_url_params){
      // Filter products
      const filteredProducts = await axios.get(`${state.server_href}filter_products${filtering_url_params}`)
      return filteredProducts.data
    },
    async fetchOrGetCategories({state}){
      // If cats_formated(in LS) exist return it else fetch formated categories, write in LS and return it
      const catsLS = localStorage.getItem('cats_formated')
      if (catsLS) {
        return JSON.parse(catsLS)
      } else {
        const categories = await axios.get(
          `${state.server_href}categories`
        )
        localStorage.setItem('cats_formated', JSON.stringify(categories.data))
        return categories.data
      }
      
    },
    async commonRequestWithAuth({state}, {method, url_after_server_domain, data}){
      // Request structure with auth based on localStorage.getItem('access')
      const access_for_request = localStorage.getItem('access')

      if (access_for_request) {
        try{
          const response = await axios({
            method: method,
            url: state.server_href + url_after_server_domain,
            data: data,
            headers: {'Authorization': `JWT ${access_for_request}`}
          });
          return response.data
        }catch(err){
          return err
        }
      }else{
        return 
      }

    }
  },
  modules: {
  }
})
