<template>
<Header />

<div class="mega_category_container">
    <ui-bread-crumbs />
    <h1>Детская комната</h1>
    <div class="mega_category_subcategories">
        <div 
        class="mega_category_subcategory"
        v-for="_ in 8"
        >
            <img src="@/assets/img/mega_category_subcat.png" alt="">
            <br><br>
            <span>Детские матрасы</span>
        </div>
    </div>
</div>



<ui-brands />

<mini-products-slider style="padding: 0px;margin: 50px 0px 60px 0px;">
    <template #header>
        <h1>Популярные товары из этой категории</h1>
    </template>
    <SplideSlide 
    class="swiper-slide"
    v-for="_ in 10"
    >
        <div class="sale_hit_new_box">
            -90%
        </div>
        <div class="to_like_box">
            <div class="like"></div>
        </div>
        <img src="@/assets/img/watched_slide_img1.png" alt="">
        <div class="slide_desc">
            <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
            <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка {{ _ }}</p>
            <div class="colors">
                <div class="color" style="background: red;"></div>
                <div class="color" style="background: blue;"></div>
                <div class="color" style="background: yellow;"></div>
                <div class="color" style="background: greenyellow;"></div>
                <div class="color" style="background: teal;"></div>
            </div>
            <div class="delivery_box">
                <img src="@/assets/img/delivery.png" alt="">
                <small>Доставка: 1-2 дня</small>
            </div>
            <div class="rating">
                <div class="stars">
                    <img src="@/assets/img/star.png" class="star" />
                    <img src="@/assets/img/star.png" class="star" />
                    <img src="@/assets/img/star.png" class="star" />
                    <img src="@/assets/img/star_gray.png" class="star" />
                </div>
                <small>&nbsp; 15 отзывов</small>
            </div>
        </div>
    </SplideSlide>
</mini-products-slider>

<ui-footer />
</template>

<script>
export default {
    
}
</script>

<style scoped>
    @import url('@/assets/css/mega_category.css');
</style>