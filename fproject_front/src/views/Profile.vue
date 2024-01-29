<template>
<ui-modal
class="mail_checking_modal"
v-model:modal_visible="mail_modal_visible_for_payment_method"
>
    <img src="@/assets/img/info.png" class="info_img">
    <br>
    <h3>Прежде чем оплатить заказ, убедитесь что указали существующий адрес ел. почты!</h3>
    <br>
    <span>
        Когда вы оплатите заказ вам будет выдана дата получения товаров в заказе, 
        иммено в эту дату вы получите письмо чтобы подтвердить что все товары дошли успешно. 
        Вам нужно будет перейти по ссылке в письме чтобы подтвердить получение товаров и поменять статус заказа на "полученный".
    </span>
    <br>
    <button class="approve_btn" @click="approveMailCheckingAndCloseModal">
        Оплатить
    </button>
    
</ui-modal>
<ui-modal
class="refund_reason_modal"
v-model:modal_visible="refund_modal_visible"
>
    <h3>Напишите пожалуйста о причине возврата средств</h3>
    <textarea 
    cols="30"
    rows="7"
    placeholder="Текст причины*"
    v-model="refund_reason_text"
    :style="{
        outline: textarea_outline
    }"
    ></textarea>
    <button class="refund_btn" @click="refundPaymentAfterReason">
        Отправить причину и возвратить средства
    </button>
    
