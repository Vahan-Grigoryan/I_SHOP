<template>
    <div class="bread_crumbs">
        <img src="@/assets/img/Home.svg">
        <div v-for="category in $store.state.pagesInCrumbs">
            <img src="@/assets/img/Vector_28.png" class="right_arrow" alt="">
            <span>{{ category }}</span>
        </div>
    </div>
</template>

<script>
// Component for bread crumbs(below header in each page),
// bread crumbs pages get from $store.state.categoriesInCrambs

</script>

<style scoped>
.bread_crumbs{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    color: #686877;
    line-height: 139.02%;
}
.right_arrow{
    margin: 0px 10px;
}
</style>
