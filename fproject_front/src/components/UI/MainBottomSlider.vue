<template>
    <swiper 
        :modules="modules"
        :slides-per-view="4"
        :space-between="10"
        :loop="true"
        :grab-cursor="true"
        :resistance="false"
        :speed="700"
        :navigation="{
            nextEl: '.main_bottom_slider_next',
            prevEl: '.main_bottom_slider_prev',
        }"
        
        
    >
        <swiper-slide>
            <img src="@/assets/img/main_bottom_slide1.png" alt="">
        </swiper-slide>
        <swiper-slide>
            <img src="@/assets/img/Banner1.png" alt="">
        </swiper-slide>
        <swiper-slide>
            <img src="@/assets/img/main_bottom_slide3.png" alt="">
        </swiper-slide>
        <swiper-slide>
            <img src="@/assets/img/main_bottom_slide4.png" alt="">
        </swiper-slide>
        <swiper-slide>
            <img src="@/assets/img/main_bottom_slide2.png" alt="">
        </swiper-slide>
        
    </swiper>
    <div class="main_bottom_prev swiper-button-prev main_bottom_slider_prev"></div>
    <div class="main_bottom_next swiper-button-next main_bottom_slider_next"></div>

</template>

<script>
import { Navigation } from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/navigation';


export default {
    name: 'ui-main-bottom-slider',
    components: {
      Swiper,
      SwiperSlide,
    },
    data(){
        return {
            modules: [Navigation]
        }
    },
    
}
</script>

<style scoped>

.main_bottom_slider > .main_bottom_prev {
  left: 5%;
  top: 147px;
}

.main_bottom_slider > .main_bottom_next {
  right: 5%;
  top: 147px;
}
.swiper-button-prev:after, .swiper-button-next:after {
  color: #B7B8C5;
  font-size: 25px;
}
.swiper .swiper-button-prev:after, .swiper .swiper-button-next:after {
  color: #B7B8C5;
  font-size: 30px;
}

.main_bottom_slider .swiper {
  width: 95%;
}

.main_bottom_slider .swiper-wrapper {
  min-width: 100%;
  min-height: 100%;
}

.main_bottom_slider .swiper-slide > img {
  height: 215px;
  width: 100%;
  object-fit: cover;
  border-radius: 7px;
}

</style>