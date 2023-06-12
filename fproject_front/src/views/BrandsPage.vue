<template>


<div class="brands_container">
    <ui-bread-crumbs />
    <h1>Бренды</h1>
</div>

<ui-brands :header_have="false" >
    <template #pagination_or_href>
        <ui-pagination 
        :pages_per_view="10"
        />
    </template>
</ui-brands>


</template>

<script>
import emitsForApp from '@/mixins/emitsForApp';

export default {
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Brands')
    },
    mixins: [emitsForApp]
}
</script>

<style scoped>
    @import url('@/assets/css/brands.css');
</style>