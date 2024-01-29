<template>
<ui-modal
class="write_feedback_modal"
v-model:modal_visible="write_feedback_visible"
>
    <h2>Напишите свой отзыв о продукте:</h2>
    <input
    :style="comment_inputs_styles['header']"
    v-model="comment_header"
    type="text"
    placeholder="Заголовок*"
    >
    <textarea 
    :style="comment_inputs_styles['message']"
    v-model="comment_text"
    cols="30"
    rows="10" 
    placeholder="Текст отзыва*" 
    ></textarea>
    <div class="set_starts">
        <span>Ваша оценка:</span>&nbsp;&nbsp;
        <div v-for="star_num in 5">
            <img
            v-if="star_num <= stars['hovered']"
            src="@/assets/img/star.png"
            @mouseenter="stars['hovered'] = star_num"
            @mouseleave="stars['hovered'] = stars['clicked']"
            @click="stars['clicked'] = star_num"
            >
            <img
            v-else
            src="@/assets/img/star_gray.png"
            @mouseenter="stars['hovered'] = star_num"
            @mouseleave="stars['hovered'] = stars['clicked']"
            @click="stars['clicked'] = star_num"
            >
        </div>
    </div>
    <button class="feedback_btn" @click="writeComment">
        <img src="@/assets/img/star_white.png">&nbsp;
        Оставить отзыв
    </button>
    
</ui-modal>

