<template>
    <Header 
    v-model:likes="likes.length" 
    />

    <main>
        <ui-main-top-slider style="width: 70%" />

        
        
        <div class="right_screens">
            <img src="@/assets/img/img_top.png" alt="">
            <img src="@/assets/img/Banner2.png" alt="">
        </div>
    </main>
    
    <!-- <div class="main_bottom_slider">
        <ui-main-bottom-slider />
    </div> -->

    <mini-products-slider 
    class="main_bottom_slider"
    
    >
        <SplideSlide>
            <img src="@/assets/img/main_bottom_slide1.png" alt="">
        </SplideSlide>
        <SplideSlide>
            <img src="@/assets/img/Banner1.png" alt="">
        </SplideSlide>
        <SplideSlide>
            <img src="@/assets/img/main_bottom_slide3.png" alt="">
        </SplideSlide>
        <SplideSlide>
            <img src="@/assets/img/main_bottom_slide4.png" alt="">
        </SplideSlide>
        <SplideSlide>
            <img src="@/assets/img/main_bottom_slide2.png" alt="">
        </SplideSlide>
    </mini-products-slider>
    
    <ui-our-procs />

    <div class="variety_of_products">
        <h1>Широкий ассортимент товаров</h1><br>
        <span>для малышей и мам</span>
        <div class="for_grid">
            <div 
            class="category_box" 
            v-for="center_category in center_categories"
            @click="$router.push('to_filters!!!')"
            >
                <img :src="$store.getters.getImageUrl(center_category.image)"><br>
                <span>{{ center_category.name }}</span>
            </div>
        </div>
    </div>
    
    <mini-products-slider>
        <template #header>
            <h1>Акции и скидки</h1>
        </template>
        
        <SplideSlide 
        class="swiper-slide"
        v-for="product in sailed_products"
        :key="product.id"
        @click="$router.push(`products/${product.id}`)"
        >
            <div :class="defineSaleNewHit('sale')">
                {{ product.sale_new_hit.slice(4) }}%
            </div>
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img :src="product.images[0].image">
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

    </mini-products-slider>

    <div class="get_sales_info_form_box">
        <img src="@/assets/img/sale_kupon.png">
        <img src="@/assets/img/sale_circle.png">
        <div class="form_wrapper" action="">
            <div style="width:80%">
                <h1>Получайте информацию о скидках первыми</h1>
                <span>Оформите подписку и вы будете вкурсе всех наших выгодных акций и скидок</span>
                <form @submit.prevent method="post">
                    <div style="width: 45%;position: relative;">
                        <input ref="mail_to_mailing_list" type="email" placeholder="Ваша электронная почта" />
                        <div 
                        v-if="mailing_list_response" 
                        :class="{
                            response_msg: true,
                            response_msg_invalid: mailing_list_response_invalid,
                            response_msg_valid: mailing_list_response_valid
                        }"
                        >
                            {{ mailing_list_response }}
                        </div>
                    </div>
                    <button @click="subscribeMailingList">
                        <strong>&#10003; Оформить подписку</strong>
                    </button>
                    <button @click="unsubscribe">
                        <strong>&#10005; Отказатся от подписки</strong>
                    </button>
                </form>
            </div>
            
        </div>
        <img class="right_girl" src="@/assets/img/form_right_girl.png" alt="">
    </div>

    <mini-products-slider>
        <template #header>
            <h1>Популярные товары</h1>
        </template>
        
        <SplideSlide 
        class="swiper-slide"
        v-for="product in hit_products"
        :key="product.id"
        @click="$router.push(`products/${product.id}`)"
        >
            <div :class="defineSaleNewHit('hit')">
                {{ product.sale_new_hit }}
            </div>
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img :src="product.images[0].image">
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
    </mini-products-slider>

    <mini-products-slider style="background: #F4F5F9;">
        <template #header>
            <h1>Новинки</h1>
        </template>
        
        <SplideSlide 
        class="swiper-slide"
        v-for="product in new_products"
        :key="product.id"
        @click="$router.push(`products/${product.id}`)"
        >
            <div :class="defineSaleNewHit('new')">
                {{ product.sale_new_hit }}
            </div>
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img :src="product.images[0].image">
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
        

    </mini-products-slider>

    <div class="about_us">
        <div class="content">
            <div class="in_line">
                <h1>О нас</h1> 
                <img src="@/assets/img/Logo2.png" alt=""> 
            </div>
            <p>
                <strong>Bērnu veikals</strong> — это огромный интернет-магазин для малышей и их родителей.
                Для нас главный приоритет — это комфорт и безопасность для Вас и Ваших драгоценных крошек ♥.
                Наш интернет-магазин всегда под рукой и Вы в любое время суток можете заказывать товары,
                которые мы наиболее быстрым и удобным для Вас способом доставим по всей территории Балтии.
                Bērnu Veikals обеспечивает большим выбором товаров наилучшего качества по доступным ценам,
                мы заботимся не только о качестве, но и о вашем кошельке 👛.
            </p>
            <strong class="read_detail" @click="$router.push('/about')">
                Читать подробнее &nbsp; &nbsp; 
                <img src="@/assets/img/arrow_5.png" alt="">
            </strong>
        </div>
        <div class="images_box">
            <img src="@/assets/img/portrait-pretty-mother-with-shopping-package-walking-with-baby-carriage-incity-center_1.png" alt="">
        </div>
    </div>

    <ui-brands 
    :brands="brands_index"
    />

    <ContactUsBox />

    <ui-href-blog-box />

    <ui-footer />
    
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            likes: [],
            likesPurpleStatus: new Proxy({}, {
                get: function(target, name) {
                    return name in target ? target[name] : false
                }
            }),
            center_categories: [],
            sailed_products: [],
            hit_products: [],
            new_products: [],
            brands_index: [],
            mailing_list_response: '',
            mailing_list_response_valid: false,
            mailing_list_response_invalid: false,
            
        }
    },
    methods:{
        addOrDelLikes(product_id){
            // if (this.likes.includes(product_id)) {
            //     this.likes = this.likes.filter( id => id != product_id)
            //     delete this.likesPurpleStatus[product_id]
            // } 
            // else {
            //     this.likes.push(product_id)
            //     this.likesPurpleStatus[product_id] = product_id
            // }
        },
        defineSaleNewHit(productSaleNewHit){
            const definition = {
                sale: {sale_hit_new_box50: true},
                new: {sale_hit_new_boxnew: true},
                hit: {sale_hit_new_boxhit: true},
            } 
            return definition[productSaleNewHit]
        },
        check_mailing_list_response(response){
            if(response.data['Error']){
                this.mailing_list_response_invalid = true
                this.mailing_list_response = response.data['Error']
                setTimeout(() => {
                    this.mailing_list_response_invalid = false
                    this.mailing_list_response = ''
                }, 4000);
            }
            else if(response.data['Message']){
                this.mailing_list_response_valid = true
                this.mailing_list_response = 'Loading...'
                this.mailing_list_response = response.data['Message']
                setTimeout(() => {
                    this.mailing_list_response_valid = false
                    this.mailing_list_response = ''
                }, 4000);
            }
        },
        async subscribeMailingList(){
            let mail = await this.$refs.mail_to_mailing_list.value.trim()
            if (mail) {
                const response = await axios.post(`${this.$store.state.server_href}mailing_list`, {mail:mail})
                this.check_mailing_list_response(response)
            }
            
            
            
        },
        async unsubscribe(){
            let mail = await this.$refs.mail_to_mailing_list.value.trim()
            if (mail) {
                const response = await axios.post(`${this.$store.state.server_href}mailing_list`, {mail:mail, for_delete:true})
                this.check_mailing_list_response(response)
            }
            
            
        }
    },
    async beforeMount(){
        this.center_categories = await this.$store.getters.fetchCategories('center')
        this.sailed_products = await this.$store.getters.fetchProductsBySaleNewHit('sale')
        this.new_products = await this.$store.getters.fetchProductsBySaleNewHit('NEW')
        this.hit_products = await this.$store.getters.fetchProductsBySaleNewHit('HIT')
        this.brands_index = await this.$store.getters.fetchBrandsIndex()

        function setProductsStarsAvg(products) {
            for (let i = 0; i < products.length; i++) {
                products[i].stars_avg = products[i].stars_avg
            }
        }

        setProductsStarsAvg(this.sailed_products)
        setProductsStarsAvg(this.new_products)
        

    },
    async beforeCreate(){
        // let params = new URLSearchParams(document.location.search);
        // if (params.size) {
        //     const [state, code] = [params.get('state'), params.get('code')] 
        //     console.log(state, code);
        //     const auth = await axios.post(
        //     `${this.$store.state.server_href}/auth/o/google-oauth2/?state=${state}&code=${code}`,
        //     {
        //         headers: {
        //             'Content-Type': 'application/x-www-form-urlencoded'
        //         }
        //     })
        //     console.log(auth.data);
        // }
    }
}
</script>

<style>
    @import url("@/assets/css/index.css");
</style>