</ui-modal>
<div class="profile_container">
    <ui-bread-crumbs />
    <div class="profile_info_and_content">
        <div class="profile_info">
            <a class="exit_acc" @click="exitAcc">Выйти</a>
            <div v-if="user_mini_info" class="user_photo">
                <img 
                v-if="!['None', 'null', null].includes(user_mini_info?.photo)"
                :src="$store.getters.getImageUrl(user_mini_info?.photo)"
                >
                <div
                v-else
                class="user_no_img"
                >
                    {{ user_mini_info?.first_name.charAt(0).toUpperCase() }}
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
            <h3 
            style="padding: 0px 30px;"
            v-if="user_additional_info"
            >
                {{ user_mini_info?.first_name }}
                {{ user_additional_info['last_name'] }}
            </h3>
            <div class="profile_tabs">
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: checkStoreProfileContent('orders') || tabs_visibility['orders_visible']
                }"
                @mouseenter="setTabVisible('orders')"
                @mouseleave="setTabInvisible('orders')"
                @click="profileWhatVisible('orders')"
                >
                    <img 
                    src="@/assets/img/cart_blue.png" 
                    v-if="!checkStoreProfileContent('orders') && !tabs_visibility['orders_visible']"
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
                    profile_tab_clicked: checkStoreProfileContent('liked') || tabs_visibility['liked_visible']
                }"
                @mouseenter="setTabVisible('liked')"
                @mouseleave="setTabInvisible('liked')"
                @click="profileWhatVisible('liked')"
                >
                    <img 
                    src="@/assets/img/like_blue.png" 
                    v-if="!checkStoreProfileContent('liked') && !tabs_visibility['liked_visible']"
                    > 
                    <img src="@/assets/img/like_white.png" v-else> 
                    <span>&nbsp; &nbsp;</span>
                    <span>Список желаний</span>
                </div>
                <div 
                :class="{
                    profile_tab: true,
                    profile_tab_clicked: checkStoreProfileContent('sales') || tabs_visibility['sales_visible']
                }"
                @mouseenter="setTabVisible('sales')"
                @mouseleave="setTabInvisible('sales')"
                @click="profileWhatVisible('sales')"
                >
                    <img 
                    src="@/assets/img/sale_blue.png" 
                    v-if="!checkStoreProfileContent('sales') && !tabs_visibility['sales_visible']"
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
                    profile_tab_clicked: checkStoreProfileContent('register') || tabs_visibility['register_visible']
                }"
                @mouseenter="setTabVisible('register')"
                @mouseleave="setTabInvisible('register')"
                @click="profileWhatVisible('register')"
                >
                    <img 
                    src="@/assets/img/settings_blue.png" 
                    v-if="!checkStoreProfileContent('register') && !tabs_visibility['register_visible']"
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
            <div v-if="user_additional_info && user_additional_info['orders']?.length >= 1">
                <h2>История Ваших заказов</h2><br>
                <div class="card_product_explain">
                    <span>№ заказа</span>
                    <span>Дата получения</span>
                    <span>Колл-во</span>
                    <span>Сумма</span>
                    <span>Статус</span>
                    <img src="@/assets/img/Vector_42.png">
                </div>
                <ui-select
                :purpose="'cart_products'"
                v-for="order in user_additional_info['orders']"
                >
                    <template #row_info>
                        <span>{{ order['code'] }}</span>
                        <span>{{ order['arrive_date'] || '-' }}</span>
                        <span>{{ order['order_products'].length }}</span>
                        <span>{{ order['total_price'] }}$</span>
                        <span :class="getClassForOrderStatus(order['status'] || 'rejected')">{{ order['status'] || '-' }}</span>
                        <img src="@/assets/img/Vector_42.png" alt="">
                    </template>
                    <template #products>
                        <div class="pay_variants" v-if="order['payment_date']">
                            <p>дата оплаты: {{ order['payment_date'] }}</p>
                        </div>
                        <div class="pay_variants" v-if="!order.status && order['order_products']?.length">
                            <ui-paypal-btns 
                            @click="mail_modal_visible_for_payment_method = 'paypal'"
                            :approve_mail_checking="mail_checking_approved_for['paypal']"
                            :order_pk="order['id']"
                            :purpose="'pay'"
                            />
                            <ui-stripe-btns 
                            @click="mail_modal_visible_for_payment_method = 'stripe'"
                            @received_changed_order="replaceOrder"
                            :approve_mail_checking="mail_checking_approved_for['stripe']"
                            :order_pk="order['id']"
                            :purpose="'pay'"
                            />
                        </div>
                        <div class="pay_variants" v-if="order.status==='pending'">
                            <ui-paypal-btns 
                            v-if="order.payment_method_name === 'paypal'"
                            @received_changed_order="replaceOrder"
                            @click="refund_modal_visible = true"
                            :refund_payment_after_reason="refund_reason_pointed"
                            :order_pk="order['id']"
                            :purpose="'refund'"
                            />
                            <ui-stripe-btns
                            v-else-if="order.payment_method_name === 'stripe'"
                            :order_pk="order['id']"
                            :purpose="'refund'"
                            @received_changed_order="replaceOrder"
                            @click="refund_modal_visible = true"
                            :refund_payment_after_reason="refund_reason_pointed"
                            />
                        </div>
                        <div 
                        class="cart_product"
                        v-for="product in order['order_products']"
                        @click="$router.push(`/products/${product['id']}`)"
                        >
                            <img :src="$store.getters.getImageUrl(product['images'][0].image)">
                            <div class="product_name_and_price">
                                <div class="product_info">
                                    <h3>{{ product['name'] }}</h3>
                                    <p>Код товара: <span>{{ product['code'] }}</span></p>&nbsp;
                                    <p>Цвет: <span>{{ product['color'] }}</span></p>&nbsp;
                                    <p>Разрешение: <span>{{ product['resolution'] }}</span></p>&nbsp;
                                    <p>Количевство: <span>{{ product['quantity'] }}</span></p>&nbsp;
                                </div>
                                <div style="text-align: center;">
                                    <h2>{{ product['total_price'] }}$</h2>
                                    <button 
                                    class="remove_order_product_btn"
                                    v-if="!order.status"
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
            <div v-if="user_additional_info && user_additional_info.liked_products?.length">
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

        <div class="register_form"
        v-else-if="checkStoreProfileContent('register')"
        >
            
            <form 
            @submit.prevent="editAcc"
            >
                <h2>Редактированние личных данных</h2>
                <br>
                <div class="user_info_inputs">
                    <input v-model="update_acc_fields.email" type="email" placeholder="Электронная почта*">
                    <span class="error_message">{{ update_acc_fields_errors.email }}</span>
                    <input v-model="update_acc_fields.tel" type="number" placeholder="Номер телефона*">
                    <span class="error_message">{{ update_acc_fields_errors.tel }}</span>
                    <div class="first_last_name_row_inputs">
                        <div class="fn_input_wrapper">
                            <input v-model="update_acc_fields.first_name" type="text" placeholder="Ваше имя*">
                            <span class="error_message">{{ update_acc_fields_errors.first_name }}</span>
                        </div>
                        <div class="fn_input_wrapper">
                            <input v-model="update_acc_fields.last_name" type="text" placeholder="Фамилия*">
                            <span class="error_message">{{ update_acc_fields_errors.last_name }}</span>
                        </div>
                    
                    </div>
                
                    <input v-model="update_acc_fields.password" type="password" placeholder="Придумайте новый пароль*">
                    <span class="error_message">{{ update_acc_fields_errors.password }}</span>
                </div>
                <br>
                <h2>Адрес для получения доставки</h2>
                <div class="adresses">
                    <input v-model="update_acc_fields.city" type="text" placeholder="Город / Село / Пагаст / Район*">
                    <span class="error_message">{{ update_acc_fields_errors.city }}</span>
                    <input v-model="update_acc_fields.street" type="text" placeholder="Улица / Дом / Квартира*">
                    <span class="error_message">{{ update_acc_fields_errors.street }}</span>
                    <input v-model="update_acc_fields.post_code" type="number" placeholder="Почтовый индекс*">
                    <span class="error_message">{{ update_acc_fields_errors.post_code }}</span>
                </div>
                <label class="to_mail_list">
                    <input 
                    v-model="update_acc_fields.in_mailing_list" 
                    :checked="update_acc_fields.in_mailing_list"
                    @click="update_acc_fields.in_mailing_list=!update_acc_fields.in_mailing_list"
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
                    <img src="@/assets/img/ok3.png"> &nbsp;
                    {{ edit_acc_btn_text }}
                </button>
                <br><br>
            </form>
            <add-card-form 
            v-model:user_stripe_payment="user_additional_info['stripe_payment']"
            />
            <br />
            <span class="del_acc" @click="deleteAcc">
                Удалить аккаунт
            </span>
        </div>

    </div>