<div class="product_detail_container">
    <ui-bread-crumbs />
    <h1>{{ product.name }}</h1>
    <div class="slider_and_content_flex">
        <div class="left_slider">
            <Splide
                ref="main_detail_slider"
                class="main_detail_slider"
                :options="{ 
                    speed: 1000,
                    rewind: true,
                    pagination: false,
                    perMove: 1,
                }"
                >
                    <SplideSlide 
                    class="main_detail_slider__slide"
                    v-for="pImg in product.images"
                    >
                        <img :src="pImg.image" alt="">
                    </SplideSlide>

            </Splide>
            <Splide
                ref="thumbs_slider"
                class="thumbs"
                :options="{ 
                    speed: 1000,
                    rewind: true,
                    perPage: 6,
                    pagination: false,
                    isNavigation: true,
                    perMove: 1,
                    gap: 10
                }"
                >
                    <SplideSlide 
                    class="thumb"
                    v-for="pImg in product.images"
                    >
                        <img :src="pImg.image" alt="">
                    </SplideSlide>

            </Splide>
        </div>
        
        <div class="right_content">
            <div class="availability_box">
                <div v-if="product.available">
                    <div style="display: inline-flex;">
                        <div class="inline">
                            <img src="@/assets/img/delivery.png" alt=""> &nbsp; &nbsp;
                            <span>Доставка: &plusmn;{{ product.delivery_days }} дня</span>
                        </div>
                        &nbsp; &nbsp;
                        <div class="inline">
                            <h5>Код товара:</h5> &nbsp; &nbsp;
                            <span>{{ product.code }}</span>
                        </div>
                    </div>
                    <br>
                    <br>
                    <span>
                        <img src="@/assets/img/ok.png" alt=""> &nbsp;
                        Есть в наличии
                    </span>
                    <br>
                    <br>
                    <p>
                        <img 
                        class="star_img"
                        src="@/assets/img/star.png" 
                        v-for="_ in product.stars_avg"
                        >
                        <img 
                        class="star_img"
                        src="@/assets/img/star_gray.png" 
                        v-for="_ in 5-product.stars_avg"
                        >
                        {{ product.comments.length }} отзыва
                    </p>
                    <img :src="product.brand?.image" class="brand_logo">
                </div>
                <div v-else>
                    <div class="inline">
                        <img src="@/assets/img/close_red.png"> &nbsp; &nbsp;
                        <span style="color:red">Товара в настоящее время нет в наличии</span>
                    </div>
                    <br><br>
                    <div class="inline">
                        <h5>Код товара:</h5> &nbsp; &nbsp;
                        <span>{{ product.code }}</span>
                    </div>
                    <img :src="product.brand?.image" class="brand_logo">
                </div>
                
            </div>
            <ui-select
            class="similar_products_select"
            :purpose="'cart_products'"
            v-if="!product.available"
            >
                <template #row_info>
                    <h2>Похожие товары</h2>
                    <img src="@/assets/img/filter_top_arrow.png" alt="">
                </template>
                <template #products>
                    <div class="similar_products">
                        <div 
                        class="similar_product" 
                        v-for="product in similar_products"
                        @click="getProduct(product.id)"
                        >
                            <div 
                            @mouseenter="setSimilarProductPreviewImagesVisible(product.id, 'flex')"
                            @mouseleave="setSimilarProductPreviewImagesVisible(product.id, 'none')"
                            >
                                <img 
                                :src="$store.getters.getImageUrl(product.images[0].image)"
                                class="preview_img"
                                >
                                <div class="images_flex" :style="{display: preview_images_visibles[product.id]}">
                                    <img 
                                    v-for="image in product.images"
                                    :src="$store.getters.getImageUrl(image.image)"
                                    >
                                </div>
                            </div>
                            

                            <div class="similar_product_mini_detail">
                                <h3>{{ product.name }}</h3>
                                <br>
                                <div class="inline">
                                    <div class="inline">
                                        <span class="span_price">{{ product.saled_price || product.price }} €</span>
                                        &nbsp; &nbsp;
                                        <span 
                                        class="span_price_del"
                                        v-if="product.saled_price"
                                        >{{ product.price }} €</span>
                                    </div>
                                    <button 
                                    class="buy_btn"
                                    @click.stop
                                    >
                                        <img src="@/assets/img/basket_white.png" alt="">
                                        &nbsp;
                                        Купить
                                    </button>
                                    <div 
                                    class="like_icon"
                                    @click.stop
                                    >
                                        <div class="like"></div>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </template>
            </ui-select>
            <div class="product_detail_info" v-if="product.available">
                <div style="display: flex;align-items: center;justify-content: space-between;">
                    <h2>Размер:</h2>
                    <ui-select 
                    style="width: 85%;"
                    v-model:selected_option="selected_resolution"
                    :purpose="'detail'"
                    :options="product.get_resolutions"
                    />
                </div>
                <div style="display: flex;align-items: center;justify-content: space-between;">
                    <h2>Цвета:</h2>
                    <div class="colors">
                        <div 
                        v-for="color in product.colors.split(',')"
                        :class="getColorClass(color.trim())" 
                        :style="`background: ${color.trim()};`"
                        @click="selected_color = color.trim()"
                        >
                        </div>
                    </div>
                </div>
                <div class="inline product_prices">
                    <div class="price inline">
                        <h2>{{ product.saled_price || product.price }} €</h2> &nbsp; &nbsp;
                        <span v-if="product.saled_price">{{ product.price }} €</span> 
                    </div>
                    <div class="count">
                        <button class="inc_dec_btn" @click="decCount">-</button>
                        <input type="text" v-model="count">
                        <button class="inc_dec_btn" @click="incCount">+</button>

                        <div :class="{
                            disable_message: true,
                            to_shake: count_disable_shake_class
                        }">
                            Максимально доступно {{ product.quantity }}
                        </div>
                    </div>
                </div>
                <br>
                <div class="inline" v-if="user.id">
                    <button 
                    class="buy_btn"
                    @click="productToOrder"
                    v-if="user.id && !$store.state.ordered_products_names.has(product.name)"
                    >
                        <img src="@/assets/img/basket_white.png">
                        &nbsp;
                        В корзину
                    </button>
                    <button 
                    class="buy_btn"
                    @click="productToOrder"
                    style="background: gray;cursor: default"
                    disabled
                    v-else-if="user.id && $store.state.ordered_products_names.has(product.name)"
                    >
                        Уже в корзине
                    </button>
                    <div 
                    class="like_icon"
                    @click="pushLikedProduct"
                    >
                        <div :class="{
                            like: true,
                            change_purple_permanent: $store.state.liked_products_names.has(product.name)
                        }">
                        </div>
                    </div>
                    <span>Нравится</span>
                    <!-- <div class="compare_icon">
                        <img src="@/assets/img/compare.png">
                    </div>
                    <span>Добавить к сравению</span> -->
                </div>
                <h2 v-else>
                    <br />
                    Зарегестрирyйтесь или войдите чтобы купить или пометить как понравившийся
                </h2>
            </div>
        </div>
    </div>
    <div class="about_product">
        <div class="what_about_product_box">
            <div 
            :class="{
                tab: true,
                tab_active: tab_active['desc']
            }"
            @click="setActiveTab('desc')"
            >Описание товара</div>
            <div 
            :class="{
                tab: true,
                tab_active: tab_active['characterictics']
            }"
            @click="setActiveTab('characterictics')"
            >Характеристики</div>
            <div 
            :class="{
                tab: true,
                tab_active: tab_active['feedbacks']
            }"
            @click="setActiveTab('feedbacks')"
            >Отзывы</div>
        </div>
        <div class="about_product_content_desc" v-if="tab_active['desc']">
            {{ product.desc }}
        </div>
        <div class="about_product_content_characteristics" v-else-if="tab_active['characterictics']">
            <div v-if="product.optional_characteristics">
                <div 
                class="characteristic"
                v-for="[key, value] in Object.entries(product.optional_characteristics)"
                >
                    <h5>{{ key }}:</h5>
                    <span>{{ value }}</span>
                </div>
            </div>
            <div v-else style="text-align: center;">
                <h2>Владелец продукта не предоставил информацию про характеристики</h2>
            </div>
        </div>
        <div class="about_product_content_feedbacks" v-else-if="tab_active['feedbacks']">
            <div 
            class="about_product_content_feedback"
            v-if="current_product_comments.length"
            v-for="comment in current_product_comments"
            >
                <h3>{{ comment.comment_header }}</h3>
                <div class="rating">
                    <div class="stars">
                        <img src="@/assets/img/star.png" v-for="_ in comment.stars">
                        <img src="@/assets/img/star_gray.png" v-for="_ in 5-comment.stars">
                    </div>
                </div>
                <br>
                <h4>{{ comment.header }}</h4>
                <span>
                    {{ comment.text }}
                </span>
                <div class="about_product_content_feedback_owner_box">
                    <img
                    class="comment_profile_image"
                    v-if="comment.user.photo"
                    :src="store.getters.getImageUrl(comment.user.photo)"
                    >
                    <span v-else class="owner_logo">
                        {{ comment.user.first_name.charAt(0) }}
                    </span>
                    <span>{{ `${comment.user.first_name} ${comment.user.last_name}` }}</span>
                </div>
            </div>
            <div v-else style="text-align: center;">
                <h1 v-if="user.id">Пока отзывов нет, будь первым!</h1>
                <h2 v-else>Пока отзывов нет, зарегестрируйся чтобы написать отзыв!</h2>
            </div>
            <div class="btns" v-if="product.comments.length != current_product_comments.length || user.id">
                <button 
                v-if="product.comments.length > current_product_comments.length"
                @click="add2comments(current_product_comments.length-1)"
                >Больше отзывов</button>
                &nbsp; &nbsp;
                <button @click="write_feedback_visible = true" v-if="user.id">Оставить отзыв</button>
            </div>
            
        </div>
    </div>

        
