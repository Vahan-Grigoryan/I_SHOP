<template>
<div class="profile_container">
    <ui-bread-crumbs />
    <div class="profile_info_and_content">
        <div class="profile_info">
            <a class="exit_acc" @click="exitAcc">Выйти</a>
            <div v-if="user_mini_info" class="user_photo">
                <img 
                v-if="!['None', 'null', null].includes(user_mini_info.photo)"
                :src="$store.getters.getImageUrl(user_mini_info.photo)"
                >
                <div
                v-else
                class="user_no_img"
                >
                    {{ user_mini_info.first_name.charAt(0).toUpperCase() }}
                </div>
            </div>
            <br>
            <div class="change_img">
                <label>
                    <img src="@/assets/img/photo-camera.png"> &nbsp; &nbsp;
                    <span>Изменить</span>
                    <input 
                    type="file" 
                    accept="image/png, image/jpeg, image/webp"
                    hidden 
                    @change="changePhoto"
                    >
                </label>
                
            </div>
            <h3 style="padding: 0px 30px;">
                {{ user_mini_info['first_name'] }}
                {{ user_additional_info['last_name'] }}
            </h3>
            <div class="profile_tabs">
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: checkStoreProfileContent('orders') || orders_visible
                }"
                @mouseenter="setTabVisible('orders')"
                @mouseleave="setTabInvisible('orders')"
                @click="profileWhatVisible('orders')"
                >
                    <img 
                    src="@/assets/img/cart_blue.png" 
                    v-if="!checkStoreProfileContent('orders') && !orders_visible"
                    > 
                    <img 
                    src="@/assets/img/cart_white.png" 
                    v-else
                    > 
                    <span>&nbsp; &nbsp;</span>
                    <span>Мои заказы</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: checkStoreProfileContent('liked') || liked_visible
                }"
                @mouseenter="setTabVisible('liked')"
                @mouseleave="setTabInvisible('liked')"
                @click="profileWhatVisible('liked')"
                >
                    <img 
                    src="@/assets/img/like_blue.png" 
                    v-if="!checkStoreProfileContent('liked') && !liked_visible"
                    > 
                    <img src="@/assets/img/like_white.png" v-else> 
                    <span>&nbsp; &nbsp;</span>
                    <span>Список желаний</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: checkStoreProfileContent('sales') || sales_visible
                }"
                @mouseenter="setTabVisible('sales')"
                @mouseleave="setTabInvisible('sales')"
                @click="profileWhatVisible('sales')"
                >
                    <img 
                    src="@/assets/img/sale_blue.png" 
                    v-if="!checkStoreProfileContent('sales') && !sales_visible"
                    > 
                    <img 
                    src="@/assets/img/sale_white.png" 
                    v-else
                    > 
                    <span>&nbsp; &nbsp;</span>
                    <span>Акции и скидки</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: checkStoreProfileContent('register') || register_visible
                }"
                @mouseenter="setTabVisible('register')"
                @mouseleave="setTabInvisible('register')"
                @click="profileWhatVisible('register')"
                >
                    <img 
                    src="@/assets/img/settings_blue.png" 
                    v-if="!checkStoreProfileContent('register') && !register_visible"
                    > 
                    <img 
                    src="@/assets/img/settings_white.png" 
                    v-else
                    > 
                    <span>&nbsp; &nbsp;</span>
                    <span>Настройки профиля</span>
                </div>
            </div>
            
        </div>

        <div class="profile_content_orders" v-if="checkStoreProfileContent('orders')">
            <div v-if="user_additional_info['orders'].length >= 1">
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
                v-for="order in user_additional_info['orders']"
                >
                    <template #row_info>
                        <span>{{ order['code'] }}</span>
                        <span>{{ order['payment_date'] || '-' }}</span>
                        <span>{{ order['order_products'].length }}</span>
                        <span>{{ order['total_prices_sum'] }}$</span>
                        <span :class="getClassForOrderStatus(order['status'])">{{ order['status'] }}</span>
                        <img src="@/assets/img/Vector_42.png" alt="">
                    </template>
                    <template #products>
                        <div 
                        class="cart_product"
                        v-for="product in order['order_products']"
                        @click="$router.push(`/products/${product['id']}`)"
                        >
                            <img :src="$store.getters.getImageUrl(product['images'][0].image)">
                            <div class="product_name_and_price">
                                <div class="product_info">
                                    <h3>{{ product['name'] }}</h3>
                                    <p>Код товара: <span>{{ product['code'] }}</span></p>
                                </div>
                                <div style="text-align: center;">
                                    <h2>{{ product['price'] }}$</h2>
                                    <button 
                                    class="remove_order_product_btn"
                                    v-if="order.status === 'pending'"
                                    @click="(e) => delOrderProduct(e, product)"
                                    >Убрать</button>
                                </div>
                            </div>
                        </div>
                    </template>
                </ui-select>
            </div>
            <div class="profile_empty" v-else>
                <ui-profile-empty 
                :header="'У вас пока нет заказов'"
                :content="'Давайте исправим это! Сделайте свою первую покупку в нашем магазине прямо сейчас.'"
                :btn_content="'Смотреть каталог'"
                /> 
            </div>
            
            
        </div>
        <div class="profile_content_liked" v-else-if="checkStoreProfileContent('liked')">
            <div v-if="user_additional_info.liked_products.length">
                <h1>Список моих желаний</h1><br>
                <div class="liked_products">
                    <ui-slide
                    v-for="product in user_additional_info.liked_products"
                    :key="product.id"
                    :product="product"
                    :top_right_btn_purpose="'delete'"
                    @del_liked_product="removeLikedProduct"
                    >
                    </ui-slide>
                </div>
            </div>
            <div class="profile_empty" v-else>
                <ui-profile-empty 
                :header="'У вас пока нет списка пожеланий'"
                :content="'Самое время это исправить и создать свой первый список из широкого ассортимента наших товаров ;)'"
                :btn_content="'Смотреть каталог'"
                /> 
            </div>
        </div>
        <div class="profile_content_sales" v-else-if="checkStoreProfileContent('sales')">
            <h1>Актуальные акции и скидки</h1>
            <ui-select 
            :purpose="'detail'"
            v-model:selected_option="current_sale"
            :options="['>= 25%', '>= 50%', '>= 75%']"
            />
            <div class="liked_products">
                <ui-slide
                v-for="product in sailed_products.results"
                :key="product.id"
                :product="product"
                @add_liked_product="pushLikedProduct"
                @rerender_header="$emit('rerender_header')"
                >
                </ui-slide>
            </div>
            <br><br>
            <ui-pagination
            :pages="$store.getters.calculatePagesCount(sailed_products.count)"
            @paginated_to="getFilteredSailedProducts"
            v-model:page_active="current_pagination_page"
            />
        </div>
        <form 
        class="register_form" 
        v-else-if="checkStoreProfileContent('register')"
        @submit.prevent="editAcc"
        >
            <h2>Редактированние личных данных</h2>
            <br>
            <div class="user_info_inputs">
                <input v-model="fields.email" type="email" placeholder="Электронная почта*">
                <span class="error_message">{{ fields_errors.email }}</span>
                <input v-model="fields.tel" type="number" placeholder="Номер телефона*">
                <span class="error_message">{{ fields_errors.tel }}</span>
                <div class="first_last_name_row_inputs">
                    <div class="fn_input_wrapper">
                        <input v-model="fields.first_name" type="text" placeholder="Ваше имя*">
                        <span class="error_message">{{ fields_errors.first_name }}</span>
                    </div>
                    <div class="fn_input_wrapper">
                        <input v-model="fields.last_name" type="text" placeholder="Фамилия*">
                        <span class="error_message">{{ fields_errors.last_name }}</span>
                    </div>
                    
                </div>
                
                <input v-model="fields.password" type="password" placeholder="Придумайте новый пароль*">
                <span class="error_message">{{ fields_errors.password }}</span>
            </div>
            <br>
            <h2>Адрес для получения доставки</h2>
            <div class="adresses">
                <input v-model="fields.city" type="text" placeholder="Город / Село / Пагаст / Район*">
                <span class="error_message">{{ fields_errors.city }}</span>
                <input v-model="fields.street" type="text" placeholder="Улица / Дом / Квартира*">
                <span class="error_message">{{ fields_errors.street }}</span>
                <input v-model="fields.post_code" type="number" placeholder="Почтовый индекс*">
                <span class="error_message">{{ fields_errors.post_code }}</span>
            </div>
            <label class="to_mail_list">
                <input 
                v-model="fields.in_mailing_list" 
                :checked="fields.in_mailing_list"
                @click="fields.in_mailing_list=!fields.in_mailing_list"
                type="checkbox" 
                />
                &nbsp;
                Оформить подписку на рассылку писем
            </label>
            <button 
            class="reg_btn"
            style="margin-top: 20px;"
            ref="edit_acc_btn"
            >
                <img src="@/assets/img/ok3.png" alt=""> &nbsp;
                {{ edit_acc_btn_text }}
            </button>
            <span class="del_acc" @click="deleteAcc">
                Удалить аккаунт
            </span>
        </form>
        
    </div>
