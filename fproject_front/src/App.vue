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
      // If any page component emit rerender_header 
      //  with arg set_search_text_empty this.search_query = '' (need for leave from filters page), 
      //  else update header page component
      if (key == 'set_search_text_empty') {
        this.search_query = ''
      } else {
        this.header_rerender_key++
      }
    },
    setLeftAndCenterCategory(left_and_center_cats){
      // Need when center category is clicked(on Index, MegaCategory pages for example),
      //  report filters page about it.
      //  Left category need for select(UI component) relevant dropdown menu
      this.center_cat = left_and_center_cats
    }
  },
  updated(){
    // After each center category/brand selected it seted to empty for future center category/brand select
    this.center_cat = ''
    this.brand = '' 
  },
  provide(){
    // search_query, change_brand, change_center_category, change_right_category:
    //  For filters page
    // change_left_category:
    //  For MegaCategory page
    return {
      search_query: computed(() => this.search_query),
      change_brand: computed(() => this.brand),
      change_left_category: computed(() => this.left_cat),
      change_center_category: computed(() => this.center_cat),
      change_right_category: computed(() => this.right_cat),
      
    }
  },
  async beforeMount(){
    // Update access token on each page update 
    //  if refresh token exist and valid, 
    //  if refresh token is invalid delete tokens and user data
    const refresh = localStorage.getItem('refresh')
    if (refresh) {
      try{
        const access_token = await axios.post(`${this.$store.state.server_href}auth/jwt/refresh`, {
          refresh: refresh
        })
        localStorage.setItem('access', access_token.data['access'])
      }catch(error){
        if (error.response.data.code === "token_not_valid"){
          this.$store.getters.delAllDataFromLocalStorage()
        }
        if (this.$route.name === 'profile') this.$router.push('/register');
      }
    }

    // OAuth2
    // If redirected with cookies, transfer cookies to lacalStorage(tokens, user data)
    //  and delete all cookies
    const access = await cookieStore.get('access')
    if (access) {
      this.$store.getters.setTokensInLS({
        access: access.value,
        refresh: (await cookieStore.get('refresh')).value
      })
      await cookieStore.delete('access')
      await cookieStore.delete('refresh')
      let current_user = {}
      for (const iterable of await cookieStore.getAll()){
        if (iterable['name'].startsWith('user_')) {
          current_user[iterable['name'].slice(5)] = iterable.value
          await cookieStore.delete(iterable['name'])
        }
      }
      this.header_rerender_key++
      this.$store.getters.setUserInLS(current_user)
      this.$router.push(`/profile/${current_user.id}`)
    }

  },
  watch: {

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
