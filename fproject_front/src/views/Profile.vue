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
                <div class="profile_tab">
                    <img src="@/assets/img/cart_blue.png"> &nbsp; &nbsp;
                    <!-- <img src="@/assets/img/cart_white.png"> &nbsp; &nbsp;        CHANGE WHEN TAB CLICKED!!!  -->
                    <span>Мои заказы</span>
                </div>
                <div class="profile_tab">
                    <img src="@/assets/img/like_blue.png"> &nbsp; &nbsp;
                    <!-- <img src="@/assets/img/like_white.png"> &nbsp; &nbsp;        CHANGE WHEN TAB CLICKED!!!  -->
                    <span>Список желаний</span>
                </div>
                <div class="profile_tab">
                    <img src="@/assets/img/sale_blue.png"> &nbsp; &nbsp;
                    <!-- <img src="@/assets/img/sale_white.png"> &nbsp; &nbsp;        CHANGE WHEN TAB CLICKED!!!  -->
                    <span>Акции и скидки</span>
                </div>
                <div class="profile_tab">
                    <img src="@/assets/img/settings_blue.png"> &nbsp; &nbsp;
                    <!-- <img src="@/assets/img/settings_white.png"> &nbsp; &nbsp;    CHANGE WHEN TAB CLICKED!!!  -->
                    <span>Настройки профиля</span>
                </div>
            </div>
            
        </div>
        <div class="profile_content_orders" v-if="profile_content == 'orders'">
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
        <div class="profile_content_liked" v-if="profile_content == 'liked'">
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
        <div class="profile_content_sales" v-if="profile_content == 'sales'">
            <h1>Актуальные акции и скидки</h1>
            <div class="profile_sales_grid">
                <div class="sale_box">
                    <img src="@/assets/img/Rectangle_59.png" alt="">
                    <br>
                    <br>
                    <h4>Акция 2+1</h4>
                    <br>
                    <span>При покупке двох единиц товара вы получите третий в подарок!</span>
                    <strong class="read_detail" @click="$router.push('/about')">
                        Смотреть товары &nbsp; &nbsp; 
                        <img src="@/assets/img/arrow_5.png" alt="">
                    </strong>
                </div>
                <div class="sale_box">
                    <img src="@/assets/img/Rectangle_59.png" alt="">
                    <br>
                    <br>
                    <h4>Акция 2+1</h4>
                    <br>
                    <span>При покупке двох единиц товара вы получите третий в подарок!</span>
                    <strong class="read_detail" @click="$router.push('/about')">
                        Смотреть товары &nbsp; &nbsp; 
                        <img src="@/assets/img/arrow_5.png" alt="">
                    </strong>
                </div>
                <div class="sale_box">
                    <img src="@/assets/img/Rectangle_59.png" alt="">
                    <br>
                    <br>
                    <h4>Акция 2+1</h4>
                    <br>
                    <span>При покупке двох единиц товара вы получите третий в подарок!</span>
                    <strong class="read_detail" @click="$router.push('/about')">
                        Смотреть товары &nbsp; &nbsp; 
                        <img src="@/assets/img/arrow_5.png" alt="">
                    </strong>
                </div>
            </div>
        </div>
        <form action="" class="register_form">
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
                Зарегестрироватся
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
            profile_content: 'orderss'
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/css/profile.css');
</style>