<template>
<div class="brands_container">
    <ui-bread-crumbs />
    <h1>Бренды</h1>
</div>

<ui-brands 
:header_have="false" 
:brands="brands.results"
>
    <template #pagination_or_href>
        <ui-pagination
        :pages="$store.getters.calculatePagesCount(brands.count, 6)"
        @paginated_to="getPaginatedBrands"
        v-model:page_active="current_pagination_page"
        />
    </template>
</ui-brands>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount } from 'vue'


const store = useStore()
const route = useRoute()

const brands = reactive({})
const current_pagination_page = ref(1)


onBeforeMount(async () => {
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Brands')

    Object.assign(brands, await store.dispatch('fetchBrands'))
})


async function getPaginatedBrands(page){
    Object.assign(brands, await store.dispatch('fetchBrands', page))
    current_pagination_page.value = page
}

</script>

<style scoped>
    @import url('@/assets/css/brands.css');
</style>
