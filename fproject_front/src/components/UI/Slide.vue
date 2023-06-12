<template>
<SplideSlide 
class="swiper-slide"
@click="$router.push(`/products/${product.id}`)"
>
    <ui-detect-salenewhit 
    :sale_new_hit="product.sale_new_hit"
    />
    <div class="to_like_box">
        <div class="like"></div>
    </div>
    <img :src="$store.getters.getImageUrl(product.images[0].image)">
    <div class="slide_desc">
        <h3>{{ product.saled_price ? product.saled_price : product.price }} &dollar;</h3> &nbsp; 
        <span v-if="product.saled_price">{{ product.price }} &dollar;</span>
        <br><br>
        <p>{{ product.name }}</p>
        <div class="colors">
            <div 
            class="color" 
            v-for="color in product.colors.split(',')"
            :style="`background: ${color};`"
            >
            </div>
        </div>
        <div class="delivery_box">
            <img src="@/assets/img/delivery.png" alt="">
            <small>Доставка: &plusmn; {{ product.delivery_days }} дня</small>
        </div>
        <div class="rating">
            <div class="stars">
                <img 
                src="@/assets/img/star.png" 
                class="star" 
                v-for="_ in product.stars_avg"
                />
                <img 
                src="@/assets/img/star_gray.png" 
                class="star" 
                v-for="_ in 5-product.stars_avg"
                />
            </div>
            <small>&nbsp; отзывы: {{ product.comments_count }}</small>
        </div>
    </div>
</SplideSlide>
</template>

<script>
export default {
    name: 'ui-slide',
    props: {
        product: Object
    },
    methods: {
        
    }
}
</script>

<style scoped>

</style>