</div>
<mini-products-slider 
style="padding: 60px 7%;background: rgb(244, 245, 249);"
v-if="user_additional_info.viewed10_products?.length"
>
    <template #header>
        <h1>Вы уже смотрели</h1>
    </template>
    
    <ui-slide
    v-for="product in user_additional_info.viewed10_products"
    :key="product.id"
    :product="product"
    @add_liked_product="pushLikedProduct"
    >
    </ui-slide>
</mini-products-slider> 
<div class="history_empty" v-else>
    <h2>История пуста</h2>
</div>


</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount, watch } from 'vue'


const emit = defineEmits()
const store = useStore()
const route = useRoute()
const router = useRouter()

const user_mini_info = reactive(JSON.parse(localStorage.getItem('current_user')) || {})
const user_additional_info = reactive({})
const tabs_visibility = reactive({
    'orders_visible': false,
    'liked_visible': false,
    'sales_visible': false,
    'register_visible': false,
})
const mail_checking_approved_for = reactive({
    'paypal': false,
    'stripe': false,
})
const mail_modal_visible_for_payment_method = ref(false)
const refund_modal_visible = ref(false)
const refund_reason_pointed = ref(false)
const refund_reason_text = ref('')
const textarea_outline = ref('2px solid #74CCD8')
const edit_acc_btn_text = ref('Сохранить изменения')
const current_sale = ref('>= 25%')
const current_pagination_page = ref(1)
const sailed_products = reactive({})
const update_acc_fields = reactive({})
const update_acc_fields_errors = ref({}) // ref used for easy assigning empty Object by .value={}
const edit_acc_btn = ref(null)


