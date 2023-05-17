<template>
<div class="slider_component_main_box">
    <slot name="header"></slot>
    <Splide 
    class="watched_products_slider" 
    :options="{ 
        speed: 1000,
        rewind: true,
        perPage: slidesPerPage,
        perMove: 1,
        gap: 20,
        pagination: false,
    }"
    >   
        
        <slot></slot>

    </Splide>
    <slot name="bottom_button"></slot>
</div>
</template>

<script>
// Slider component with custom content, header, bottom section in this project,
// used in many places


import { Navigation, Autoplay} from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/effect-coverflow'
import 'swiper/css/pagination';

import '@splidejs/vue-splide/css/sea-green';



export default {
  name: 'mini-products-slider',
  components: {
    Swiper,
    SwiperSlide,
  },
  props:{
    slidesPerPage: {
      type: Number,
      default: 4
    }
  },
  data(){
      return {
        modules: [Navigation, Autoplay]
      }
  },
}
</script>

<style>                                                     /* STYLES NOT SCOPED */
.slider_component_main_box {
  text-align: center;
  padding: 60px 5% 70px 5%;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #090F24;
  position: relative;
}
.watched_products_slider{
    width: 90%;
    display: flex;
}
.watched_products_slider .swiper-slide {
    background: white;
    padding: 15px 15px 20px 15px;
    border: 1px solid #E4E7EE;
    border-radius: 15px;
    min-height: 400px;
    max-height: 550px;
    position: relative;
    transition: .5s;
    cursor: pointer;
}
.watched_products_slider .swiper-slide:hover{
    background: rgba(126, 126, 126, 0.2);
}
.to_like_box {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #F4F5F9;
  opacity: 0.85;
  border-radius: 50px;
  top: 15px;
  right: 15px;
  width: 55px;
  height: 55px;
  cursor: pointer;
}
.like {
  width: 25px;
  height: 22px;
  background: #b8b9c6;
  clip-path: path("M12 21.593c-5.63-5.539-11-10.297-11-14.402 0-3.791 3.068-5.191 5.281-5.191 1.312 0 4.151.501 5.719 4.457 1.59-3.968 4.464-4.447 5.726-4.447 2.54 0 5.274 1.621 5.274 5.181 0 4.069-5.136 8.625-11 14.402m5.726-20.583c-2.203 0-4.446 1.042-5.726 3.238-1.285-2.206-3.522-3.248-5.719-3.248-3.183 0-6.281 2.187-6.281 6.191 0 4.661 5.571 9.429 12 15.809 6.43-6.38 12-11.148 12-15.809 0-4.011-3.095-6.181-6.274-6.181");
}
.to_like_box:hover .like, .change_purple_permanent {
  background: #ED9BB9;
  clip-path: path("M12 4.248c-3.148-5.402-12-3.825-12 2.944 0 4.661 5.571 9.427 12 15.808 6.43-6.381 12-11.147 12-15.808 0-6.792-8.875-8.306-12-2.944z");
}
.watched_products_slider .swiper-slide > img {
  width: 100%;
  height: 240px;
  object-fit: cover;
  border-radius: none;
  margin-bottom: 20px;
}
.slide_desc {
  text-align: left;
}
.slide_desc > div > h3 {
  display: inline;
}
.slide_desc > div > span {
  text-decoration: line-through;
  color: #B7B8C5;
}
.slide_desc > p {
  font-weight: 400;
  font-size: 18px;
  line-height: 139%;
}
.colors {
  width: 100%;
  margin: 15px 0px;
  display: flex;
}
.colors .color {
  border-radius: 50px;
  width: 40px;
  height: 40px;
  margin-right: 10px;
}
.colors .color:last-child {
  margin-right: 0px;
}
.slide_desc .delivery_box {
  display: flex;
}
.delivery_box > img {
  margin-right: 10px;
}
.delivery_box > small {
  color: #686877;
}
.sale_hit_new_box50{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #FFD882;
    border-radius: 50px;
    top: 15px;left: 15px;
    border: 1.5px dashed white;
    width: 55px;
    height: 55px;
    font-size: 14px;
    animation: scaled_sale 1s infinite;
}
.sale_hit_new_boxhit{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(180deg, #ED9BC1 0%, #ED9BB9 100%);
    color: white;
    border-radius: 50px;
    top: 15px;left: 15px;
    width: 55px;
    height: 55px;
    font-size: 14px;
}
.sale_hit_new_boxnew{
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #FFC186;
    color: white;
    border-radius: 8px;
    top: 15px;left: 15px;
    padding: 8px 10px;
    font-weight: 600;
    line-height: 139%;
    font-size: 14px;
}

.swiper-button-prev:after, .swiper-button-next:after {
  color: #B7B8C5;
  font-size: 30px;
}
.watched_products_slider .swiper-button-prev{
    left: 9%;
}
.watched_products_slider .swiper-button-next{
    right: 9%;
}





















@keyframes scaled_sale {
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
</style>