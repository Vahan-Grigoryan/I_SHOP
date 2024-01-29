<template>
<div 
class="stripe_pay"
v-if="purpose === 'pay'"
> 
    <img v-if="!pay_loading" src="@/assets/img/credit-card.png">
    <span v-if="!pay_loading">Оплатить с карты</span>
    <div v-if="pay_loading" class="loading_circle"></div>
</div>
<div 
class="stripe_reject"
v-else-if="purpose === 'refund'"
>   
    <img v-if="!refund_loading" src="@/assets/img/credit-card.png">
    <span v-if="!refund_loading">Возврат средств</span>
    <div v-if="refund_loading" class="loading_circle"></div>
</div>
</template>

<script setup>

import { ref, watch } from 'vue'
import { useStore } from 'vuex'


const store = useStore()
const emit = defineEmits()
const props = defineProps({
    purpose: {
        type: String,
        required: true,
    },
    order_pk: {
        type: Number,
        required: true,
    },
    refund_payment_after_reason: {
        type: Boolean,
    },
    approve_mail_checking:{
        required: true,
        type: Boolean,
    }, 
})

const pay_loading = ref(false)
const refund_loading = ref(false)

async function refundOrder(){
    // emit to top changed order for valid ui
    refund_loading.value = true
    const changedOrder = await store.dispatch(
        'commonRequestWithAuth',
        {
            method: 'get',
            url_after_server_domain: `stripe_refund_order/${props.order_pk}`,
        }
    )
    emit('received_changed_order', changedOrder)
    refund_loading.value = false
}

async function createOrder(){
    // emit to top changed order for valid ui
    pay_loading.value = true
    const changedOrder = await store.dispatch(
        'commonRequestWithAuth', 
        {
            method: 'get',
            url_after_server_domain: `stripe_pay_order/${props.order_pk}`,
        }
    )
    emit('received_changed_order', changedOrder)
    pay_loading.value = false
}


// pay order after approving mail checking
watch(
    () => props.approve_mail_checking,
    async newValue => await createOrder()
)

// refund payment after reason is pointed and 
watch(
    () => props.refund_payment_after_reason,
    async newValue => await refundOrder()
)
</script>

<style scoped>
@import url('@/assets/css/loading_circle.css');
.stripe_pay{
    width: fit-content;
    height: fit-content;
    padding: 5px 40px;
    display: flex; 
    justify-content: center;
    align-items: center;
    background: rgb(13, 219, 13);
    border-radius: 5px;
    color: white;
    cursor: pointer;
    transition: .5s;
}
.stripe_pay:hover{
    box-shadow: 5px 5px 15px rgb(26, 136, 26);
}
.stripe_pay > img, .stripe_reject > img{
    width: 30px;
    height: 30px;
    margin-right: 10px;
}
.stripe_reject{
    width: fit-content;
    padding: 5px 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #858585;
    border-radius: 5px;
    color: white;
    cursor: pointer;
    transition: .5s;
}
.stripe_reject:hover{
    background: red;
    box-shadow: 5px 5px 15px red;
}
</style>