onBeforeMount(async () => {
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Profile')
    
    // If user is not authed redirect to /register
    if (!user_mini_info?.id){
        router.push(`/register`)
        return
    }
    
    // Get user additional info and sailed products(if sales tab active)
    Object.assign(
        user_additional_info,
        await store.dispatch(
            'commonRequestWithAuth', 
            {
                method: 'get',
                url_after_server_domain: `users_profile/${user_mini_info?.id}`,
            }
        )
    )
    if (checkStoreProfileContent('sales')) await getSailedProducts()
      

    // Set all values in edit account inputs.
    const exclude_update_acc_fields = ['orders', 'liked_products', 'viewed10_products']
    Object.assign(update_acc_fields, user_additional_info)
    update_acc_fields['first_name'] = user_mini_info?.first_name
    exclude_update_acc_fields.forEach(field => delete update_acc_fields[field])
})


watch(
    current_sale,
    async newValue => {
        // If sale changed paginate to first page and get relevant sailed products
        current_pagination_page.value = 1

        const new_sailed_products = await store.dispatch(
            'commonRequestWithAuth', 
            {
                method: 'get',
                url_after_server_domain: `filter_products?sale_new_hit_by_sailed=${newValue.slice(3, 5)}&pg=1`,
            }
        )

        Object.assign(sailed_products, new_sailed_products)
    }
)


