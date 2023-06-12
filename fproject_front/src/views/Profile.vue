<template>
<!-- <Header :key="header_user_state" /> -->

<div class="profile_container">
    <ui-bread-crumbs />
    <div class="profile_info_and_content">
        <div class="profile_info">
            <a class="exit_acc" @click="exitAcc">Выйти</a>
            <img src="@/assets/img/cat_profile.jpg">
            <br>
            <div class="change_img">
                <img src="@/assets/img/photo-camera.png"> &nbsp; &nbsp;
                <span>Изменить</span>
            </div>
            <h3 style="padding: 0px 30px;">Иванова Иванна Ивановна</h3>
            <div class="profile_tabs">
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: orders_visible
                }"
                @mouseenter="setTabVisible('orders')"
                @mouseleave="setTabInvisible('orders')"
                @click="profileWhatVisible('orders')"
                >
                    <img src="@/assets/img/cart_blue.png" v-if="!orders_visible"> 
                    <span v-if="!orders_visible">&nbsp; &nbsp;</span>
                    <img src="@/assets/img/cart_white.png" v-if="orders_visible"> 
                    <span v-if="orders_visible">&nbsp; &nbsp;</span>
                    <span>Мои заказы</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: liked_visible
                }"
                @mouseenter="setTabVisible('liked')"
                @mouseleave="setTabInvisible('liked')"
                @click="profileWhatVisible('liked')"
                >
                    <img src="@/assets/img/like_blue.png" v-if="!liked_visible"> 
                    <span v-if="!liked_visible">&nbsp; &nbsp;</span>
                    <img src="@/assets/img/like_white.png" v-if="liked_visible"> 
                    <span v-if="liked_visible">&nbsp; &nbsp;</span>
                    <span>Список желаний</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: sales_visible
                }"
                @mouseenter="setTabVisible('sales')"
                @mouseleave="setTabInvisible('sales')"
                @click="profileWhatVisible('sales')"
                >
                    <img src="@/assets/img/sale_blue.png" v-if="!sales_visible"> 
                    <span v-if="!sales_visible">&nbsp; &nbsp;</span>
                    <img src="@/assets/img/sale_white.png" v-if="sales_visible"> 
                    <span v-if="sales_visible">&nbsp; &nbsp;</span>
                    <span>Акции и скидки</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: register_visible
                }"
                @mouseenter="setTabVisible('register')"
                @mouseleave="setTabInvisible('register')"
                @click="profileWhatVisible('register')"
                >
                    <img src="@/assets/img/settings_blue.png" v-if="!register_visible"> 
                    <span v-if="!register_visible">&nbsp; &nbsp;</span>
                    <img src="@/assets/img/settings_white.png" v-if="register_visible"> 
                    <span v-if="register_visible">&nbsp; &nbsp;</span>
                    <span>Настройки профиля</span>
                </div>
            </div>
            
        </div>
        <div class="profile_content_orders" v-if="$store.state.profile_content == 'orders'">
            <h2>История Ваших заказов</h2><br>
            <div class="card_product_explain">
                <span>№ заказа</span>
                <span>Дата</span>
                <span>Колл-во</span>
                <span>Сумма</span>
                <span>Статус</span>
                <img src="@/assets/img/Vector_42.png" alt="">
            </div>
            <ui-select
                    :purpose="'cart_products'"
                    >
                        <template #row_info>
                            <span>2345678</span>
                            <span>24.05.2022</span>
                            <span>5</span>
                            <span>1244.99 €</span>
                            <span class="order_statuswait">В ожидании</span>
                            <img src="@/assets/img/Vector_42.png" alt="">
                        </template>
                        <template #products>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                        </template>
            </ui-select>
            <ui-select
                    :purpose="'cart_products'"
                    >
                        <template #row_info>
                            <span>2345678</span>
                            <span>24.05.2022</span>
                            <span>5</span>
                            <span>1244.99 €</span>
                            <span class="order_statuspayed">Оплачен</span>
                            <img src="@/assets/img/Vector_42.png" alt="">
                        </template>
                        <template #products>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                        </template>
            </ui-select>
            <ui-select
                    :purpose="'cart_products'"
                    >
                        <template #row_info>
                            <span>2345678</span>
                            <span>24.05.2022</span>
                            <span>5</span>
                            <span>1244.99 €</span>
                            <span class="order_statusclosed">Отменен</span>
                            <img src="@/assets/img/Vector_42.png" alt="">
                        </template>
                        <template #products>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                            <div class="cart_product">
                                <img src="@/assets/img/Rectangle_37.png" alt="">
                                <div class="product_name_and_price">
                                    <div class="product_info">
                                        <h3>Прогулочная коляска ABC Design Ping</h3>
                                        <p>Модель: <span>CH-353553</span></p>
                                        &nbsp; &nbsp;
                                        <p>Код товара: <span>000433</span></p>
                                    </div>
                                    <h2>1000.99 €</h2>
                                </div>
                            </div>
                        </template>
            </ui-select>
                    
        </div>
        <div class="profile_content_liked" v-else-if="$store.state.profile_content == 'liked'">
            <h1>Список моих желаний</h1><br>
            <div class="liked_products">
                <div class="swiper-slide">
                    <div class="sale_hit_new_box50">
                        -90%
                    </div>
                    <div class="to_like_box">
                        <img src="@/assets/img/trash.png" alt="">
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
                </div>
                <div class="swiper-slide">
                    <div class="sale_hit_new_box50">
                        -90%
                    </div>
                    <div class="to_like_box">
                        <img src="@/assets/img/trash.png" alt="">
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
                </div>
                <div class="swiper-slide">
                    <div class="sale_hit_new_box50">
                        -90%
                    </div>
                    <div class="to_like_box">
                        <img src="@/assets/img/trash.png" alt="">
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
                </div>
                <div class="swiper-slide">
                    <div class="sale_hit_new_box50">
                        -90%
                    </div>
                    <div class="to_like_box">
                        <img src="@/assets/img/trash.png" alt="">
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
                </div>
            </div>
        </div>
        <div class="profile_content_sales" v-else-if="$store.state.profile_content == 'sales'">
            <h1>Актуальные акции и скидки</h1>
            <ui-select 
            :purpose="'detail'"
            v-model:selected_option="current_sale"
            :options="['>= 25%', '>= 50%', '>= 75%']"
            />
            <div class="liked_products">
                <div 
                class="swiper-slide"
                v-for="_ in 4"
                >
                    <div class="sale_hit_new_box50">
                        -90%
                    </div>
                    <div class="to_like_box">
                        <div class="like"></div>
                    </div>
                    <img src="@/assets/img/watched_slide_img1.png" alt="">
                    <div class="slide_desc">
                        <h3>100 &euro;</h3> &nbsp; <span>200 &euro;</span><br><br>
                        <p>Safety 1st Timba Natural Wood 3 в 1 Стульчик для кормления + подушка {{ _ }}</p>
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
                </div>
            </div>
        </div>
        <form class="register_form" v-else>
            <h2>Редактированние личных данных</h2>
            <br>
            <div class="user_info_inputs">
                <input v-model="email" type="email" placeholder="Электронная почта*">
                <span class="error_message">{{ email_error }}</span>
                <input v-model="tel" type="number" placeholder="Номер телефона*">
                <span class="error_message">{{ tel_error }}</span>
                <div class="first_last_name_row_inputs">
                    <div class="fn_input_wrapper">
                        <input v-model="first_name" type="text" placeholder="Ваше имя*">
                        <span class="error_message">{{ first_name_error }}</span>
                    </div>
                    <div class="fn_input_wrapper">
                        <input v-model="last_name" type="text" placeholder="Фамилия*">
                        <span class="error_message">{{ last_name_error }}</span>
                    </div>
                    
                </div>
                
                <input v-model="password" type="password" placeholder="Придумайте пароль*">
                <span class="error_message">{{ password_error }}</span>
            </div>
            <br>
            <h2>Адрес для получения доставки</h2>
            <div class="adresses">
                <input v-model="city" type="text" placeholder="Город / Село / Пагаст / Район*">
                <span class="error_message">{{ city_error }}</span>
                <input v-model="street" type="text" placeholder="Улица / Дом / Квартира*">
                <span class="error_message">{{ street_error }}</span>
                <input v-model="post_code" type="number" placeholder="Почтовый индекс*">
                <span class="error_message">{{ post_code_error }}</span>
            </div>
            <label class="to_mail_list">
                <input v-model="in_mailing_list" type="checkbox" />
                &nbsp;
                Оформить подписку на рассылку писем
            </label>
            <button 
            class="reg_btn"
            style="margin-top: 20px;"
            >
                <img src="@/assets/img/ok3.png" alt=""> &nbsp;
                Сохранить изменения
            </button>
            <span class="del_acc">
                Удалить аккаунт
            </span>
        </form>
        <!-- <div class="profile_empty">
           <ui-profile-empty 
            :header="'У вас пока нет заказов'"
            :content="'Давайте исправим это! Сделайте свою первую покупку в нашем магазине прямо сейчас.'"
            :btn_content="'Смотреть каталог'"
            /> 
        </div> -->
        
    </div>
