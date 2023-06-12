<template>
<div class="write_feedback_modal_wrapper" v-if="write_feedback_visible"></div>
<div class="write_feedback_modal" v-if="write_feedback_visible">
    <img
    src="@/assets/img/clear.png"
    class="auth_modal_close_img"
    @click="write_feedback_visible = false"
    >
    <h2>Напишите свой отзыв о продукте:</h2>
    <input type="text" placeholder="Заголовок*" v-model="comment_header">
    <textarea name="" id="" cols="30" rows="10" placeholder="Текст отзыва*" v-model="comment_text"></textarea>
    <div class="set_starts">
        <span>Ваша оценка:</span>&nbsp;&nbsp;
        <img 
        v-for="star_num in 5"
        src="@/assets/img/star_gray.png"
        :ref="`feedback_star${ star_num }`"
        @mouseenter="setStarsUI(star_num)"
        @mouseleave="delStartsUI"
        @click="setStarsUI(star_num, for_click=true)"
        
        >
    </div>
    <button class="feedback_btn" @click="writeComment">
        <img src="@/assets/img/star_white.png">&nbsp;
        Оставить отзыв
    </button>
</div>

<div class="product_detail_container">
    <ui-bread-crumbs />
    <h1>{{ product.name }}</h1>
    <div class="slider_and_content_flex">
        <div class="left_slider">
            <Splide
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
                    <img :src="product.brand.image" class="brand_logo">
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
                    <img :src="product.brand.image" class="brand_logo">
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
                                        <span class="span_price">{{ product.price }} €</span>
                                        &nbsp; &nbsp;
                                        <span 
                                        class="span_price_del"
                                        v-if="product.saled_price"
                                        >{{ product.saled_price }} €</span>
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
                        :class="getColorClass(color)" 
                        :style="`background: ${color};`"
                        @click="selected_color = color"
                        >
                        </div>
                    </div>
                </div>
                <div class="inline product_prices">
                    <div class="price inline">
                        <h2>{{ product.price }} €</h2> &nbsp; &nbsp;
                        <span v-if="product.saled_price">{{ product.saled_price }} €</span> 
                    </div>
                    <div class="count">
                        <button class="inc_dec_btn" @click="decCount">-</button>
                        <input type="number" v-model="count">
                        <button class="inc_dec_btn" @click="incCount">+</button>

                        <div :class="{
                            disable_message: true,
                            to_shake: count_disable_shake_class
                        }">
                            Махимально доступно {{ product.quantity }}
                        </div>
                    </div>
                </div>
                <br>
                <div class="inline">
                    <button class="buy_btn">
                        <img src="@/assets/img/basket_white.png" alt="">
                        &nbsp;
                        Купить
                    </button>
                    <div class="like_icon">
                        <div class="like"></div>
                    </div>
                    <span>Нравится</span>
                    <div class="compare_icon">
                        <img src="@/assets/img/compare.png" alt="">
                    </div>
                    <span>Добавить к сравению</span>
                </div>
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
                <h1>Владелец продукта не предоставил информацию про характеристики</h1>
            </div>
        </div>
        <div class="about_product_content_feedbacks" v-else-if="tab_active['feedbacks']">
            <div 
            class="about_product_content_feedback"
            v-if="product.comments.length"
            v-for="comment in current_product_comments"
            >
                <h3>{{ comment.comment_header }}</h3>
                <div class="rating">
                    <div class="stars">
                        <img src="@/assets/img/star.png" v-for="_ in comment.stars">
                        <img src="@/assets/img/star_gray.png" v-for="_ in 5-comment.stars">
                    </div>
                </div>
                <span>
                    {{ comment.text }}
                </span>
                <div class="about_product_content_feedback_owner_box">
                    <span class="owner_logo">
                        {{ comment.user.first_name.charAt(0) }}
                    </span>
                    <span>{{ `${comment.user.first_name} ${comment.user.last_name}` }}</span>
                </div>
            </div>
            <div v-else style="text-align: center;">
                <h1 v-if="user">Пока отзывов нет, будь первым!</h1>
                <h2 v-else>Пока отзывов нет, зарегесстрируйся чтобы написать отзыв!</h2>
                <br>
            </div>
            <div class="btns">
                <button 
                v-if="product.comments.length != current_product_comments.length"
                @click="add2comments(current_product_comments.length-1)"
                >Больше отзывов</button>
                &nbsp; &nbsp;
                <button @click="write_feedback_visible = true" v-if="user">Оставить отзыв</button>
            </div>
            
        </div>
    </div>

        
</div>
<ui-href-blog-box 
style="padding: 60px 0% 70px 0%;margin-top: 0px;"
/>


</template>