async function profileWhatVisible(visible_tab){
    // set tab clicked by name
    store.commit('setProfileContent', visible_tab)
    if (visible_tab !== 'sales') return

    await getSailedProducts()
    current_pagination_page.value = 1 
    current_sale.value = '>= 25%'
}
function setTabVisible(tab_name){
    // set tab _visible = true by name for styles
    tabs_visibility[`${tab_name}_visible`] = true
}
function setTabInvisible(tab_name){
    // set tab _visible = false by name for disable style
    tabs_visibility[`${tab_name}_visible`] = false
    
}
function checkStoreProfileContent(value){
    return store.state.profile_content === value
}
async function approveMailCheckingAndCloseModal(){
    if(
        mail_modal_visible_for_payment_method.value === 'stripe' && 
        !user_additional_info['stripe_payment']
    ){
        await profileWhatVisible('register')
        await document.querySelector(".payment_form").scrollIntoView({
            behavior: "smooth",
            block: "center"
        })
    }else{
        mail_checking_approved_for[mail_modal_visible_for_payment_method.value] = true
    }
    mail_modal_visible_for_payment_method.value = false
}
function refundPaymentAfterReason(){
    if (refund_reason_text.value.trim()) {
        refund_modal_visible.value = false
        refund_reason_pointed.value = true
    }else{
        textarea_outline.value = '2px solid red'
        setTimeout(() => {
            textarea_outline.value = '2px solid #74CCD8'
        }, 2000);
    }
    
}
function getClassForOrderStatus(order_status){
    const classes = {
        pending: 'order_statuswait',
        received: 'order_statuspayed',
        rejected: 'order_statusclosed',
    }
    return classes[order_status]
}
async function changePhoto(e){
    
    const photoData = new FormData();
    photoData.append('photo', e.target.files[0], e.target.files[0].name);
    const changed_acc = await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'patch',
            url_after_server_domain: `users_edit_or_del/${user_mini_info?.id}`,
            data: photoData
        }
    )
    user_mini_info.photo = changed_acc.photo
    emit('rerender_header')
}
function pushLikedProduct(product){
    // If product not in liked list, add it, update header
    if (!store.state.liked_products_names.has(product.name)) {
        user_additional_info.liked_products.push(product)
    }
}
function removeLikedProduct(product){
    // Remove product from liked list, update header, del product name from liked_products_names vuex state
    user_additional_info.liked_products=user_additional_info.liked_products.filter(el => el !== product)
}
async function delOrderProduct(e, product){
    // Del product from order wthout status and update ui by replacing order without status, received from server,
    // if after delete product order will be empty - del order,
    // update order product count in header component
    e.stopPropagation()
    const updated_order_without_status = await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'delete',
            url_after_server_domain: `users_add_or_del_order_product/${user_mini_info?.id}/${product['id']}`,
        }
    )
    if (!('detail' in updated_order_without_status)) {
        user_additional_info['orders'][0] = updated_order_without_status
    } else if(updated_order_without_status['detail'] === 'Order deleted') {
        user_additional_info['orders'] = user_additional_info['orders'].filter(
            order => order.status 
        )
    }
    store.commit('delOrderedProduct', product['name'])

}
function replaceOrder(changed_order){
    // replace refunded order(received from server) for valid ui
    for (let i = 0; i < user_additional_info['orders'].length; i++) {
        if (user_additional_info['orders'][i].id === changed_order.id){
            user_additional_info['orders'][i] = changed_order
            break
        }
    }
}
async function getSailedProducts(){
    // If tab is sales, lazy upload relevant products(without sale limit for first)
    if (!checkStoreProfileContent('sales')) return

    const new_sailed_products = await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'get',
            url_after_server_domain: `filter_products?sale_new_hit_by_sailed=all_sailed`,
         
        }
    )

    Object.assign(sailed_products, new_sailed_products)
    
}
async function getFilteredSailedProducts(paginated_to){
    let sale = 
    current_sale.value === 'Select sale' ? 
    'sale_new_hit_by_sailed=all_sailed' : 
    `sale_new_hit_by_sailed=${current_sale.value.slice(3, 5)}`
    
    const new_sailed_products = await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'get',
            url_after_server_domain: `filter_products?${sale}&pg=${paginated_to}`,
        }
    )

    Object.assign(sailed_products, new_sailed_products)
    current_pagination_page.value = paginated_to
}
function updateUserInfo(obj){
    // Update few user info given from inputs after successfully edit acc(and before mount)
    user_mini_info.first_name = obj['first_name']
    user_additional_info['last_name'] = obj['last_name']
    user_additional_info['email'] = obj['email']
    user_additional_info['tel'] = obj['tel']
    user_additional_info['city'] = obj['city']
    user_additional_info['street'] = obj['street']
    user_additional_info['post_code'] = obj['post_code']
    user_additional_info['in_mailing_list'] = obj['in_mailing_list']
}
async function editAcc(){
    // Edit acc and update header, user_mini_info, user_additional_info.
    // If any input are invalid show error in ui
    const changed_acc = await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'patch',
            url_after_server_domain: `users_edit_or_del/${user_mini_info?.id}`,
            data: update_acc_fields
        }
    )
    if (![400, 401].includes(changed_acc.response?.status)) {
        emit('rerender_header')
        updateUserInfo(changed_acc)
        update_acc_fields_errors.value = {}

        edit_acc_btn_text.value = 'Сохранено!'
        edit_acc_btn.value.style.background = '#90de63'
        setTimeout(() => {
            edit_acc_btn_text.value = 'Сохранить изменения'
            edit_acc_btn.value.style.background = '#74CCD8'
        }, 2000);
    }else{
        Object.assign(update_acc_fields_errors.value, changed_acc.response.data)
        for (const [key, value] of Object.entries(changed_acc.response.data)) {
            update_acc_fields_errors.value[key] = value[0]
        }
    }
    
    
}
async function deleteAcc(){
    await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'delete',
            url_after_server_domain: `users_edit_or_del/${user_mini_info?.id}`,
        }
    )
    store.getters.delAllDataFromLocalStorage()
    router.push('/register')
    emit('rerender_header')
}
function exitAcc(){
    // Delete all data in localStorage(tokens, user info) and redirect to /register
    store.getters.delAllDataFromLocalStorage()
    emit('rerender_header')
    router.push('/register')
}

</script>

<style scoped>
    @import url('@/assets/css/profile.css');
</style>
