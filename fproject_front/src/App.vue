<template>
  <Header 
  v-model:search_text="search_query"
  v-model:left_cat="left_cat"
  v-model:right_cat="right_cat"
  :key="header_rerender_key"
  />
  <!-- <router-view 
  v-if="cat"
  :change_category="cat"
  />
  <router-view 
  v-else-if="search_query.length > 2"
  :search_query="search_query"
  />
  <router-view 
  v-else-if="['register', 'profile'].includes($route.name)"
  @rerender_header="(key) => header_rerender_key = key"
  /> -->
  <RouterView 
  @selectedCenterCategory="setLeftAndCenterCategory"
  @selectedBrand="(brand_name) => brand = brand_name"
  @rerender_header="rerenderHeader"
  />
  
  <ui-footer />
</template>

<script>
import axios from 'axios';
import { computed } from 'vue'


export default {
  data(){
    return {
      search_query: '',
      left_cat: '',
      center_cat: '',
      right_cat: '',
      brand: '',
      header_rerender_key: 0,
    }
  },
  methods: {
    rerenderHeader(key){
      if (key == 'set_search_text_empty') {
        this.search_query = ''
      } else {
        this.header_rerender_key++
      }
    },
    setLeftAndCenterCategory(left_and_center_cats){
      this.center_cat = left_and_center_cats
    }
  },
  updated(){
    this.center_cat = ''
    
  },
  provide(){
    return {
      search_query: computed(() => this.search_query),
      change_brand: computed(() => this.brand),
      change_left_category: computed(() => this.left_cat),
      change_center_category: computed(() => this.center_cat),
      change_right_category: computed(() => this.right_cat),
      
    }
  },
  async beforeMount(){
    // this.$store.getters.delCookie('tokens')
    localStorage.setItem('cats_formated', JSON.stringify(await this.$store.dispatch('fetchCategories')))
    
    if (await cookieStore.get('access')) {
      try{
        const access_token = await axios.post(`${this.$store.state.server_href}auth/jwt/refresh`, {
          refresh: (await cookieStore.get('refresh')).value
        })
        await cookieStore.set('access', access_token.data.access)
        // this.$store.commit('updateHeaders')
      }catch(error){
        if (error.response.data.code === "token_not_valid"){
          await cookieStore.delete('access')
          await cookieStore.delete('refresh')
          await cookieStore.delete('user_id')
          await cookieStore.delete('user_first_name')
          await cookieStore.delete('user_photo')
          await cookieStore.delete('user_liked_products_count')
          await cookieStore.delete('user_ordered_products_count')
        }
        if (this.$route.name === 'profile') this.$router.push('/register');
      }
    }

  },
  watch: {
    center_cat(newValue){
      // console.log(newValue);
    }
  },
  beforeUnmount(){
    localStorage.removeItem('cats_formated')
  }
}
</script>

<style>
*{
  margin: 0px;
  padding: 0px;
  font-family: Arial;
  box-sizing: border-box;
}
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
