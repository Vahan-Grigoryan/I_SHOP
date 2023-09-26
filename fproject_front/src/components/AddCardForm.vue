<template>
<div v-if="user_stripe_payment" class="card_remembered_box">
    <h2>Вы уже указали карту</h2>
    <img src="@/assets/img/checkmark.png">
    <button @click="delCardFromOwner">Удалить и добавить новую</button>
</div>
<form 
class="payment_form" 
v-show="!user_stripe_payment && !stripe_payment_creating_loading"
@submit.prevent="createCardWithOwner"
>
    <div class="link_authentication_element">
        <!--Stripe.js injects the Link Authentication Element-->
    </div>
    <div class="payment_element">
        <!--Stripe.js injects the Payment Element-->
    </div>
    <button class="submit_card_credentials">
        Запомнить карту
    </button>
    <div ref="payment_message" class="payment_message hidden"></div>
    <h3 v-if="error_message">{{ error_message }}</h3>
    </form>
<div v-if="stripe_payment_creating_loading" class="loading_circle"></div>
    
</template>

<script>
import { loadStripe } from '@stripe/stripe-js';


export default {
    name: 'add-card-form',
    data(){
        return {
            stripe: '',
            payment_elements: '',
            stripe_payment_creating_loading: false,
            error_message: '',
        }
    },
    props:  {
        user_stripe_payment:{
            required: true,
            type: [null, Number],
        },
    },
    methods: {
        async createCardWithOwner(){
            // prepare stripe elements values and create payment method with stripe api,
            // also create card owner(StripePayment model),
            // if StripePayment successfully created
            // show valid ui, else show error

            this.stripe_payment_creating_loading = true

            const elements = this.payment_elements
            const {error: submitError} = await elements.submit();
            if (submitError) {
                console.log(submitError)
                return
            }
            const {error: paymentMethodError, paymentMethod} = await this.stripe.createPaymentMethod({elements});
            if (paymentMethodError) {
                console.log(paymentMethodError.message)
                return
            }
      
            const rememberCard = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'post',
                    url_after_server_domain: `stripe_create_card_owner`,
                    data: {
                        payment_method_id: paymentMethod['id']
                    }
                }
            )
            this.stripe_payment_creating_loading = false
            if (rememberCard['stripe_payment_id']) {
                this.$emit('update:user_stripe_payment', rememberCard['stripe_payment_id'])
            }else if(rememberCard['detail']){
                this.error_message = rememberCard['detail']
                setTimeout(()=>{
                    this.error_message = ''
                }, 4000)
            }
        },
    async delCardFromOwner(){
        // del StripePayment model from server, update ui
        const forgetCard = await this.$store.dispatch(
          'commonRequestWithAuth', 
          {
            method: 'delete',
            url_after_server_domain: `stripe_del_card_from_owner/${this.user_stripe_payment}`,
          }
        )
        this.$emit('update:user_stripe_payment', null)
        await this.loadStripeUi() 
    },
    async loadStripeUi(){
        // load stripe ui(card inputs)
        this.stripe = await loadStripe('pk_test_51NgBEoC400K1QcWYU04wbx5uagsDHWXdwqmDYhziI5rnsjGPm3yzJQag4l9Yf42Ztbo6B3YtId0kIdN6pbJ2YixR00YLaSqvqw')
        const options = {
            mode: 'payment',
            amount: 100,
            currency: 'usd',
            paymentMethodCreation: 'manual',
            appearance: {theme: 'stripe'},
        };
        this.payment_elements = this.stripe.elements(options);
        // const linkAuthenticationElement = this.payment_elements.create("linkAuthentication");
        // linkAuthenticationElement.mount(".link-authentication-element");
        const paymentElement = this.payment_elements.create("payment");
        paymentElement.mount(".payment_element"); 
    },

    },
    async beforeMount(){
        // if not poin card credentials yet show inputs
        if (!this.user_stripe_payment) {
            this.loadStripeUi() 
        }
    }
}
</script>

<style scoped>
@import url('@/assets/css/loading_circle.css');
body {
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  display: flex;
  justify-content: center;
  align-content: center;
  height: 100vh;
  width: 100vw;
}

.payment_form {
  align-self: center;
  border-radius: 7px;
}
.payment_form h3 {
    color: red;
    margin-top:7px
}

.hidden {
  display: none;
}

.payment_message {
  color: rgb(105, 115, 134);
  font-size: 16px;
  line-height: 20px;
  padding-top: 12px;
  text-align: center;
}

.payment_element {
  margin-top: 20px;
}

/* Buttons and links */
.submit_card_credentials {
  padding: 13px 35px;
  background: #74CCD8;
  border-radius: 5px;
  font-family: Arial, sans-serif;
  color: #ffffff;
  border: 0;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  display: block;
  transition: all 0.2s ease;
  box-shadow: 0px 4px 5.5px 0px rgba(0, 0, 0, 0.07);
  margin-top: 10px;
  width: 100%;
}
.submit_card_credentials:hover {
  filter: contrast(115%);
}
.submit_card_credentials:disabled {
  opacity: 0.5;
  cursor: default;
}

.card_remembered_box{
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #5eff8e;
  padding: 15px 0px;
  border-radius: 5px;
  color: white;
}
.card_remembered_box > img{
  margin: 10px 0px;
  width: 50px;
  height: 50px;
}
.card_remembered_box > button{
  padding: 13px 35px;
  background: #74CCD8;
  border-radius: 5px;
  color: white;
  border: none;
  font-size: 15px;
  cursor: pointer;
}
</style>
