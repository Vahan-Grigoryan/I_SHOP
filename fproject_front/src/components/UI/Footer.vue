<template>
    <footer>
        <div class="left_info footer_info_box">
            <h4>Контакты</h4><br>
            <div class="footer_info_inline">
                
                <img src="@/assets/img/tel.png" alt=""> &nbsp;
                <a href="tel:+3899887857">+38 097 435 6743</a>
                
            </div><br>
            <div class="footer_info_inline">
                <img src="@/assets/img/Whatsup_icon.png" alt=""> &nbsp;
                <img src="@/assets/img/Messenger.png" alt=""> &nbsp;
            </div><br>
            <div class="footer_info_inline">
                <img src="@/assets/img/Mail.png" alt=""> &nbsp;
                <a href="mailto:Kidsshop@gmail.com">Kidsshop@gmail.com</a>
            </div><br>
            <div class="footer_info_inline">
                <img src="@/assets/img/time.svg" alt=""> &nbsp;
                <span>Пн-Пт: 9:00 - 17:00</span>
            </div>
        </div>
        <div class="center_info footer_info_box">
            <h4>Меню сайта</h4>
            <div class="menu_flex">
                <div class="menu_left">
                    <span @click="$router.push('/product_filters')">Каталог</span><br>
                    <span @click="$router.push('/about')">О нас</span><br>
                    <span>Оплата и доставка</span><br>
                    
                </div>
                <div class="menu_right">
                    <span @click="$router.push('/register')">Регистрироватся</span><br>
                    <span @click="$router.push('/blog')">Блог</span><br>
                    <span @click="$router.push('/brands')">Бренды</span><br>
                </div>
            </div>
        </div>
        <div class="right_info footer_info_box">
            <h4>Социальные сети</h4>
            <div class="footer_info_inline">
                <a href="">
                    <img src="@/assets/img/twitter_blue.png" alt=""> &nbsp; &nbsp;
                </a>
                <a href="">
                    <img src="@/assets/img/instagram_blue.png" alt=""> &nbsp; &nbsp;
                </a>
                <a href="">
                    <img src="@/assets/img/facebook_blue.png" alt=""> &nbsp; &nbsp;
                </a>
                <a href="https://www.youtube.com/channel/UCENl4Z16gUwF1QLQZyJORgQ">
                    <img src="@/assets/img/youtube_blue.png" alt=""> &nbsp; &nbsp;
                </a>
            </div>
            <br>
            <img src="@/assets/img/Logo.png" alt="" class="footer_logo" @click="$router.push('/')">
        </div>
    </footer>
    <div class="protected_permissions_box">
        2011-2022 Все права защищены
    </div>
</template>

<script>
// Common footer
</script>

<style scoped>
footer{
    width: 100%;
    display: flex;
}
.footer_info_box{
    width: calc(100% / 3);
    border: 1px solid #74CCD8;
    padding: 40px 0px;
    font-size: 14px;
    line-height: 19px;
    color: #090F24;
}
.footer_info_inline{
    display: inline-block;
    margin-bottom: 20px;
}
.left_info{
    padding-left: 200px;
}
.center_info, .right_info{
    padding: 40px 55px 35px 55px;
}
.right_info h4{
    margin-bottom: 20px;
}
.menu_flex{
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}
.footer_info_inline img{
    cursor: pointer;
}
.menu_flex .menu_left{
    width: 60%;
}
.menu_flex .menu_left span, .menu_flex .menu_right span{
    display: inline-block;
    margin-bottom: 10px;
    cursor: pointer;
}
.menu_flex .menu_right{
    width: 35%;
}
.footer_logo{
    margin-top: 60px;
    cursor: pointer;
}
.protected_permissions_box{
    width: 100%;
    text-align: center;
    padding: 14px 0px;
    background: #74CCD8;
    color: white;
    font-size: 14px;
}
</style>
