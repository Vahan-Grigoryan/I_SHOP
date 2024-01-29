<template>
<div class="mega_category_container">
    <ui-bread-crumbs />
    <h1>{{ $route.params.category_name }}</h1>
    <div class="mega_category_subcategories">
        <div 
        class="mega_category_subcategory"
        v-for="child_category in category_children"
        @click="toFiltersPage($route.params.category_name, child_category.name)"
        >
            <img :src="$store.getters.getImageUrl(child_category.image)">
            <br><br>
            <span>{{ child_category.name }}</span>
        </div>
    </div>
</div>

<ui-brands 
:brands="brands"
/>

<mini-products-slider style="padding: 0px;margin: 50px 0px 60px 0px;">
    <template #header>
        <h1>Товары из этой категории</h1>
    </template>

    <ui-slide
    v-for="product in products"
    :key="product.id"
    :product="product"
    >
    </ui-slide>
</mini-products-slider>


</template>

<script setup>
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { reactive, onBeforeMount, watch } from 'vue'


const store = useStore()
const route = useRoute()
const router = useRouter()

const category_children = reactive([])
const brands = reactive([])
const products = reactive([])


onBeforeMount(async () => {
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Mega category with subcategories')

    category_children.push(...await fetchCategoryChildren())
    brands.push(...await store.dispatch('fetchBrandsIndex'))
})


watch(
    () => route.query.left_category,
    async newCatgeory => {
        products.splice(0, products.length)
        category_children.splice(
            0,
            category_children.length,
            ...await fetchCategoryChildren(newCatgeory)
        )
    }
)


async function fetchCategoryChildren(category_name=route.params.category_name){
    // Fetch children categories of pointed category and all products of children categories
    const category_children = await axios.get(`${store.state.server_href}/category_children/${category_name}`)
    for (const category of category_children.data) {
        const children_category_products = await store.dispatch('fetchCategoryProducts', {
            category_name: category.name
        })
        products.push(...children_category_products)
    }
    

    return category_children.data
}
function toFiltersPage(left_category, center_category){
    router.push({ path:'/product_filters', query: {'center_category': `${left_category},${center_category}`} })
}

</script>

<style scoped>
    @import url('@/assets/css/mega_category.css');
</style>
