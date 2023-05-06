<template>
<Header />

<div class="profile_container">
    <ui-bread-crumbs />
    <div class="profile_info_and_content">
        <div class="profile_info">
            <img src="@/assets/img/cat_profile.jpg" alt="">
            <br>
            <div class="change_img">
                <img src="@/assets/img/photo-camera.png" alt=""> &nbsp; &nbsp;
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
        <form action="" class="register_form" v-else-if="$store.state.profile_content == 'register'">
            <h2>Редактированние личных данных</h2>
            <br>
            <div class="user_info_inputs">
                <input type="email" placeholder="Электронная почта*">
                <input type="tel" placeholder="Номер телефона*">
                <input type="text" placeholder="Ваше имя*">
                <input type="text" placeholder="Фамилия*">
                <input type="password" placeholder="Придумайте пароль (от 6 до 10 символов)*">
            </div>
            <br>
            <br>
            <h2>Адрес для получения доставки</h2>
            <div class="adresses">
                <input type="text" placeholder="Город / Село / Пагаст / Район*">
                <input type="text" placeholder="Улица / Дом / Квартира*">
                <input type="text" placeholder="Почтовый индекс*">
            </div>
            <button type="submit" class="reg_btn">
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

<ui-footer />
</template>

<script>
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
        }
    },
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
            
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/css/profile.css');
</style>