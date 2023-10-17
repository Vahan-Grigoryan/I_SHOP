<template>
    <Header 
    :key="header_rerender_key"
    />

    <RouterView 
    v-if="$route.name === 'productFilters'"
    @rerender_header="rerenderHeader"
    />
    <RouterView 
    v-else
    />
  
    <ui-footer />
</template>

<script>
import axios from 'axios';
import { computed } from 'vue'


export default {
    data(){
        return {
            header_rerender_key: 0,
        }
    },
    methods: {
        rerenderHeader(){
            this.header_rerender_key++
        },
    },
    async beforeMount(){
        // Update access token on each page update 
        //  if refresh token exist and valid, 
        //  else delete tokens and user data
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
    
        // Set liked products names, ordered products names in vuex liked_products_names state,
        // for slide top right btn valid ui and product detail add_product_to_cart btn valid ui
        const user = JSON.parse(localStorage.getItem('current_user'))
        if (user && this.$route.name !== 'profile') {
        const user_additional_info = await this.$store.dispatch(
            'commonRequestWithAuth', 
            {
            method: 'get',
            url_after_server_domain: `users_profile/${user['id']}`,
            }
        )
        user_additional_info.liked_products.forEach( p => {
            this.$store.commit('pushLikedProduct', p.name)
        })
        if (user_additional_info['orders'].length) {
            const order = user_additional_info['orders'].find(order=>!order.status)
            if (order) {
            const indexInOrders = user_additional_info['orders'].indexOf(order)
            user_additional_info['orders'][indexInOrders]['order_products'].forEach( p => {
                this.$store.commit('pushOrderedProduct', p.name)
            })
            }
        }
         
         
         
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
