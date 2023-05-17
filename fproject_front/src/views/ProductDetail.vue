<template>
<div class="write_feedback_modal_wrapper" v-if="write_feedback_visible"></div>
<div class="write_feedback_modal" v-if="write_feedback_visible">
    <img
    src="@/assets/img/clear.png"
    class="auth_modal_close_img"
    @click="write_feedback_visible = false"
    >
    <h2>Напишите свой отзыв о продукте:</h2>
    <input type="text" placeholder="Заголовок*">
    <textarea name="" id="" cols="30" rows="10" placeholder="Текст отзыва*"></textarea>
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
    <button class="feedback_btn">
        <img src="@/assets/img/star_white.png" alt="">&nbsp;
        Оставить отзыв
    </button>
</div>
<Header />

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
                            {{ product.comments_count }} отзыва
                        </p>
                        <img :src="product.brand.image" class="brand_logo">
                </div>
                <div v-else>
                        <div class="inline">
                            <img src="@/assets/img/close_red.png" alt=""> &nbsp; &nbsp;
                            <span style="color:red">Товара в настоящее время нет в наличии</span>
                        </div>
                        <br><br>
                        <div class="inline">
                            <h5>Код товара:</h5> &nbsp; &nbsp;
                            <span>000433</span>
                        </div>
                        <img src="@/assets/img/brand2.png" alt="" class="brand_logo">
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
                            v-for="_ in 5"
                            >
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="similar_product_mini_detail">
                                    <h3>Прогулочная коляска ABC Design Ping {{ _ }}</h3>
                                    <br>
                                    <div class="inline">
                                        <div class="inline">
                                            <span class="span_price">1000 €</span>
                                            &nbsp; &nbsp;
                                            <span class="span_price_del">2500 €</span>
                                        </div>
                                        <button class="buy_btn">
                                            <img src="@/assets/img/basket_white.png" alt="">
                                            &nbsp;
                                            Купить
                                        </button>
                                        <div class="like_icon">
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
                        v-model:selected_option="selected_option"
                        :purpose="'detail'"
                        :options="product.get_resolutions"
                        />
                    </div>
                    <div class="inline product_prices">
                        <div class="price inline">
                            <h2>{{ product.price }} €</h2> &nbsp; &nbsp;
                            <span v-if="product.saled_price">{{ product.saled_price }} €</span> 
                        </div>
                        <div class="count">
                            <button class="inc_dec_btn" @click="dec_count">-</button>
                            <input type="number" v-model="count">
                            <button class="inc_dec_btn" @click="count++">+</button>
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
                    Maxi-Cosi Mica — вращающееся автокресло стандарта ECE 129 i-Size, предназначенное для детей от рождения до 4 лет.
                    <br><br>
                    Модель Mica предлагает простую установку при помощи основания Isofix с упором в пол и обеспечивает поворот чаши
                    в любом направлении на 360 °. Фирменная технология Maxi-Cosi G-CELL защиты от бокового удара соответствует самым
                    высоким стандартам безопасности. Подголовник имеет наполнитель с эффектом памяти. В комплекте предлагается мягкий
                    вкладыш для новорождённых. Спинка оснащена встроенной системой вентиляции для поддержания оптимального микроклимата.
                    <br><br>
                    Преимущества автокресла Maxi Cosi Mica: <br>
                    — поворотное автокресло стандарта ECE 129 i-Size <br>
                    — технология боковой защиты G-CELL <br>
                    — возможность откидывания в горизонтальное положения для сна <br>
                    — вкладыш для новорождённых <br>
                    — система вентиляции в спинке <br>
                    — наполнитель подголовника с эффектом памяти <br>
                    — 5-точечные внутренние ремни с системой лёгкой посадки и высадки ребёнка <br>
            </div>
            <div class="about_product_content_characteristics" v-else-if="tab_active['characterictics']">
                <div class="characteristic">
                    <h5>Максимальный вес ребенка:</h5>
                    <span>7 кг</span>
                </div>
                <div class="characteristic">
                    <h5>Цвет:</h5>
                    <span>Красный, черный, коричневый, синий</span>
                </div>
                <div class="characteristic">
                    <h5>Материал:</h5>
                    <span>Водонепроницаемая ткань</span>
                </div>
                <div class="characteristic">
                    <h5>Размер:</h5>
                    <span>107см x 234см</span>
                </div>
            </div>
            <div class="about_product_content_feedbacks" v-else-if="tab_active['feedbacks']">
                <div class="about_product_content_feedback">
                    <h3>Очень понравилась коляска!</h3>
                    <div class="rating">
                        <div class="stars">
                            <img src="@/assets/img/star.png" alt="">
                            <img src="@/assets/img/star.png" alt="">
                            <img src="@/assets/img/star.png" alt="">
                            <img src="@/assets/img/star.png" alt="">
                            <img src="@/assets/img/star_gray.png" alt="">
                        </div>
                    </div>
                    <span>
                        Модель Mica предлагает простую установку при помощи основания Isofix с упором в пол и
                        обеспечивает поворот чаши в любом направлении на 360 °.
                        Модель Mica предлагает простую установку при помощи основания Isofix с упором в пол и
                        обеспечивает поворот чаши в любом направлении на 360 °.
                    </span>
                    <div class="about_product_content_feedback_owner_box">
                        <span class="owner_logo">
                            M
                        </span>
                        <span>Мария</span>
                    </div>
                </div>
                <div class="about_product_content_feedback">
                    <h3>Очень NE понравилась коляска!</h3>
                    <div class="rating">
                        <div class="stars">
                            <img src="@/assets/img/star.png" alt="">
                            <img src="@/assets/img/star.png" alt="">
                            <img src="@/assets/img/star_gray.png" alt="">
                            <img src="@/assets/img/star_gray.png" alt="">
                            <img src="@/assets/img/star_gray.png" alt="">
                        </div>
                    </div>
                    <span>
                        Модель Mica предлагает простую установку при помощи основания Isofix с упором в пол и
                        обеспечивает поворот чаши в любом направлении на 360 °.
                        Модель Mica предлагает простую установку при помощи основания Isofix с упором в пол и
                        обеспечивает поворот чаши в любом направлении на 360 °.
                    </span>
                    <div class="about_product_content_feedback_owner_box">
                        <span class="owner_logo">
                            T
                        </span>
                        <span>Tария</span>
                    </div>
                </div>
                <div class="btns">
                    <button>Больше отзывов</button>
                    &nbsp; &nbsp;
                    <button @click="write_feedback_visible = true">Оставить отзыв</button>
                </div>
                
            </div>
    </div>

        