</div>
<ui-href-blog-box 
style="padding: 60px 0% 70px 0%;margin-top: 0px;"
/>


</template>

<script setup>
import '@splidejs/vue-splide/css/sea-green'
import { Splide, SplideSlide } from '@splidejs/vue-splide'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount, watch } from 'vue'


const store = useStore()
const router = useRouter()
const route = useRoute()
const emit = defineEmits()

const user = reactive(JSON.parse(localStorage.getItem('current_user')) || {})
const product = reactive({})
const current_product_comments = reactive([])
const similar_products = reactive([])
const count = ref(1) // product quantity
const count_disable_shake_class = ref(false)
const write_feedback_visible = ref(false)
const selected_resolution = ref('')
const selected_color = ref('')
const preview_images_visibles = reactive({})
const comment_header = ref('')
const comment_text = ref('')
const stars = reactive({
    'hovered': 1,
    'clicked': 1
})
const main_detail_slider = ref(null)
const thumbs_slider = ref(null)
const tab_active = reactive({
    'desc': true,
    'characterictics': false,
    'feedbacks': false
})
const comment_inputs_styles = reactive({
    'header': '',
    'message': ''
})


onBeforeMount(async () => {
    await getProduct(route.params.product_id)
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Product')

    if (user.id) {
        // If user authed, add current product to viewed
        await store.dispatch(
            'commonRequestWithAuth',
            {
                method: 'get',
                url_after_server_domain: `users_add_viewed_product/${user['id']}/${route.params.product_id}`,
            }
        )    
    }

})


