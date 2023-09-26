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
                <input 
                v-model="mail_msg_name"
                :style="inputs_styles['name']"
                type="text"
                placeholder="Ваше имя для обращения к вам в ответном письме*"
                >
                <input 
                v-model="mail_msg_tel"
                type="tel"
                placeholder="Телефон"
                >
                <input 
                v-model="mail_msg_mail"
                :style="inputs_styles['mail']"
                type="email"
                placeholder="Электронная почта*"
                >
                <textarea 
                v-model="mail_msg_body"
                :style="inputs_styles['body']"
                cols="30"
                rows="10" 
                placeholder="Текст сообщения*"
                >
                </textarea>
                <button type="submit" :style="send_btn_style">
                    <img src="@/assets/img/telegram_icon.png" alt="">
                    {{submit_btn_text}}
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
            submit_btn_text: 'Отправить сообщение',

            inputs_styles: {
                name: {},
                mail: {},
                body: {}
            } ,
            send_btn_style: {},

        }
    },
    methods: {
        set_empty_all_inputs(){
            this.mail_msg_name = ''
            this.mail_msg_tel = ''
            this.mail_msg_mail = ''
            this.mail_msg_body = ''
        },
        validate_inputs(){
            // Validate all inputs and show relevant ui if needed
            if (!this.mail_msg_name.trim()) {
                this.inputs_styles['name']['border'] = '2px solid red'
            }
            else if (!this.mail_msg_mail.trim()) {
                this.inputs_styles['mail']['border'] = '2px solid red'
            }
            else if (!this.mail_msg_body.trim()) {
                this.inputs_styles['body']['border'] = '2px solid red'
            }else{
                this.send_btn_style['background'] = '#69CB87'
                this.submit_btn_text = 'Отправлено!'
                setTimeout(() => {
                    this.send_btn_style['background'] = '#74CCD8'
                    this.submit_btn_text = 'Отправить сообщение'
                }, 2000);
                return true
            }

            setTimeout(() => {
                for (const key in this.inputs_styles) {
                    this.inputs_styles[key]['border'] = '1px solid #74CCD8'
                }
            }, 2000);

            return false
        },
        send_question() {
            if (this.validate_inputs()) {
                axios.post(`${this.$store.state.server_href}receive_mail`, {
                    mail_msg_name: this.mail_msg_name,
                    mail_msg_tel: this.mail_msg_tel,
                    mail_msg_mail: this.mail_msg_mail,
                    mail_msg_body: this.mail_msg_body,
                })
                this.set_empty_all_inputs()

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