</div>
<mini-products-slider 
style="padding: 60px 7%;background: rgb(244, 245, 249);"
v-if="user_additional_info.viewed10_products.length"
>
    <template #header>
        <h1>Вы уже смотрели</h1>
    </template>
    
    <ui-slide
    v-for="product in user_additional_info.viewed10_products"
    :key="product.id"
    :product="product"
    @add_liked_product="pushLikedProduct"
    @rerender_header="$emit('rerender_header')"
    >
    </ui-slide>
</mini-products-slider> 
<div class="history_empty" v-else>
    <h2>История пуста</h2>
</div>


</template>

<script>
import emitsForApp from '@/mixins/emitsForApp'

export default {
    data(){
        return {
            user_mini_info: JSON.parse(localStorage.getItem('current_user')),
            user_additional_info: null,
            orders_visible: false,
            liked_visible: false,
            sales_visible: false,
            register_visible: false,

            edit_acc_btn_text: 'Сохранить изменения',
            
            current_sale: '>= 25%',
            current_pagination_page: 1,
            sailed_products: [],
            fields: {},
            fields_errors: {}
        }
    },
    mixins: [emitsForApp],
    methods: {
        async profileWhatVisible(visible_tab){
            // set tab clicked by name
            this.$store.commit('setProfileContent', visible_tab)
            this.current_pagination_page = 1 
            this.current_sale = '>= 25%'
            if (visible_tab === 'sales') await this.getSailedProducts()
        },
        setTabVisible(tab_name){
            // set tab _visible = true by name for styles
            this.$data[`${tab_name}_visible`] = true
        },
        setTabInvisible(tab_name){
            // set tab _visible = false by name for disable style
            this.$data[`${tab_name}_visible`] = false
            
        },
        checkStoreProfileContent(value){
            return this.$store.state.profile_content === value
        },
        getClassForOrderStatus(order_status){
            const classes = {
                pending: 'order_statuswait',
                payed: 'order_statuspayed',
                rejected: 'order_statusclosed',
            }
            return classes[order_status]
        },
        async changePhoto(e){
            
            const photoData = new FormData();
            photoData.append('photo', e.target.files[0], e.target.files[0].name);
            const changed_acc = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'patch',
                    url_after_server_domain: `users_edit_or_del/${this.user_mini_info['id']}`,
                    data: photoData
                }
            )
            this.user_mini_info.photo = changed_acc.photo
            this.$emit('rerender_header')
        },
        pushLikedProduct(product){
            // If product not in liked list, add it, update header
            if (!this.$store.state.liked_products_names.includes(product.name)) {
                this.user_additional_info.liked_products.push(product)
            }
            this.$emit('rerender_header')
        },
        removeLikedProduct(product){
            // Remove product from liked list, update header, del product name from liked_products_names vuex state
            this.user_additional_info.liked_products=this.user_additional_info.liked_products.filter(el => el !== product)
            this.$emit('rerender_header')
        },
        async delOrderProduct(e, product){
            // Del product from pending order and update ui by changing pending order gettet from server,
            // update header order product count
            e.stopPropagation()
            const updated_pending_order = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'delete',
                    url_after_server_domain: `users_add_or_del_order_product/${this.user_mini_info['id']}/${product['id']}`,
                }
            )
            this.user_additional_info['orders'][0] = updated_pending_order
            this.$store.commit('delOrderedProduct', product['name'])
            this.$emit('rerender_header')

        },
        async getSailedProducts(){
            // If tab is sales, lazy upload relevant products(without sale limit for first)
            if (this.checkStoreProfileContent('sales')) {
                this.sailed_products = await this.$store.dispatch(
                    'commonRequestWithAuth', 
                    {
                        method: 'get',
                        url_after_server_domain: `filter_products?sale_new_hit_by_sailed=all_sailed`,
                        
                    }
                    
                )
            }
        },
        async getFilteredSailedProducts(paginated_to){
            let sale = 
            this.current_sale === 'Select sale' ? 
            'sale_new_hit_by_sailed=all_sailed' : 
            `sale_new_hit_by_sailed=${this.current_sale.slice(3, 5)}`
            
            this.sailed_products = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'get',
                    url_after_server_domain: `filter_products?${sale}&pg=${paginated_to}`,
                }
                
            )
            this.current_pagination_page = paginated_to
        },
        updateUserInfo(obj){
            // Update few user info given from inputs after successfully edit acc(and before mount)
            this.user_mini_info['first_name'] = obj['first_name']
            this.user_additional_info['last_name'] = obj['last_name']
            this.user_additional_info['email'] = obj['email']
            this.user_additional_info['tel'] = obj['tel']
            this.user_additional_info['city'] = obj['city']
            this.user_additional_info['street'] = obj['street']
            this.user_additional_info['post_code'] = obj['post_code']
            this.user_additional_info['in_mailing_list'] = obj['in_mailing_list']
        },
        async editAcc(){
            // Edit acc and apdate header, user_mini_info, user_additional_info.
            // If any input are invalid show error in ui
            const changed_acc = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'patch',
                    url_after_server_domain: `users_edit_or_del/${this.user_mini_info['id']}`,
                    data: this.fields
                }
            )
            if (![400, 401].includes(changed_acc.response?.status)) {
                this.$emit('rerender_header')
                this.updateUserInfo(changed_acc)
                this.fields_errors = {}

                this.edit_acc_btn_text = 'Сохранено!'
                this.$refs['edit_acc_btn'].style.background = '#90de63'
                setTimeout(() => {
                    this.edit_acc_btn_text = 'Сохранить изменения'
                    this.$refs['edit_acc_btn'].style.background = '#74CCD8'
                }, 2000);
            }else{
                this.fields_errors = changed_acc.response.data
                for (const [key, value] of Object.entries(changed_acc.response.data)) {
                    this.fields_errors[key] = value[0]
                }
            }
            
            
        },
        async deleteAcc(){
            await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'delete',
                    url_after_server_domain: `users_edit_or_del/${this.user_mini_info['id']}`,
                }
            )
            this.$store.getters.delAllDataFromLocalStorage()
            this.$router.push('/register')
            this.$emit('rerender_header')
        },
        exitAcc(){
            // Delete all data in localStorage(tokens, user info) and redirect to /register
            this.$store.getters.delAllDataFromLocalStorage()
            this.$emit('rerender_header')
            this.$router.push('/register')
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Profile')

        // If user is not authed redirect to /register
        if (!this.user_mini_info) this.$router.push(`/register`)

        // Get user additional info and sailed products(if sales tab active)
        this.user_additional_info = await this.$store.dispatch(
            'commonRequestWithAuth', 
            {
                method: 'get',
                url_after_server_domain: `users_profile/${this.user_mini_info['id']}`,
            }
        )
        if (this.checkStoreProfileContent('sales')) await this.getSailedProducts()

        // Set liked products names, ordered products names in vuex liked_products_names state,
        // for slide top right btn valid ui and product detail add_product_to_cart btn valid ui
        let products_names = []
        this.user_additional_info.liked_products.forEach(p => products_names.push(p.name))
        this.$store.state.liked_products_names = products_names
        if (this.user_additional_info['orders'].length) {
            let ordered_products_names = []
            this.user_additional_info['orders'][0]['order_products'].forEach( p => ordered_products_names.push(p.name) )
            this.$store.state.ordered_products_names = ordered_products_names
        }
        
        // Set all values in edit account inputs.
        const exclude_fields = ['orders', 'liked_products', 'viewed10_products']
        this.fields = {...this.user_additional_info}
        this.fields['first_name'] = this.user_mini_info['first_name']
        exclude_fields.forEach(field => delete this.fields[field])

    },
    watch: {
        async current_sale(newValue){
            // If sale changed paginate to first page and get relevant sailed products
            this.current_pagination_page = 1
            this.sailed_products = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'get',
                    url_after_server_domain: `filter_products?sale_new_hit_by_sailed=${newValue.slice(3, 5)}&pg=1`,
                }
            )
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/css/profile.css');
</style>