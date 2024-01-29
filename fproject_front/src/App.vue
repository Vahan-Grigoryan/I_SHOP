<template>
    <Header 
    :key="header_rerender_key"
    />

    <RouterView 
    @rerender_header="header_rerender_key++"
    />
  
    <ui-footer />
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ref, onBeforeMount } from 'vue'


const store = useStore()
const router = useRouter()

const header_rerender_key = ref(0)


onBeforeMount(async () => {
    // If redirected with cookies, transfer cookies to lacalStorage(tokens, user data)
    //  and delete all cookies
    const access = await cookieStore.get('access')

    if (!access) return 
    
    store.getters.setTokensInLS({
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
    header_rerender_key.value++
    store.getters.setUserInLS(current_user)
    router.push(`/profile/${current_user.id}`)

})
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
