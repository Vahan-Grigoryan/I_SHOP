<template>
    <Header />
    <div class="filters_container">
        <ui-bread-crumbs style="margin-bottom: 40px;"/>
        <br>
        <span class="filter_result_plug">Результаты поиска: </span>
        <span class="filter_result_header"> Детская коляска</span>
        
        <div class="filters_and_products">
            <div class="filters_box">
                <div class="cats">
                    <div class="filter_categories">
                        <div class="filter_categories__burger">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                        <span class="categories_header">Каталог товаров</span>
                    </div>
                    <ui-select 
                    :selected_option="'Детская комната'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 2'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 3'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 4'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 5'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 6'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 7'"
                    :options="options"
                    />
                    <ui-select 
                    :selected_option="'Детская комната 8'"
                    :options="options"
                    />
                </div>
                <div class="filters">
                    <div class="filter_categories">
                        <img src="@/assets/img/filter.png" alt="">&nbsp; &nbsp;
                        <span class="categories_header">Каталог товаров</span>
                    </div>
                    <div class="point_filters">

                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="price_available=!price_available"
                            >
                                <span class="subfilter_header">По цене:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!price_available">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="price_available">
                            </div>
                            
                            <div class="price_between_box" v-if="price_available">
                                <input type="number" name="">
                                <span class="separator">-</span>
                                <input type="number" name="">
                            </div>
                        </div>
                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="brand_available=!brand_available"
                            >
                                <span class="subfilter_header">Бренды:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!brand_available">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="brand_available">
                            </div>
                            
                            <div class="brands_box" v-if="brand_available">
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        Avent
                                    </span>
                                    
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        Omron
                                    </span>
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        NUK
                                    </span>
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                            </div>
                        </div>
                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="color_available=!color_available"
                            >
                                <span class="subfilter_header">По цветам:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!color_available">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="color_available">
                            </div>
                            
                            <div class="brands_box" v-if="color_available">
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        Black
                                    </span>
                                    
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        Red
                                    </span>
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        Purple
                                    </span>
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                                <label class="checkbox_input_container">
                                    <span class="checkbox_value">
                                        Yellow
                                    </span>
                                    <input type="checkbox">
                                    <span class="checkmark"></span>
                                </label><br>
                            </div>
                        </div>

                    </div>
                </div>
                
            </div>

            <div class="products_box">
                <div class="current_filters">
                    <div class="slug_and_close">
                        <h3>Активные фильтры</h3>
                        <div class="close">
                            
                            &nbsp; Очистить все
                        </div>
                    </div>
                    <hr>
                    <div class="selected_filters">
                        <div class="filter_row">
                            <span>Бренды:</span>
                            <div class="filter_with_close">
                                AVENT &nbsp; 
                                <img src="@/assets/img/clear.png" alt="">
                            </div>
                        </div>
                        <div class="filter_row">
                            <span>По цветам:</span>
                            <div class="filter_with_close">
                                Black &nbsp; 
                                <img src="@/assets/img/clear.png" alt="">
                            </div>
                            <div class="filter_with_close">
                                Red &nbsp; 
                                <img src="@/assets/img/clear.png" alt="">
                            </div>
                        </div>
                    </div>

                </div>
                <div class="products_count_and_sort_select">
                    <span>Найдено 1246 товаров</span>
                    <ui-select 
                    :purpose="'detail'"
                    v-model:selected_option="products_sort_option"
                    :options="['by newest', 'by latest']"
                    />
                </div>
                
                <div class="found_products">
                    <div class="swiper-slide">
                        <div class="sale_hit_new_box50">
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
                    </div>
                    <div class="swiper-slide">
                        <div class="sale_hit_new_boxnew">
                            NEW
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
                    </div>
                    <div class="swiper-slide">
                        <div class="sale_hit_new_boxnew">
                            NEW
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
                    </div>
                    <div class="swiper-slide">
                        <div class="sale_hit_new_boxhit">
                            HIT
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
                    </div>
                    
                </div>
                <ui-pagination 
                :pages_per_view="15"
                />
            </div>
            
        </div>

    </div>
    <ui-footer />
    

</template>

<script>
export default {
    data(){
        return {
            options: ['Option1', 'Option2', 'Option3', 'Option4', 'Option5'],
            price_available: false,
            brand_available: false,
            color_available: false,
            products_sort_option: 'by newest'
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Search and filter products')
    }
}
</script>

<style scoped>
    @import url('@/assets/css/product_filters.css');
</style>