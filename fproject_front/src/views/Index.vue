<template>
    <main>
        <ui-main-top-slider style="width: 70%" />

        
        
        <div class="right_screens">
            <img src="@/assets/img/img_top.png" alt="">
            <img src="@/assets/img/Banner2.png" alt="">
        </div>
    </main>

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
            @click="toFiltersPage(center_category.name)"
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
        
        <ui-slide
        v-for="product in sailed_products"
        :key="product.id"
        :product="product"
        @rerender_header="$emit('rerender_header')"
        >
        </ui-slide>
    </mini-products-slider>

    <div class="get_sales_info_form_box">
        <img src="@/assets/img/sale_kupon.png">
        <img src="@/assets/img/sale_circle.png">
        <div class="form_wrapper" action="">
            <div style="width:80%">
                <h1>Получайте информацию о скидках первыми</h1>
                <span>Оформите подписку на рассылку(без регистрации) и вы будете вкурсе всех наших новых продуктов</span>
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
        
        <ui-slide
        v-for="product in hit_products"
        :key="product.id"
        :product="product"
        @rerender_header="$emit('rerender_header')"
        >
        </ui-slide>
    </mini-products-slider>

    <mini-products-slider style="background: #F4F5F9;">
        <template #header>
            <h1>Новинки</h1>
        </template>
        
        <ui-slide
        v-for="product in new_products"
        :key="product.id"
        :product="product"
        @rerender_header="$emit('rerender_header')"
        >
        </ui-slide>
        

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
    @selectedBrand="brand => $emit('selectedBrand', brand)"
    />

    <ContactUsBox />

    <ui-href-blog-box />

    
    
</template>

<script>
import emitsForApp from '@/mixins/emitsForApp'
import axios from 'axios'

export default {
    data(){
        return {
            likes: [],
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
    mixins: [emitsForApp],
    methods:{
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
            
            
        },
        toFiltersPage(center_category){
            const cats_formated = JSON.parse(localStorage.getItem('cats_formated'))
            for(let [lcat_key, lcat_value] of Object.entries(cats_formated)){
                for(let [ccat_key, ccat_value] of Object.entries(lcat_value).splice(2)){
                    if (ccat_key == center_category) {
                        this.$emit('selectedCenterCategory', `${lcat_key},${ccat_key}`)
                        this.$router.push('/product_filters')
                    }
                }
            }
        }
    },
    async beforeMount(){
        this.center_categories = await this.$store.dispatch('fetchPositionCategories', 'center')
        this.sailed_products = await this.$store.dispatch('fetchProductsBySaleNewHit', 'sale')
        this.new_products = await this.$store.dispatch('fetchProductsBySaleNewHit', 'NEW')
        this.hit_products = await this.$store.dispatch('fetchProductsBySaleNewHit', 'HIT')
        this.brands_index = await this.$store.dispatch('fetchBrandsIndex')

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