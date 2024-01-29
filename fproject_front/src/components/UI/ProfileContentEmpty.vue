<template>
    <div class="profile_content_empty">
        <h2>{{ header }}</h2>
        <span>{{ content }}</span>
        <button @click="$router.push('/product_filters')">
            <img src="@/assets/img/Vector_30.png" alt="">
            {{ btn_content }}
        </button>
    </div>
</template>

<script setup>
// If content empty in profile tab, put this component with custom 
// header, content, button for redirect

const props = defineProps({
    header: String,
    content: String,
    btn_content: String
})
</script>

<style scoped>
.profile_content_empty{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}
.profile_content_empty span{
    font-size: 17px;
    line-height: 155.02%;
    color: #828282;
    margin: 10px 0px 20px 0px;
}
.profile_content_empty button{
    background: #74CCD8;
    box-shadow: 0px 2px 4px rgba(51, 196, 223, 0.2);
    border-radius: 25px;
    padding: 13px 30px;
    font-size: 15px;
    border: none;
    color:white;
    cursor: pointer;
}
.profile_content_empty button img{
    transform: rotateZ(180deg);
    margin-right: 5px;
}
</style>
