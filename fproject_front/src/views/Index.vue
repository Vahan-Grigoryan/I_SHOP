<template>
    <Header />

    <main>
        <ui-main-top-slider />
        
        <div class="right_screens">
            <img src="@/assets/img/img_top.png" alt="">
            <img src="@/assets/img/Banner2.png" alt="">
        </div>
    </main>
    
    <div class="main_bottom_slider">
        <ui-main-bottom-slider />
    </div>
    
    <div class="our_procs">
        <div class="our_procs_box">
            <img src="@/assets/img/diamond.png" alt="">
            <span>Гарантия <br> качества</span>
        </div>
        <div class="our_procs_box">
            <img src="@/assets/img/mini_cubes.png" alt="">
            <span>Огромный <br> ассортимент</span>
        </div>
        <div class="our_procs_box">
            <img src="@/assets/img/delivery.png" alt="">
            <span>Быстрая <br> доставка</span>
        </div>
        <div class="our_procs_box">
            <img src="@/assets/img/sale.png" alt="">
            <span>Выгодные <br> цены и бонусы</span>
        </div>
    </div>

    <div class="variety_of_products">
        <h1>Широкий ассортимент товаров</h1><br>
        <span>для малышей и мам</span>
        <div class="for_grid">
            <div class="category_box">
                <img src="@/assets/img/cbimg1.png" alt=""><br>
                <span>Коляски</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg2.png" alt=""><br>
                <span>Автокресла</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg3.png" alt=""><br>
                <span>Детская комната</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg4.png" alt=""><br>
                <span>Транспорт и спорт</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg4.png" alt=""><br>
                <span>Игрушки и игры</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg5.png" alt=""><br>
                <span>Одежда и обувь</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg6.png" alt=""><br>
                <span>Для мамочек</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg7.png" alt=""><br>
                <span>Гигиена и уход</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg8.png" alt=""><br>
                <span>Кормление</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg9.png" alt=""><br>
                <span>Детксие подарки</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg10.png" alt=""><br>
                <span>Елки и игрушки</span>
            </div>
            <div class="category_box">
                <img src="@/assets/img/cbimg11.png" alt=""><br>
                <span>Подарочные карты</span>
            </div>
        </div>
    </div>

    <mini-products-slider>
        <template #header>
            <h1>Вы уже смотрели</h1>
        </template>
        
        <SplideSlide class="swiper-slide">
            <div :class="{
                sale_hit_new_box50:true,
                sale_hit_new_boxnew:saleNew,
                sale_hit_new_boxhit:saleHit
            }">
                -50%
            </div>
            <div class="to_like_box" @click.stop>
                <div class="like"></div>
            </div>
            <img src="@/assets/img/watched_slide_img1.png" alt="">
            <div class="slide_desc">
                <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
            </div>
        </SplideSlide>
        <SplideSlide class="swiper-slide">
        
            <div :class="{
                sale_hit_new_box50:saleNumber,
                sale_hit_new_boxnew:saleNew,
                sale_hit_new_boxhit:saleHit
            }">
                ХИТ!
            </div>
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img src="@/assets/img/watched_slide_img2.png" alt="">
            <div class="slide_desc">
                <h3>1200 &euro;</h3><br><br>
                <p>Футболка DJ Dutchjeans E38091-45 Anthracite 16...</p> 
            </div>
        
        </SplideSlide>
        <SplideSlide class="swiper-slide">
        
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img src="@/assets/img/watched_slide_img3.png" alt="">
            <div class="slide_desc">
                <h3>1000 &euro;</h3> &nbsp; <span>1500 &euro;</span><br><br>
                <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
            </div>
        
        </SplideSlide>
        <SplideSlide class="swiper-slide">
    
            <div :class="{
                sale_hit_new_box50:saleNumber,
                sale_hit_new_boxnew:saleNew,
                sale_hit_new_boxhit:saleHit
            }">
                NEW!
            </div>
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img src="@/assets/img/watched_slide_img4.png" alt="">
            <div class="slide_desc">
                <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                <p>Safety 1st Timba Natural</p>
            </div>
        
        </SplideSlide>
        <SplideSlide class="swiper-slide">
            
            <div class="to_like_box">
                <div class="like"></div>
            </div>
            <img src="@/assets/img/watched_slide_img2.png" alt="">
            <div class="slide_desc">
                <h3>500 &euro;</h3> &nbsp; <span>750 &euro;</span><br><br>
                <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
            </div>
            
        </SplideSlide>

    </mini-products-slider>
    
    <mini-products-slider style="background: #F4F5F9;">
        <template #header>
            <h1>Акции и скидки</h1>
        </template>
        
        <SplideSlide class="swiper-slide">
                    <div class="sale_hit_new_box">
                        -90%
                    </div>
                    <div class="to_like_box">
                        <div class="like"></div>
                    </div>
                    <img src="@/assets/img/watched_slide_img1.png" alt="">
                    <div class="slide_desc">
                        <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                        <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
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
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div class="star"></div>
                            </div>
                            <small>15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
        <SplideSlide class="swiper-slide">
                    <div class="sale_hit_new_box">
                        -50%
                    </div>
                    <div class="to_like_box">
                        <div class="like"></div>
                    </div>
                    <img src="@/assets/img/watched_slide_img1.png" alt="">
                    <div class="slide_desc">
                        <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                        <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
                        <div class="colors">
                            <div class="color" style="background: maroon;"></div>
                            <div class="color" style="background: rgb(0, 255, 149);"></div>
                            <div class="color" style="background: rgb(30, 50, 58);"></div>
                            <div class="color" style="background: rgb(15, 112, 88);"></div>
                            <div class="color" style="background: rgb(189, 201, 19);"></div>
                        </div>
                        <div class="delivery_box">
                            <img src="@/assets/img/delivery.png" alt="">
                            <small>Доставка: 1-2 дня</small>
                        </div>
                        <div class="rating">
                            <div class="stars">
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                            </div>
                            <small>15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
        <SplideSlide class="swiper-slide">
                    <div class="sale_hit_new_box">
                        -70%
                    </div>
                    <div class="to_like_box">
                        <div class="like"></div>
                    </div>
                    <img src="@/assets/img/watched_slide_img1.png" alt="">
                    <div class="slide_desc">
                        <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                        <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
                        <div class="colors">
                            <div class="color" style="background: rgb(127, 153, 9);"></div>
                            <div class="color" style="background: rgb(84, 84, 179);"></div>
                            <div class="color" style="background: rgb(23, 173, 86);"></div>
                            <div class="color" style="background: rgb(47, 255, 245);"></div>
                            <div class="color" style="background: rgb(2, 48, 48);"></div>
                        </div>
                        <div class="delivery_box">
                            <img src="@/assets/img/delivery.png" alt="">
                            <small>Доставка: 1-2 дня</small>
                        </div>
                        <div class="rating">
                            <div class="stars">
                                <div style="background: #FFC186;" class="star"></div>
                                <div class="star"></div>
                                <div class="star"></div>
                                <div class="star"></div>
                                <div class="star"></div>
                            </div>
                            <small>15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
        <SplideSlide class="swiper-slide">
                    <div class="sale_hit_new_box">
                        -10%
                    </div>
                    <div class="to_like_box">
                        <div class="like"></div>
                    </div>
                    <img src="@/assets/img/watched_slide_img1.png" alt="">
                    <div class="slide_desc">
                        <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                        <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
                        <div class="colors">
                            <div class="color" style="background: violet;"></div>
                            <div class="color" style="background: gray;"></div>
                            <div class="color" style="background: aqua;"></div>
                            <div class="color" style="background: rgb(255, 47, 227);"></div>
                            <div class="color" style="background: rgb(128, 0, 100);"></div>
                        </div>
                        <div class="delivery_box">
                            <img src="@/assets/img/delivery.png" alt="">
                            <small>Доставка: 1-2 дня</small>
                        </div>
                        <div class="rating">
                            <div class="stars">
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div class="star"></div>
                                <div class="star"></div>
                                <div class="star"></div>
                            </div>
                            <small>15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
        <SplideSlide class="swiper-slide">
                    <div class="sale_hit_new_box">
                        -50%
                    </div>
                    <div class="to_like_box">
                        <div class="like"></div>
                    </div>
                    <img src="@/assets/img/watched_slide_img1.png" alt="">
                    <div class="slide_desc">
                        <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                        <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка</p>
                        <div class="colors">
                            <div class="color" style="background: red;"></div>
                            <div class="color" style="background: rgb(37, 37, 173);"></div>
                            <div class="color" style="background: rgb(0, 255, 170);"></div>
                            <div class="color" style="background: rgb(201, 211, 186);"></div>
                            <div class="color" style="background: rgb(86, 168, 168);"></div>
                        </div>
                        <div class="delivery_box">
                            <img src="@/assets/img/delivery.png" alt="">
                            <small>Доставка: 1-2 дня</small>
                        </div>
                        <div class="rating">
                            <div class="stars">
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div style="background: #FFC186;" class="star"></div>
                                <div class="star"></div>
                                <div class="star"></div>
                            </div>
                            <small>15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>

    </mini-products-slider>

    <div class="get_sales_info_form_box">
        <img src="@/assets/img/sale_kupon.png" alt="">
        <img src="@/assets/img/sale_circle.png" alt="">
        <div class="form_wrapper" action="">
            <div>
                <h1>Получайте информацию о скидках первыми</h1>
                <span>Оформите подписку и вы будете вкурсе всех наших выгодных акций и скидок</span>
                <form action="" method="post">
                    <input type="text" placeholder="Ваша электронная почта">
                    <button><strong>&#10003; Оформить подписку</strong></button>
                </form>
            </div>
            
        </div>
        <img class="right_girl" src="@/assets/img/form_right_girl.png" alt="">
    </div>

</template>

<script>
export default {
    data(){
        return {

        }
    }
}
</script>

<style>
    @import url("@/assets/css/index.css");
</style>