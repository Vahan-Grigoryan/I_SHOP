<template>
<Header />

<div class="compare_container">
    <ui-bread-crumbs />

    <div class="compare_logo_box">
        <img src="@/assets/img/compare_big.png" alt="">
        <h2>Сравнение товаров</h2>
        <span>(показываются только отличия)</span>
        <div class="clear_all_products">
            <img src="@/assets/img/clear.png" alt=""> &nbsp;
            <span>Очистить все</span>
        </div>
    </div>
    <br>
    <Splide 
    ref="splide"
    style="padding: 30px 0px;"
    :options="{
        rewind:true,
        perPage:4,
        speed: 1000,
        pagination: false,
        gap: 20,
        arrows: false,
    }"
    @splide:move="splideMoved"
    >
        <SplideSlide 
        class="swiper-slide"
        v-for="num in 10"
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
                <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка {{ num }}</p>
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


        
    </Splide>

    <div class="progressbar" ref="pbar">
        <div class="bar"></div>
    </div>

    <h1>Характеристики</h1>

    
    <div class="products_differences">
        <div class="product_diff">

        </div>
    </div>

</div>

<ui-footer />
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import Splide from '@splidejs/splide'


export default defineComponent({
    setup() {
        const splide = ref();


        onMounted( () => {
            const end  = splide.value.splide.Components.Controller.getEnd() + 1;
            const pbar = document.querySelector('.progressbar')
            const bar = document.querySelector('.bar')
            bar.style.width = `${bar.offsetWidth / end}px`

        } );
        
        function splideMoved() {
            const splide1_instance = splide.value.splide
            const current_splide_i = splide1_instance.index
            const pbar = document.querySelector('.progressbar')
            const bar = document.querySelector('.bar')
            const end  = splide1_instance.Components.Controller.getEnd() + 1;
            bar.style.transform = `translateX(${current_splide_i*(pbar.offsetWidth / end)}px)`;

        }
        
        return {
            splide,
            splideMoved,
        }
    },

})
</script>

<style scoped>
    @import url('@/assets/css/compare_products.css');
</style>