watch(
    write_feedback_visible,
    newValue => {
        // If write feedback modal visible block scroll opportunity
        let [current_scrollX, current_scrollY] = [scrollX, scrollY]
        if (newValue) {
            window.onscroll = () => window.scrollTo(current_scrollX, current_scrollY)
         
        } 
        else {
            window.onscroll = () => window.scrollTo(scrollX, scrollY)
        }
    }
)
watch(
    count,
    newValue => {
        // Follow product count and valid it
        if (/\d+/.test(count.value)){
            count.value = Number(/\d+/.exec(count.value)[0])
        } else { count.value = 1 }

        if(newValue > product.quantity){
            count.value = product.quantity
            count_disable_shake_class.value = true
            setTimeout(() => {
                count_disable_shake_class.value = false
            }, 3000)
        }
    }
)


function getColorClass(color){
    // If any product available color clicked wrap in border it
    return {
        color: true,
        color_selected: color === selected_color.value
    }
}
function decCount(){
    count.value > 1 ? count.value-- : null
}
function incCount(){
    count.value < product.quantity ? count.value++ : null
}
function setActiveTab(tab_name){
    // Need for set active tab(desc, characteristics, comments)
    Object.keys(tab_active).forEach( key => tab_active[key] = false )
    tab_active[tab_name] = true
}
function add2comments(last_el_index) { 
    // Add 2 comments in comments list
    const two_comments = product.comments.slice(last_el_index+1, last_el_index+3)
    current_product_comments.push(...two_comments)
}
function setSimilarProductPreviewImagesVisible(product_id, value){
    // Need for show beautiful all images preview on each product in similar products
    if (preview_images_visibles[product_id]) {
        preview_images_visibles[product_id]=value
    }
}
async function getProduct(id){
    // Get product by id and redurect to relevant route path,
    // auto-select first resolution, first_color
    // get firts comment pairs,
    // get similar products if product not available
    router.push(`/products/${id}`)
    Object.assign(product, await store.dispatch('fetchProduct', id))
    product.stars_avg = product.stars_avg 
    selected_resolution.value = product.get_resolutions[0]
    selected_color.value = product.colors.split(',')[0].trim()
    current_product_comments.splice(
        0,
        2,
        ...product.comments.slice(0, 2)
    )
    if (!product.available) {
        const receive_similar_products = await store.dispatch(
            'fetchCategoryProducts',
            {
                category_name: product.category,
                product_id: product.id
            }
        )
        similar_products.push(...receive_similar_products)

        // If product(in similar products have only 1 image left menu not show)
        for (let i = 0; i < similar_products.length; i++) {
            if (similar_products[i].images.length > 1) {
                preview_images_visibles[similar_products[i].id] = 'none'
            }
        }
    }

    await main_detail_slider.value.splide.sync(thumbs_slider.value.splide)
}
async function writeComment(){
    // Create comment if valid fields provided else show relevant UI,
    // add created comment top,
    // comment creation modal close,
    // set all inputs empty

    let error_occured = false
    if (!comment_header.value.trim()){
        comment_inputs_styles['header'] = 'border: 2px solid red'
        error_occured = true
    } 
    if (!comment_text.value.trim()){
        comment_inputs_styles['message'] = 'border: 2px solid red'
        error_occured = true
    }
    if (error_occured){
        setTimeout(()=>{
            comment_inputs_styles['header'] = ''
            comment_inputs_styles['message'] = ''
        }, 4000)

        return
    }

    const createComment = await store.dispatch(
        'commonRequestWithAuth',
        {
            method: 'post',
            url_after_server_domain: `comments`,
            data: {
                user_id: user.id,
                product_id: route.params.product_id,
                header: comment_header.value,
                text: comment_text.value,
                stars: stars['clicked']
            }
        }
    )

    current_product_comments.unshift(createComment)
    write_feedback_visible.value = false
    comment_header.value = ''
    comment_text.value = ''
    stars.value = 1
}
async function pushLikedProduct(){
    if (store.state.liked_products_names.has(product.name)) return
    await store.dispatch(
        'commonRequestWithAuth',
        {
            method: 'get',
            url_after_server_domain: `users_add_or_del_liked_product/${user['id']}/${product['id']}`,
        }
    )
    store.commit('pushLikedProduct', product.name)
    
}
async function productToOrder(){
    // Add product in order with status pending, change vuex relevant state
    await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'post',
            url_after_server_domain: `users_add_or_del_order_product/${user['id']}/${product['id']}`,
            data: {
                quantity: count.value,
                color: selected_color.value,
                resolution: selected_resolution.value,
            }
        }
    )
    store.commit('pushOrderedProduct', product.name)
}

</script>

<style scoped>
    @import url('@/assets/css/product_detail.css');
</style>
