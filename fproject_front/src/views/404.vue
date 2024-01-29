<template>


<div class="container_404">
    <ui-bread-crumbs />
    <br>
    <img class="img_404" src="@/assets/img/404.png" alt="">
    <ui-profile-empty 
    :header="'Упс, страница не найдена ;('"
    :content="'Страница, которую Вы ищете, не существует или она перемещена в другое место. Предлагаем воспользоваться функцией поиска сайта.'"
    :btn_content="'Посмотреть каталог'"
    />
</div>


</template>

<script>
</script>

<style scoped>
    @import url('@/assets/css/404.css');
</style>
