<template>


<div class="brands_container">
    <ui-bread-crumbs />
    <h1>Бренды</h1>
</div>

<ui-brands 
:header_have="false" 
:brands="brands.results"
@selectedBrand="brand => $emit('selectedBrand', brand)"
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

<script>
import emitsForApp from '@/mixins/emitsForApp';

export default {
    data(){
        return {
            brands: [],
            current_pagination_page: 1
        }
    },
    methods: {
        async getPaginatedBrands(page){
            this.brands = await this.$store.dispatch('fetchBrands', page)
            this.current_pagination_page = page
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Brands')

        this.brands = await this.$store.dispatch('fetchBrands')
    },
    mixins: [emitsForApp]
}
</script>

<style scoped>
    @import url('@/assets/css/brands.css');
</style>