<template>
<swiper 

  :modules="modules"
  :loop="true"
  :grab-cursor="true"
  :resistance="false"
  :speed="700"
  :autoplay="{delay: 5000}"
  :slides-per-view="slidesPerView"
  :pagination="{
    clickable: true,
  }"
  :navigation="{
    nextEl: '.main_bottom_next',
    prevEl: '.main_bottom_prev',
  }"
  effect="coverflow"
  

>

  <slot>
    <swiper-slide>
      <img src="@/assets/img/Banner1.png" alt="">
    </swiper-slide>
    <swiper-slide>
      <img src="@/assets/img/toys.webp" alt="">
    </swiper-slide>
    <swiper-slide>
      <img src="@/assets/img/toys2.webp" alt="">
    </swiper-slide>
    <div class="main_bottom_prev swiper-button-prev"></div>
    <div class="main_bottom_next swiper-button-next"></div>
  </slot>
    
</swiper>
</template>

<script>
// First slider from top in Index page, 
// didn't use anywhere except here


import { EffectCoverflow, Navigation, Pagination, Autoplay} from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/effect-coverflow'
import 'swiper/css/pagination';


export default {
    name: 'ui-main-top-slider',
    components: {
      Swiper,
      SwiperSlide,
    },
    props: {
      slidesPerView: {
        type: Number,
        default: 1
      }
    },
    data(){
      return {
        modules: [EffectCoverflow, Navigation, Pagination, Autoplay]
      }
    },
    
}
</script>

<style scoped>
.swiper {
  width: 100%;
  height: 100%;
  border-radius: 7px;
  margin: 0px;
  position: relative;
}

.swiper .swiper-button-prev:after, .swiper .swiper-button-next:after {
  color: #B7B8C5;
  font-size: 30px;
}

.swiper .swiper-slide {
  width: 100%;
  height: 100%;
  cursor: grab;
}

.swiper .swiper-slide > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.swiper .swiper-pagination {
  bottom: 5px;
}

.swiper .swiper-pagination-bullet {
  width: 10px;
  height: 10px;
  display: inline-block;
  background: #74CCD8;
}

.swiper-button-prev:after, .swiper-button-next:after {
  color: #B7B8C5;
  font-size: 25px;
}

</style>