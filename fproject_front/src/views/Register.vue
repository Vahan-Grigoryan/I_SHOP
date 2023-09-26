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
            <span>Или</span>
            <br>
            <a 
            :href="`${$store.state.server_href}oauth_registration?from_url=${$route.path}`"
            class="google_reg_btn"
            >
                <img src="@/assets/img/Google.png"> &nbsp;
                Зарегестрироватся через Google
            </a>
            
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

<script>
import axios from 'axios'

export default {
    data(){
        return {
            email: '',
            first_name: '',
            last_name: '',
            password: '',
            tel: '',
            city: '',
            street: '',
            post_code: '',
            in_mailing_list: false,
            email_error: '',
            first_name_error: '',
            last_name_error: '',
            password_error: '',
            tel_error: '',
            city_error: '',
            street_error: '',
            post_code_error: '',
        }
    },
    methods: {
        async register_user(){
            // Del old error fields,
            // Get user info, tokens,
            //  if error show errors to user
            // Set user info, tokens data in localStorage( with setTokensInLS(), setUserInLS() ),
            // Emit event for rerender header,
            // Set all fields values to empty (error fields includes),
            // Redirect to /profile/:id
            try{
                Object.keys(this.$data).forEach( key => {
                    if (key.endsWith('error')) {
                        this.$data[key] = ''
                    }
                })
                const user = await axios.post(`${this.$store.state.server_href}registration`, this.$data)
                const tokens = await axios.post(`${this.$store.state.server_href}auth/jwt/create`, this.$data)
                
                this.$store.getters.setTokensInLS(tokens.data)
                this.$store.getters.setUserInLS(user.data)

                this.$emit('rerender_header')
                Object.keys(this.$data).forEach( key => this.$data[key] = '')
                this.$router.push(`/profile/${user.data['id']}`)
            }catch(error){
                const response = error.response.data
                Object.keys(response).forEach( key => this.$data[`${key}_error`] = response[key][0])
            }
        },
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Registration')

        // If user authed auto-redirect to /profile/:id
        const user = JSON.parse(localStorage.getItem('current_user'))
        if (user) {
            this.$router.push(`/profile/${user['id']}`)
        }
    },
}
</script>

<style scoped>
    @import url('@/assets/css/register.css');
</style>
