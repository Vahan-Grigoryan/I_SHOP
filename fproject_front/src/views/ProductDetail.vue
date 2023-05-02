<template>
<Header />

<div class="product_detail_container">
    <ui-bread-crumbs />
    <h1>Bugaboo Butterfly sporta rati, Black/Midnight Black-Midnight Black</h1>
    <div class="slider_and_content_flex">
            <div class="left_slider">
                <Splide
                class="main_detail_slider"
                :options="{ 
                    speed: 1000,
                    rewind: true,
                    pagination: false,
                }"
                >
                    <SplideSlide class="main_detail_slider__slide">
                        <img src="@/assets/img/image_7.png" alt="">
                    </SplideSlide>
                    <SplideSlide class="main_detail_slider__slide">
                        <img src="@/assets/img/toys.webp" alt="">
                    </SplideSlide>
                    <SplideSlide class="main_detail_slider__slide">
                        <img src="@/assets/img/toys2.webp" alt="">
                    </SplideSlide>
                    <SplideSlide class="main_detail_slider__slide">
                        <img src="@/assets/img/image_7.png" alt="">
                    </SplideSlide>
                    <SplideSlide class="main_detail_slider__slide">
                        <img src="@/assets/img/toys.webp" alt="">
                    </SplideSlide>
                    <SplideSlide class="main_detail_slider__slide">
                        <img src="@/assets/img/toys2.webp" alt="">
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
                    gap: 10
                }"
                >
                    <SplideSlide class="thumb">
                        <img src="@/assets/img/image_7.png" alt="">
                    </SplideSlide>
                    <SplideSlide class="thumb">
                        <img src="@/assets/img/toys.webp" alt="">
                    </SplideSlide>
                    <SplideSlide class="thumb">
                        <img src="@/assets/img/toys2.webp" alt="">
                    </SplideSlide>
                    <SplideSlide class="thumb">
                        <img src="@/assets/img/image_7.png" alt="">
                    </SplideSlide>
                    <SplideSlide class="thumb">
                        <img src="@/assets/img/toys.webp" alt="">
                    </SplideSlide>
                    <SplideSlide class="thumb">
                        <img src="@/assets/img/toys2.webp" alt="">
                    </SplideSlide>

                </Splide>
            </div>
            
            <div class="right_content">
                <div class="availability_box">
                    <div style="display: inline-flex;">
                        <div class="inline">
                            <img src="@/assets/img/delivery.png" alt=""> &nbsp; &nbsp;
                            <span>Доставка: 1-2 дня</span>
                        </div>
                        &nbsp; &nbsp;
                        <div class="inline">
                            <h5>Код товара:</h5> &nbsp; &nbsp;
                            <span>000433</span>
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
                        <img src="@/assets/img/star.png" alt=""> &nbsp;
                        <img src="@/assets/img/star.png" alt=""> &nbsp;
                        <img src="@/assets/img/star.png" alt=""> &nbsp;
                        <img src="@/assets/img/star.png" alt=""> &nbsp;
                        <img src="@/assets/img/star_gray.png" alt=""> &nbsp;
                        3 отзыва
                    </p>
                    <img src="@/assets/img/brand2.png" alt="" class="brand_logo">
                </div>
                <div class="product_detail_info">
                    <div style="display: flex;align-items: center;justify-content: space-between;">
                        <h2>Размер:</h2>
                        <ui-select 
                        style="width: 85%;"
                        v-model:selected_option="selected_option"
                        :purpose="'detail'"
                        :options="options_to_select"
                        />
                    </div>
                    <div class="inline product_prices">
                        <div class="price inline">
                            <h2>1000 €</h2> &nbsp; &nbsp;
                            <span>2500 €</span> 
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
                <button>get more feedbacks</button>
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
            count: 1,
            tab_active: {
                'desc': false,
                'characterictics': false,
                'feedbacks': true
            },
            
            options_to_select: ['107см x 234см', '50см x 50см', '60м x 60см', '999см x 999см'],
            selected_option: '107см x 234см',
        }
    },
    methods: {
        dec_count(){
            this.count > 1 ? this.count-- : null
        },
        setActiveTab(tab_name){
            Object.keys(this.tab_active).forEach( key => this.tab_active[key] = false )
            this.tab_active[tab_name] = true
        }
    },

    mounted(){
        const main_splide = new Splide('.main_detail_slider', { 
            speed: 1000,
            rewind: true,
            pagination: false,
        })
        const thumbs_splide = new Splide('.thumbs', { 
            speed: 1000,
            rewind: true,
            perPage: 6,
            pagination: false,
            isNavigation: true,
            gap: 10
        })
        main_splide.sync(thumbs_splide)
        main_splide.mount()
        thumbs_splide.mount()
    }
}
</script>

<style scoped>
    @import url('@/assets/css/product_detail.css');
</style>