<script>
import '@splidejs/vue-splide/css/sea-green'
import Splide from '@splidejs/splide'
import emitsForApp from '@/mixins/emitsForApp'


export default {
    data(){
        return{
            user: JSON.parse(localStorage.getItem('current_user')),
            product: {},
            current_product_comments: [],
            similar_products: [],
            count: 1,
            count_disable_shake_class: false,
            tab_active: {
                'desc': true,
                'characterictics': false,
                'feedbacks': false
            },
            write_feedback_visible: false,
            selected_resolution: '',
            selected_color: '',
            stars_mouse_enter_leave_available: true,
            preview_images_visibles: {},
            comment_header: '',
            comment_text: '',
            stars: 0,
        }
    },
    mixins: [emitsForApp],
    methods: {
        getColorClass(color){
            return {
                color: true,
                color_selected: color === this.selected_color
            }
        },
        decCount(){
            this.count > 1 ? this.count-- : null
        },
        incCount(){
            this.count < this.product.quantity ? this.count++ : null
        },
        setStarsUI(star_num, for_click=false){
            if (for_click) {
                this.stars_mouse_enter_leave_available = false
                this.stars = star_num
            }
            else{
                this.stars_mouse_enter_leave_available = true
            }
            Object.keys(this.$refs).forEach(star_ref_key => {
                if (star_ref_key.charAt(13) <= star_num) {
                    this.$refs[star_ref_key][0].src = require('@/assets/img/star.png')
                }
            })
            
        },
        delStartsUI(){
            if (this.stars_mouse_enter_leave_available) {
                Object.keys(this.$refs).forEach(star_ref => {
                    this.$refs[star_ref][0].src = require('@/assets/img/star_gray.png')
                })
            }
            
        },
        setActiveTab(tab_name){
            Object.keys(this.tab_active).forEach( key => this.tab_active[key] = false )
            this.tab_active[tab_name] = true
        },
        add2comments(last_el_index) { 
            const two_comments = this.product.comments.slice(last_el_index+1, last_el_index+3)
            this.current_product_comments.push(...two_comments)
        },
        setSimilarProductPreviewImagesVisible(product_id, value){
            if (this.preview_images_visibles[product_id]) {
                this.preview_images_visibles[product_id]=value
            }
        },
        async getProduct(id){
            this.$router.push(`/products/${id}`)
            this.product = await this.$store.dispatch('fetchProductDetail', id)
            this.product.stars_avg = this.product.stars_avg 
            this.selected_resolution = this.product.get_resolutions[0]
            this.current_product_comments = this.product.comments.slice(0, 2)
            this.similar_products = await this.$store.dispatch('fetchCategoryProducts', {
                category_name: this.product.category,
                product_id: this.product.id
            })
            for (let i = 0; i < this.similar_products.length; i++) {
                if (this.similar_products[i].images.length > 1) {
                    this.preview_images_visibles[this.similar_products[i].id] = 'none'
                }
            }


            const main_splide = new Splide('.main_detail_slider', { 
                speed: 1000,
                rewind: true,
                pagination: false,
                perMove: 1,
            })
            const thumbs_splide = new Splide('.thumbs', { 
                speed: 1000,
                rewind: true,
                perPage: 6,
                pagination: false,
                isNavigation: true,
                perMove: 1,
                gap: 10
            })
            await main_splide.sync(thumbs_splide)
            main_splide.mount()
            thumbs_splide.mount()
        },
        async writeComment(){
            const createComment = await this.$store.dispatch('commonPOSTRequestWithAuth', {
                url_after_server_domain: 'comments',
                post_data: {
                    user_id: this.user.id,
                    product_id: this.$route.params.product_id,
                    header: this.comment_header,
                    text: this.comment_text,
                    stars: this.stars
                }
            })
            this.product.comments.length++
            this.current_product_comments.unshift(createComment)
            this.write_feedback_visible = false
        }
    },

    async beforeMount(){
        await this.getProduct(this.$route.params.product_id)
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Product')
    },
    watch: {
        write_feedback_visible(newValue){
            let [current_scrollX, current_scrollY] = [scrollX, scrollY]
            if (newValue) {
                window.onscroll = function () { window.scrollTo(current_scrollX, current_scrollY); };
                
            } 
            else {
                window.onscroll = function () { window.scrollTo(scrollX, scrollY); };
            }
        },
        count(newValue){
            console.log(newValue);
            if(newValue > this.product.quantity){
                this.count = this.product.quantity
                this.count_disable_shake_class = true
                setTimeout(() => {
                    this.count_disable_shake_class = false
                }, 3000)
            }else if(newValue < 0){
                this.count = 1
            }
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/css/product_detail.css');
</style>