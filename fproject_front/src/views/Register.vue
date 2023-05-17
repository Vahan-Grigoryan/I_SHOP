<template>
<Header />
<ui-bread-crumbs style="padding-left: 5%;margin-top: 15px;" />
<div class="reg_container">
    <h1>Регистрация аккаунта</h1>
    <span>С помощью регистраци Вы сможете покупать у нас в 3 раза быстрее</span>
    <div class="register_form_and_register_procs">
        <form action="" class="register_form">
            <h2>Заполните форму регистрации</h2>
            <br>
            <div class="user_info_inputs">
                <input type="email" placeholder="Электронная почта*">
                <input type="tel" placeholder="Номер телефона*">
                <input type="text" placeholder="Ваше имя*">
                <input type="text" placeholder="Фамилия*">
                <input type="password" placeholder="Придумайте пароль (от 6 до 10 символов)*">
            </div>
            <br>
            <span>Или</span>
            <br>
            <button class="google_reg_btn">
                <img src="@/assets/img/Google.png" alt=""> &nbsp;
                Зарегестрироватся через Google
            </button>
            <h2>Адрес для получения доставки</h2>
            <div class="adresses">
                <input type="text" placeholder="Город / Село / Пагаст / Район*">
                <input type="text" placeholder="Улица / Дом / Квартира*">
                <input type="text" placeholder="Почтовый индекс*">
            </div>
            <label class="to_mail_list">
                <input type="checkbox" value="in_mail_list" />
                &nbsp;
                Оформить подписку на рассылку писем
            </label>
            <button type="submit" class="reg_btn">
                <img src="@/assets/img/ok3.png" alt=""> &nbsp;
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

<ui-footer />
</template>

<script>
export default {
    
}
</script>

<style scoped>
    @import url('@/assets/css/register.css');
</style>