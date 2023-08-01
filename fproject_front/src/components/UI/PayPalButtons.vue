<template>
<div 
v-if="purpose === 'pay'"
class="paypal_pay"
@click="createOrder"
>
    <img src="@/assets/img/paypal.png">
    <span>Pay with PayPal</span>
</div>
<div 
v-else-if="purpose === 'refund'"
class="paypal_reject"
@click="refundOrder"
>
    <img src="@/assets/img/paypal.png">
    <span>Refund payment</span>
</div>
</template>

<script>
export default {
    name: 'ui-paypal-btns',
    props: {
        order_pk: {
            type: Number,
            required: true,
        },
        purpose: {
            type: String,
            required: true,
        },
    },
    methods: {
        async createOrder(){
            // Create paypal order
            const response = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'post',
                    url_after_server_domain: `paypal_create_order/${this.order_pk}`,
                    data: {
                        approved_url: location.href,
                        cancel_url: location.href
                    }
                }
            )
            location.href = response['purchase_url']
        },
        async refundOrder(){
            // Refund captured order and pass received changed order to parent 
            const changed_order = await this.$store.dispatch(
                'commonRequestWithAuth', 
                {
                    method: 'get',
                    url_after_server_domain: `paypal_refund_order/${this.order_pk}`,
                }
            )
            this.$emit('received_changed_order', changed_order)
        }
    },
    async beforeMount(){
        
    }
}

</script>

<style scoped>
.paypal_pay{
    width: fit-content;
    padding: 5px 40px;
    background: yellow;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgb(168, 164, 164);
    cursor: pointer;
    transition: .5s;
}
.paypal_pay:hover{
    box-shadow: 5px 5px 15px rgb(240, 240, 122);
    color:white
}
.paypal_pay img, .paypal_reject img{
    width: 30px;
    height: 30px;
    margin-right: 10px;
}
.paypal_reject{
    width: fit-content;
    padding: 5px 40px;
    background: gray;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    cursor: pointer;
    transition: .5s;
}
.paypal_reject:hover{
    box-shadow: 5px 5px 15px red;
    background: red;
}
</style>