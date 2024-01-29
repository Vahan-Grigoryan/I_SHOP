<template>
<ui-bread-crumbs style="padding-left: 5%;margin-top: 15px;" />
<div class="reg_container">
    <h1>Регистрация аккаунта</h1>
    <span>С помощью регистраци Вы сможете покупать у нас в 3 раза быстрее</span>
    <div class="register_form_and_register_procs">
        <form class="register_form">
            <h2>Заполните форму регистрации</h2>
            <br>
            <div class="user_info_inputs">
                <input v-model="fields['email']" type="email" placeholder="Электронная почта*">
                <span class="error_message">{{ fields_errors['email'] }}</span>
                <input v-model="fields['tel']" type="number" placeholder="Номер телефона*">
                <span class="error_message">{{ fields_errors['tel'] }}</span>
                <div class="first_last_name_row_inputs">
                    <div class="fn_input_wrapper">
                        <input v-model="fields['first_name']" type="text" placeholder="Ваше имя*">
                        <span class="error_message">{{ fields_errors['first_name'] }}</span>
                    </div>
                    <div class="fn_input_wrapper">
                        <input v-model="fields['last_name']" type="text" placeholder="Фамилия*">
                        <span class="error_message">{{ fields_errors['last_name'] }}</span>
                    </div>
                    
                </div>
                
                <input v-model="fields['password']" type="password" placeholder="Придумайте пароль*">
                <span class="error_message">{{ fields_errors['password'] }}</span>
            </div>
            <br>
            <span>Или</span>
            <br>
            <a 
            :href="`${$store.state.server_href}oauth_registration?from_url=${$route.path}`"
            class="google_reg_btn"
            >
                <img src="@/assets/img/Google.png"> &nbsp;
                Войти через Google
            </a>
            
            <h2>Адрес для получения доставки</h2>
            <div class="adresses">
                <input v-model="fields['city']" type="text" placeholder="Город / Село / Пагаст / Район*">
                <span class="error_message">{{ fields_errors['city'] }}</span>
                <input v-model="fields['street']" type="text" placeholder="Улица / Дом / Квартира*">
                <span class="error_message">{{ fields_errors['street'] }}</span>
                <input v-model="fields['post_code']" type="number" placeholder="Почтовый индекс*">
                <span class="error_message">{{ fields_errors['post_code'] }}</span>
            </div>
            <label class="to_mail_list">
                <input v-model="fields['in_mailing_list']" type="checkbox" />
                &nbsp;
                Оформить подписку на рассылку писем
            </label>
            <button 
            type="submit" 
            class="reg_btn"
            @click.prevent="register_user"
            >
                <img src="@/assets/img/ok3.png"> &nbsp;
                Зарегестрироватся
            </button>
        </form>
        <div class="register_procs">
            <h2>Преимущества регистрации</h2>
            <div class="subproc">
                <img src="@/assets/img/Group_939.png" alt=""><br>
                <span class="header">Купон бесплатной доставки каждый месяц</span>
            </div>
            <div class="subproc">
                <img src="@/assets/img/Group_956.png" alt=""><br>
                <span class="header">Акции и скидки для постоянных покупателей</span>
            </div>
            <div class="subproc">
                <img src="@/assets/img/Rocket.png" alt=""><br>
                <span class="header">Скорость покупки</span>
            </div>
        </div>
    </div>
</div>

</template>

<script setup>
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount } from 'vue'


const store = useStore()
const router = useRouter()
const emit = defineEmits()

const fields = reactive({
    'email': '',
    'first_name': '',
    'last_name': '',
    'password': '',
    'tel': '',
    'city': '',
    'street': '',
    'post_code': '',
    'in_mailing_list': false,
})
const fields_errors = reactive({
    'email': '',
    'first_name': '',
    'last_name': '',
    'password': '',
    'tel': '',
    'city': '',
    'street': '',
    'post_code': '',
})


onBeforeMount(() => {
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Registration')

    // If user authed auto-redirect to /profile/:id
    const user = JSON.parse(localStorage.getItem('current_user'))
    if (user) {
        router.push(`/profile/${user['id']}`)
    }
})


async function register_user(){
    // Del old error fields,
    // Get user info, tokens,
    //  if error show errors to user
    // Set user info, tokens data in localStorage( with setTokensInLS(), setUserInLS() ),
    // Emit event for rerender header,
    // Set all fields values to empty (error fields includes),
    // Redirect to /profile/:id
    try{
        Object.keys(fields_errors).forEach(key => fields_errors[key] = '')

        const user = await axios.post(`${store.state.server_href}registration`, fields)
        const tokens = await axios.post(
            `${store.state.server_href}auth/jwt/create`,
            {
                'email': fields['email'],
                'password': fields['password'],
            }
        )
        
        store.getters.setTokensInLS(tokens.data)
        store.getters.setUserInLS(user.data)

        emit('rerender_header')
        Object.keys(fields).forEach(key => fields[key] = '')
        router.push(`/profile/${user.data['id']}`)
    }catch(error){
        const response = error.response.data
        Object.keys(response).forEach( key => fields_errors[key] = response[key][0])
    }
}

</script>

<style scoped>
    @import url('@/assets/css/register.css');
</style>
