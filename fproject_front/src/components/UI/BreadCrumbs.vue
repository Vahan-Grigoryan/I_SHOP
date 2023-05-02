<template>
    <div class="bread_crumbs">
        <img src="@/assets/img/Home.svg" alt="">
        <div v-for="category in $store.state.categoriesInCrambs">
            <img src="@/assets/img/Vector_28.png" class="right_arrow" alt="">
            <span>{{ category }}</span>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ui-bread-crumbs',
}
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