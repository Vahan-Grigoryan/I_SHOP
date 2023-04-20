<template>
    <header>
        <div class="top_nav">
                <img src="@/assets/img/Logo.png" alt="" class="logo">
            <ul>
                <li><a href="#">О нас</a></li>
                <li><a href="#">Оплата и доставка</a></li>
                <li><a href="#">Отзывы</a></li>
                <li><a href="#">FAQ</a></li>
                <li><a href="#">Блог</a></li>
                <li><a href="#">Контакты</a></li>
            </ul>
            <div class="connects">
                <a class="connects__a" href="tel:+3899887857" >+38 097 435 6743</a>
                <a class="connects__a" href="mailto:Kidsshop@gmail.com">Kidsshop@gmail.com</a>
            </div>
            
            <div class="languages">
                <a href="" class="deactive">РУ</a>&nbsp;
                <a href="" class="active">LV</a>
            </div>
        </div>
        <div class="bottom_nav">
            <div class="bottom_nav__categories">
                <div class="bottom_nav__categories__burger">
                    <span class="b1"></span>
                    <span class="b2"></span>
                    <span class="b3"></span>
                </div>
                <h2>Каталог товаров</h2>
            </div>
            <form action="" class="bottom_nav__search_form">
                <img src="/@/assets/img/Search.png" alt="">
                <input type="text" placeholder="Введите запрос для поиска">
                <button type="submit">Найти</button>
            </form>

            <div class="bottom_nav__profile_box">
                <div class="log_or_reg">
                    <img src="@/assets/img/Profile1.png" alt="">

                    <div>
                        <a class="login" href="">Войти</a><br>
                        <a class="register" href="">Регистрироватся</a>
                    </div>
                </div>
                <!-- <div class="authorintacated">
                    <span>N</span>
                </div> -->
            </div>
            <a href="" class="bottom_nav__liked" data-count='9'><img src="/@/assets/img/Liked.png" alt=""></a>
            <a href="" class="bottom_nav__basket" data-count='99+'><img src="/@/assets/img/Basket.png" alt=""></a>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header'
    
}
</script>

<style scoped>
header {
  height: 120px;
  color: #090F24;
  font-size: 13px;
}

header .top_nav {
  display: flex;
  align-items: center;
  height: 50px;
  justify-content: space-between;
  padding: 0px 5.48387%;
}

header .top_nav ul {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 40%;
}

header .top_nav .connects {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 24%;
}

header .top_nav .connects__a {
  position: relative;
}

header .top_nav .connects__a:first-child::before {
  content: '';
  top: 0px;
  left: -24px;
  width: 16px;
  height: 16px;
  background: url("@/assets/img/Phone.png");
  position: absolute;
}

header .top_nav .connects__a:last-child::before {
  content: '';
  top: 0px;
  left: -28px;
  width: 20px;
  height: 15px;
  background: url("@/assets/img/Mail.png");
  position: absolute;
}

header .top_nav .languages {
  margin-left: -55px;
}

header .top_nav .languages .deactive {
  color: #B7B8C5;
}

header .top_nav .languages .active {
  border-bottom: 1px solid #74CCD8;
  padding-bottom: 2px;
}

header .bottom_nav {
  display: flex;
  align-items: center;
  height: 70px;
  background: #F4F5F9;
  padding: 0px 5.48387%;
  border-top: 1px solid #E4E7EE;
  border-bottom: 1px solid #E4E7EE;
}

header .bottom_nav__categories {
  height: 100%;
  border-left: 1px solid #E4E7EE;
  border-right: 1px solid #E4E7EE;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-right: 17.41935%;
}

header .bottom_nav__categories__burger {
  width: 20px;
  margin: 0px 12px 0px 20px;
}

header .bottom_nav__categories__burger span {
  display: block;
  width: 100%;
  height: 2px;
  background: #090F24;
  margin-bottom: 6px;
}

header .bottom_nav__categories__burger span:last-child {
  margin: 0px;
}

header .bottom_nav__search_form {
  margin: 0px 2% 0px 1%;
  font-size: 17px;
  position: relative;
}

header .bottom_nav__search_form img {
  position: absolute;
  margin: 11px 15px;
}

header .bottom_nav__search_form input {
  padding: 11px 5px 11px 45px;
  width: 305px;
  border: none;
  border-radius: 30px 0px 0px 30px;
  outline: none;
}

header .bottom_nav__search_form button {
  padding: 11px 25px;
  margin-left: -5px;
  border-radius: 0px 30px 30px 0px;
  color: white;
  background: #74CCD8;
  border: none;
  cursor: pointer;
}

header .bottom_nav__profile_box {
  display: flex;
}

header .bottom_nav__profile_box img {
  margin-right: 8px;
  height: 34px;
  width: 34px;
}

header .bottom_nav__profile_box .log_or_reg {
  display: flex;
}

header .bottom_nav__profile_box .login {
  color: #B7B8C5;
}

header .bottom_nav__profile_box .register {
  line-height: 19px;
  margin-top: 3px;
  display: block;
  font-weight: 600;
}

header .bottom_nav__profile_box .authorintacated {
  background: #74CCD8;
  border-radius: 50px;
  padding: 10px 15px;
  color: white;
  margin-left: 6.96774%;
  margin-right: 110px;
}

header .bottom_nav__profile_box .authorintacated span {
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
}

header .bottom_nav__liked {
  margin-left: 17.09677%;
  margin-right: 1.93548%;
  position: relative;
}

header .bottom_nav__liked::after {
  content: attr(data-count);
  top: 0px;
  right: 0px;
  transform: translateX(10px) translateY(-10px);
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50px;
  font-size: 10px;
  color: white;
  background: linear-gradient(180deg, #ED9BC1 0%, #ED9BB9 100%);
}

header .bottom_nav__basket {
  position: relative;
}

header .bottom_nav__basket::after {
  content: attr(data-count);
  top: 0px;
  right: 0px;
  transform: translateX(10px) translateY(-10px);
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50px;
  font-size: 10px;
  color: white;
  background: linear-gradient(180deg, #ED9BC1 0%, #ED9BB9 100%);
}
</style>