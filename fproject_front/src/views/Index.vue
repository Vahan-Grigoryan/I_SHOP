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
        >
        </ui-slide>
    </mini-products-slider>

    <div class="get_sales_info_form_box">
        <img src="@/assets/img/sale_kupon.png">
        <img src="@/assets/img/sale_circle.png">
        <div class="form_wrapper" action="">
            <div style="width:80%">
                <h1>Получайте информацию о скидках первыми</h1>
                <span>Оформите подписку на рассылку(можно без регистрации) и вы будете вкурсе всех наших новых продуктов</span>
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
    />

    <ContactUsBox />

    <ui-href-blog-box />

    
    
</template>

<script setup>
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount } from 'vue'


const store = useStore()
const router = useRouter()

const center_categories = reactive([])
const sailed_products = reactive([])
const hit_products = reactive([])
const new_products = reactive([])
const brands_index = reactive([])
const mailing_list_response = ref('')
const mailing_list_response_valid = ref(false)
const mailing_list_response_invalid = ref(false)
const mail_to_mailing_list = ref(null)


onBeforeMount(async () => {
    center_categories.push(...await store.dispatch('fetchPositionCategories', 'center'))
    sailed_products.push(...await store.dispatch('fetchProductsBySaleNewHit', 'sale'))
    new_products.push(...await store.dispatch('fetchProductsBySaleNewHit', 'NEW'))
    hit_products.push(...await store.dispatch('fetchProductsBySaleNewHit', 'HIT'))
    brands_index.push(...await store.dispatch('fetchBrandsIndex'))
})


function check_mailing_list_response(response){
    if(response.data['Error']){
        mailing_list_response_invalid.value = true
        mailing_list_response.value = response.data['Error']
        setTimeout(() => {
            mailing_list_response_invalid.value = false
            mailing_list_response.value = ''
        }, 4000);
    }
    else if(response.data['Message']){
        mailing_list_response_valid.value = true
        mailing_list_response.value = 'Loading...'
        mailing_list_response.value = response.data['Message']
        setTimeout(() => {
            mailing_list_response_valid.value = false
            mailing_list_response.value = ''
        }, 4000)
    }
}
function invalid_email_ui(){
    mail_to_mailing_list.value.style = "border: 2px solid red"
    setTimeout(()=>{
        // Validation below used to avoid error when user
        // after submit with empty email try go to other page 
        if (mail_to_mailing_list.value) mail_to_mailing_list.value.style = ""
    }, 4000)
}
async function subscribeMailingList(){
    const mail = mail_to_mailing_list.value.value.trim()
    if (!mail) {
        invalid_email_ui()
        return
    }

    const response = await axios.post(`${store.state.server_href}mailing_list`, {mail:mail})
    check_mailing_list_response(response)
}
async function unsubscribe(){
    const mail = mail_to_mailing_list.value.value.trim()
    if (!mail) {
        invalid_email_ui()
        return
    }
    
    const response = await axios.post(`${store.state.server_href}mailing_list`, {mail:mail, for_delete:true})
    check_mailing_list_response(response)
}
function toFiltersPage(center_category){
    // find center cat in localStorage cats_formated and redirect to
    // filters page with center cat name and parent cat name 
    const cats_formated = JSON.parse(localStorage.getItem('cats_formated'))
    for(const [lcat_key, lcat_value] of Object.entries(cats_formated)){
        if (Object.keys(lcat_value).find( el => el==center_category )) {
            router.push({ path:'/product_filters', query:{'center_category': `${lcat_key},${center_category}`} })
            break
        }
    }
}


</script>

<style>
    @import url("@/assets/css/index.css");
</style>