</div>
<mini-products-slider style="padding: 60px 0%;background: rgb(244, 245, 249);">
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


</template>

<script>
import emitsForApp from '@/mixins/emitsForApp'

export default {
    data(){
        return {
            orders_visible: false,
            liked_visible: false,
            sales_visible: false,
            register_visible: false,
            orders_clicked: false,
            liked_clicked: false,
            sales_clicked: false,
            register_clicked: false,
            
            current_sale: 'Select sale',
            user: JSON.parse(localStorage.getItem('current_user')),
            
        }
    },
    mixins: [emitsForApp],
    methods: {
        profileWhatVisible(visible_tab){
            // set tab clicked = true by name
            Object.keys(this.$data).forEach( key => {
                if (key.endsWith('clicked') || key.endsWith('visible')) {
                    this.$data[key] = false
                }
            })
            this.$store.commit('setProfileContent', visible_tab)
            this.setTabVisible(visible_tab)
            this.$data[`${visible_tab}_clicked`] = true
        },
        setTabVisible(tab_name){
            // set tab _visible = true by name for styles
            this.$data[`${tab_name}_visible`] = true
        },
        setTabInvisible(tab_name){
            // set tab _visible = false by name for disable styles
            if (!this.$data[`${tab_name}_clicked`]) {
                this.$data[`${tab_name}_visible`] = false
            }
            
        },
        exitAcc(){
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
            localStorage.removeItem('current_user')
            this.$emit('rerender_header')
            this.$router.push('/register')
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Profile')
        const user_profile_info = await this.$store.dispatch(
            'commonGETRequestWithAuth', 
            `users_profile/${this.user.id}`
        )
    }
}
</script>

<style scoped>
    @import url('@/assets/css/profile.css');
</style>