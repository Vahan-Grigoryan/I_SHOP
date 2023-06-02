<template>
  <router-view/>
</template>

<script>
import axios from 'axios';

export default {
  async beforeMount(){
    
    if (localStorage.getItem('current_user')) {
      try{
        const access_token = await axios.post(`${this.$store.state.server_href}auth/jwt/refresh`, {
          refresh: localStorage.getItem('refresh')
        })
        localStorage.setItem('access', access_token.data.access)
        this.$store.commit('updateHeaders')
      }catch(error){
        localStorage.clear();
      }
    }
    
    

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
