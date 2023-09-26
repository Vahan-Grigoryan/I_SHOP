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
@selectedBrand="(brand) => $emit('selectedBrand', brand)"
/>

<mini-products-slider style="padding: 0px;margin: 50px 0px 60px 0px;">
    <template #header>
        <h1>Товары из этой категории</h1>
    </template>

    <ui-slide
    v-for="product in products"
    :key="product.id"
    :product="product"
    @rerender_header="$emit('rerender_header')"
    >
    </ui-slide>
</mini-products-slider>


</template>

<script>
import axios from 'axios';


export default {
    data(){
        return {
            category_children: [],
            brands: [],
            products: [],
        }
    },
    methods: {
        async fetchCategoryChildren(category_name=this.$route.params.category_name){
            // Fetch children categories of pointed category and all products of children categories
            const category_children = await axios.get(`${this.$store.state.server_href}/category_children/${category_name}`)
            for (const category of category_children.data) {
                const children_category_products = await this.$store.dispatch('fetchCategoryProducts', {
                    category_name: category.name
                })
                this.products = [...this.products, ...children_category_products]
            }
            

            return category_children.data
        },
        toFiltersPage(left_category, center_category){
            this.$router.push({ path:'/product_filters', query:{'center_category': `${left_category},${center_category}`} })
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Mega category with subcategories')

        this.category_children = await this.fetchCategoryChildren()
        this.brands = await this.$store.dispatch('fetchBrandsIndex')

    },
    watch: {
        '$route.query.left_category':{
            async handler(newCatgeory){
                this.products = []
                this.category_children = await this.fetchCategoryChildren(newCatgeory)
            }
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/css/mega_category.css');
</style>
