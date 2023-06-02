<template>
    <div class="contact_us_box">
        <img src="@/assets/img/left_baby.png" alt="">
        <div class="form_box">
            <div class="form_in_line">
                <img src="@/assets/img/Logo2.png" alt="">
                <h1>Свяжитесь с нами</h1>
            </div>
            <p>Отправьте нам сообщение и мы ответим в ближайшее время</p>
            <form @submit.prevent="send_question" class="contact_us_form">
                <input v-model="mail_msg_name" type="text" placeholder="Ваше имя*">
                <input v-model="mail_msg_tel" type="tel" placeholder="Телефон">
                <input v-model="mail_msg_mail" type="email" placeholder="Электронная почта*">
                <textarea v-model="mail_msg_body" cols="30" rows="10" placeholder="Текст сообщения*">
                    
                </textarea>
                <button>
                    <img src="@/assets/img/telegram_icon.png" alt="">
                    Отправить сообщение
                </button>
            </form>
        </div>
        <img class="message_img" src="@/assets/img/Group_882.png" alt="">
        <img class="right_img" src="@/assets/img/Group_879.png" alt="">
    </div>
</template>

<script>
// Common component with form whose purpose get messages from users in backend email
import axios from 'axios';


export default {
    name: 'ContactUsBox',
    data(){
        return {
            mail_msg_name: '',
            mail_msg_tel: '',
            mail_msg_mail: '',
            mail_msg_body: '',
        }
    },
    methods: {

        send_question() {
            if (
                this.mail_msg_name.trim() &&
                this.mail_msg_mail.trim() &&
                this.mail_msg_body.trim()
            ) {
                const send = axios.post(`${this.$store.state.server_href}receive_mail`, this.$data)
                console.log(send.data);
            }
            
        }
    }
}
</script>

<style scoped>
.contact_us_box{
    position: relative;
    background: #D6F4FA;
    height: 610px;
}
.contact_us_box > img{
    height: 100%;
}
.form_box{
    position: absolute;
    bottom: 60px;
    top: 60px;
    right: 80px;
    display: flex;
    flex-direction: column;
    width: 40%;
    align-items: center;
}
.form_box p{
    margin-bottom: 15px;
}
.form_in_line{
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
}
.form_in_line h1{
    margin-left: 15px;
}
.contact_us_form input, .contact_us_form textarea{
    margin-bottom: 12px;
    background: white;
    border: 1px solid #74CCD8;
    border-radius: 40px;
    color: #B7B8C5;
    font-size: 14px;
    padding: 11px 20px;
    width: 100%;
    outline: none;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.contact_us_form textarea{
    border-radius: 20px;
}
.contact_us_form button{
    padding: 13px 30px;
    font-size: 15px;
    line-height: 20px;
    box-shadow: 0px 2px 4px rgba(51, 196, 223, 0.2);
    border-radius: 30px;
    color: white;
    background: #74CCD8;
    border:none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    margin: 15px auto;
}
.contact_us_form button img{
    margin-right: 10px;
}
.message_img{
    position: absolute;
    width: 112px;
    height: 112px !important;
    bottom: 60px;
    left: 35%;
}
.right_img{
    position: absolute;
    height: 226px !important;
    right: 0px;
    bottom: 120px;
}
</style>