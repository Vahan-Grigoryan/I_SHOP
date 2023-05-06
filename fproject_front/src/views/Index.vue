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
    
    <div class="main_bottom_slider">
        <ui-main-bottom-slider />
    </div>
    
    <ui-our-procs />

    <div class="variety_of_products">
        <h1>Широкий ассортимент товаров</h1><br>
        <span>для малышей и мам</span>
        <div class="for_grid">
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg1.png" alt=""><br>
                <span>Коляски</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg2.png" alt=""><br>
                <span>Автокресла</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg3.png" alt=""><br>
                <span>Детская комната</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg4.png" alt=""><br>
                <span>Транспорт и спорт</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg4.png" alt=""><br>
                <span>Игрушки и игры</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg5.png" alt=""><br>
                <span>Одежда и обувь</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg6.png" alt=""><br>
                <span>Для мамочек</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg7.png" alt=""><br>
                <span>Гигиена и уход</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg8.png" alt=""><br>
                <span>Кормление</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg9.png" alt=""><br>
                <span>Детксие подарки</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg10.png" alt=""><br>
                <span>Елки и игрушки</span>
            </div>
            <div class="category_box" @click="$router.push('/mega_category/5')">
                <img src="@/assets/img/cbimg11.png" alt=""><br>
                <span>Подарочные карты</span>
            </div>
        </div>
    </div>

    <mini-products-slider>
        <template #header>
            <h1>Вы уже смотрели</h1>
        </template>
        
        <SplideSlide 
        class="swiper-slide"
        v-for="product in products"
        :key="product.id"
        @click="$router.push(`/detail/${product.id}`)"
        >
            <div 
            :class="defineSaleNewHit(product.saleNewHit)"
            v-if=" typeof product.price != 'number' "
            >
                {{ product.saleNewHitContent().toUpperCase() }}
            </div>
            <div class="to_like_box"> <!-- @click="addOrDelLikes(product.id)" -->
                <div :class="{
                    like: true,
                    // change_purple_permanent: likesPurpleStatus[product.id]
                }">
                </div>
            </div>
            <img :src="product.image" alt="">
            <div class="slide_desc">
                <div v-if="typeof product.price == 'number'">
                    <h3>{{ product.price }} &euro;</h3><br><br>
                </div>
                <div>
                    <h3>{{ product.price[0] }} &euro;</h3> &nbsp; <span>{{ product.price[1] }} &euro;</span><br><br>
                </div>
                
                <p>{{ product.name }}</p>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
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

    <mini-products-slider>
        <template #header>
            <h1>Популярные товары</h1>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>

    </mini-products-slider>

    <mini-products-slider style="background: #F4F5F9;">
        <template #header>
            <h1>Новинки</h1>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
                        </div>
                    </div>
        </SplideSlide>
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
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star.png" class="star" />
                                <img src="@/assets/img/star_gray.png" class="star" />
                            </div>
                            <small>&nbsp; 15 отзывов</small>
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

    <ui-brands />

    <ContactUsBox />

    <ui-href-blog-box />

    <ui-footer />
    
</template>

<script>
export default {
    data(){
        return {
            likes: [],
            likesPurpleStatus: new Proxy({}, {
                get: function(target, name) {
                    return name in target ? target[name] : false
                }
            }),
            products:[
                {   
                    id: 1,
                    price: 200,
                    image: '@/assets/img/watched_slide_img1.png',
                    name: 'Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка',
                    saleNewHit: 'sale', // define left top box type
                    saleNewHitContent: function() {
                        let calculation = () => {
                            if(this.price.length == 2 && this.saleNewHit == 'sale'){
                                return 100 - Math.round(this.price[0]*100/this.price[1])
                            }
                            return null
                        }
                        return calculation() ? `-${calculation()}%` : this.saleNewHit
                    } // define left top box content by params: saleNewHit, price
                },
                {   
                    id: 2,
                    price: [500, 700],
                    image: '@/assets/img/watched_slide_img2.png',
                    name: 'Some desc2...',
                    saleNewHit: 'new',
                    saleNewHitContent: function() {
                        let calculation = () => {
                            if(this.price.length == 2 && this.saleNewHit == 'sale'){
                                return 100 - Math.round(this.price[0]*100/this.price[1])
                            }
                            return null
                        }
                        return calculation() ? `-${calculation()}%` : this.saleNewHit
                    }
                    // not all characteristics...
                },
                {   
                    id: 3,
                    price: [100, 200],
                    image: '@/assets/img/watched_slide_img3.png',
                    name: 'Some desc3...',
                    saleNewHit: 'sale',
                    saleNewHitContent: function() {
                        let calculation = () => {
                            if(this.price.length == 2 && this.saleNewHit == 'sale'){
                                return 100 - Math.round(this.price[0]*100/this.price[1])
                            }
                            return null
                        }
                        return calculation() ? `-${calculation()}%` : this.saleNewHit
                    }
                    // not all characteristics...
                },
                {   
                    id: 4,
                    price: [100, 300],
                    image: '@/assets/img/watched_slide_img3.png',
                    name: 'Some desc4...',
                    saleNewHit: 'hit',
                    saleNewHitContent: function() {
                        let calculation = () => {
                            if(this.price.length == 2 && this.saleNewHit == 'sale'){
                                return 100 - Math.round(this.price[0]*100/this.price[1])
                            }
                            return null
                        }
                        return calculation() ? `-${calculation()}%` : this.saleNewHit
                    }
                    // not all characteristics...
                },
                {   
                    id: 5,
                    price: [550, 600],
                    image: '@/assets/img/watched_slide_img3.png',
                    name: 'Some desc5...',
                    saleNewHit: 'sale',
                    saleNewHitContent: function() {
                        let calculation = () => {
                            if(this.price.length == 2 && this.saleNewHit == 'sale'){
                                return 100 - Math.round(this.price[0]*100/this.price[1])
                            }
                            return null
                        }
                        return calculation() ? `-${calculation()}%` : this.saleNewHit
                    }
                    // not all characteristics...
                }
            ]
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
                new: {sale_hit_new_boxhit: true},
                hit: {sale_hit_new_boxnew: true},
            } 
            return definition[productSaleNewHit]
        }
    }
}
</script>

<style>
    @import url("@/assets/css/index.css");
</style>