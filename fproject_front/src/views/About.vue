<template>
    
    <div class="about_container">
        <ui-bread-crumbs />
        <div class="content_and_img">
            <div class="about_content">
                <h1>О нашей компании</h1>
                <p>Причина успеха этой страницы «О нас» для бизнеса проста — она рассказывает потенциальному покупателю историю. Если у вас есть замечательная история о том, как ваш продукт или услуга должен изменить жизнь людей к лучшему, непременно поделитесь ею.</p>
                <p>Эта веб-страница является прекрасным местом для жизни в любых ее проявлениях. Реалистичные истории очеловечивают бренд, предоставляя контекст и значение для вашего продукта. Более того, хорошими историями хочется делиться — это означает, что пользователи с большей вероятностью будут рекламировать вас.</p>
                                
            </div>
            <img src="@/assets/img/portrait-pretty-mother-with-shopping-package-walking-with-baby-carriage-incity-center_1.png" alt="">
        
        </div>
        <p>Компания по производству гамаков Yellow Leaf рассказывают пользователям о продукте, описывая, как простой хендмейд меняет жизнь мастеров и их семей в Таиланде. Страница разбита на отдельные истории и разделы, в которых сочетаются блоки текста и легкоусвояемая графика, рисуя прекрасные и человечные образы.</p>
        <p>Авторы четко дают понять преимущества продукта чуть ли не для всего мира, заканчивая месседж словами «Это основа для светлого будущего, построенная вручную».</p>
    </div>
    <div style="background: #F4F5F9;">
        <ui-our-procs style="padding: 60px 0px;" />
    </div>
    <div class="about_container">
        <p>У каждой компании есть что рассказать. Поэтому вспоминайте свои навыки пересказывания классики из того случайного урока русского языка, который вы посещали много лет назад, и разместите их на корпоративном сайте.</p>
        <p>Комбинируя описательный и эмоциональный текст с великолепной графикой, страница «О нас» заработает для вашего бизнеса гораздо больше, чем скучный однообразный контент.</p>
        <div class="photogallery">
            <h1>Фотогалерея</h1>
            <div class="gallery">
                <img src="@/assets/img/Rectangle_19.png" alt="">
                <img src="@/assets/img/Rectangle_19-1.png" alt="">
                <img src="@/assets/img/Rectangle_19-2.png" alt="">
                <img src="@/assets/img/Rectangle_19-3.png" alt="">
                <img src="@/assets/img/Rectangle_19-4.png" alt="">
                <img src="@/assets/img/Rectangle_19-5.png" alt="">
            </div>
        </div>
    </div>
    <ContactUsBox />
    
</template>

<script setup>
import { useStore } from 'vuex'
import { onBeforeMount } from 'vue'


const store = useStore()


onBeforeMount(()=>{
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('About')
})
</script>

<style scoped>
    @import url('@/assets/css/about.css');
</style>
