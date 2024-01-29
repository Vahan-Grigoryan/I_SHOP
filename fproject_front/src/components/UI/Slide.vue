<template>
<SplideSlide 
class="swiper-slide"
@click="$router.push(`/products/${product.id}`)"
>
    <ui-detect-salenewhit 
    :sale_new_hit="product.sale_new_hit"
    />
    <div 
    class="to_like_box"
    v-if="top_right_btn_purpose === 'like' && user"
    @click="addLikedProduct"
    >
        <div :class="{
            like: true,
            change_purple_permanent: $store.state.liked_products_names.has(product.name)
        }">
        </div>
    </div>
    <div 
    class="to_like_box"
    v-else-if="top_right_btn_purpose === 'delete'"
    @click="delLikedProduct"
    >
        <img src="@/assets/img/trash.png">
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

<script setup>
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'


const store = useStore()
const route = useRoute()
const emit = defineEmits()
const props = defineProps({
    product: Object,
    top_right_btn_purpose: {
        type: String,
        default: 'like'
    },
})

const user = JSON.parse(localStorage.getItem('current_user'))


async function addLikedProduct(e){
    // Add user liked product name in store state liked_products_names for valid like button ui.
    // If user on profile page, emit event for auto update liked products list
    e.stopPropagation()
    if (route.name === 'profile') {
        emit('add_liked_product', props.product)
    }
    
    await store.dispatch(
        'commonRequestWithAuth',
        {
            method: 'get',
            url_after_server_domain: `users_add_or_del_liked_product/${user?.id}/${props.product['id']}`,
        }
    )
    store.commit('pushLikedProduct', props.product.name)
}
async function delLikedProduct(e){
    // Remove user liked product.
    // If user on profile page auto update liked products list
    e.stopPropagation()
    
    store.commit('delLikedProduct', props.product.name)
    await store.dispatch(
        'commonRequestWithAuth',
        {
            method: 'delete',
            url_after_server_domain: `users_add_or_del_liked_product/${user?.id}/${props.product['id']}`,
        }
    )
    emit('del_liked_product', props.product)
}
</script>

<style scoped>
</style>