</div>
<mini-products-slider style="background: #F4F5F9;padding: 60px 0% 60px 0%">
        <template #header>
            <h1>С этим товаром покупают</h1>
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

                    </div>
        </SplideSlide>
</mini-products-slider> 
<mini-products-slider style="padding: 60px 0% 60px 0%">
        <template #header>
            <h1>Вы уже смотрели</h1>
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
<ui-href-blog-box 
style="padding: 60px 0% 70px 0%;"
:header_text="'Актуальные статьи'"
/>

<ui-footer />
</template>

<script>
import '@splidejs/vue-splide/css/sea-green'
import Splide from '@splidejs/splide'


export default {
    data(){
        return{
            product: {},
            stars_gray: 0,
            count: 1,
            tab_active: {
                'desc': true,
                'characterictics': false,
                'feedbacks': false
            },
            write_feedback_visible: false,
            // options_to_select: ['107см x 234см', '50см x 50см', '60м x 60см', '999см x 999см'],
            selected_option: '',
            stars_mouse_enter_leave_available: true,
            pointed_stars: 0
        }
    },
    methods: {
        dec_count(){
            this.count > 1 ? this.count-- : null
        },
        setStarsUI(star_num, for_click=false){
            if (for_click) {
                this.stars_mouse_enter_leave_available = false
                this.pointed_stars = star_num
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
        }
    },

    async beforeMount(){
        this.product = await this.$store.getters.fetchProductDetail(this.$route.params.product_id)
        this.product.stars_avg = this.product.stars_avg 
        this.selected_option = this.product.get_resolutions[0]

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
    }
}
</script>

<style scoped>
    @import url('@/assets/css/product_detail.css');
</style>