<template>
<div>
    <div class="modal_wrapper" v-if="modal_visible"></div>
    <div class="modal" v-if="modal_visible">
        <img
        src="@/assets/img/clear.png"
        class="auth_modal_close_img"
        @click="$emit('update:modal_visible', false)"
        >
        <slot>

        </slot>
    </div>
</div>

</template>

<script>
export default {
    name: 'ui-modal',
    props: {
        modal_visible: [Boolean, String]
    }
}
</script>

<style scoped>
.modal_wrapper{
    transform: translateY(-120px);
    width: 100%;
    height: 100%;
    position: fixed;
    background: rgba(0, 0, 0, .5);
    z-index: 99;
}
.modal{
    width: 35%;
    display: flex;
    position: fixed;
    flex-direction: column;
    left: 50%;
    top: 50%;
    z-index: 999;
    transform: translateX(-50%) translateY(-50%);
    text-align: center;
    background: #F4F5F9;
    border-radius: 20px;
    padding: 45px;
}
.modal > .auth_modal_close_img{
    width: 15px;
    height: 15px;
    position: absolute;
    right: 20px;
    top: 20px;
    cursor: pointer;
}
</style>
