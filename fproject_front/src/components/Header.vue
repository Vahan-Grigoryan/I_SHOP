<template>
<div class="auth_modal_wrapper" v-if="auth_modal_visible"></div>
<div class="auth_modal" v-if="auth_modal_visible">
  <img
  src="@/assets/img/clear.png"
  class="auth_modal_close_img"
  @click="auth_modal_visible = false"
  >
  <h2>Авторизуйтесь!</h2>
  <input type="email" placeholder="Электронная почта*">
  <input type="password" placeholder="Пароль*">
  <button class="basic_auth">Авторизоватся</button>
  <span class="or_span">Или</span>
  <button class="google_auth">
    <img src="@/assets/img/Google.png" alt=""> &nbsp;
    Войти через Google
  </button>
  <h3>У Вас еще нет аккаунта?</h3>
  <span>Зарегистрированным пользователям возвращается <strong>0,5%</strong> от стоимости покупки</span>
  <button class="or_reg_btn" @click="$router.push('/register')">Зарегестрироватся</button>
</div>
<header>
    <div class="top_nav">
        <img src="@/assets/img/Logo.png" alt="" class="logo" @click="$router.push('/')">
        <ul>
          <li><a @click="$router.push('/about')">О нас</a></li>
          <li><a >Оплата и доставка</a></li>
          <li><a @click="$router.push('/blog')">Блог</a></li>
          <li><a @click="$router.push('/brands')">Бренды</a></li>
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
        <div class="bottom_nav__categories" 
          @mouseover="mega_menu_visible=true" 
          @mouseleave="mega_menu_visible=false"
          >
            <div class="bottom_nav__categories__burger">
              <span class="b1"></span>
              <span class="b2"></span>
              <span class="b3"></span>
            </div>
            <h2>Каталог товаров</h2>
            <div v-if="mega_menu_visible" class="mega_menu">
              <div class="left_categories">
                <div 
                class="left_category" 
                v-for="category in Object.keys(categories)"
                @mouseenter="showCategories(category)"
                @click="selectLeftCategory(category)"
                >
                  <div>
                    <img :src="getImage(category)" width="25" height="25" class="default_img">
                    <img :src="getImageReplace(category)" width="25" height="25" class="replacement_img">
                    {{ category }}
                  </div>
                
                  <img src="@/assets/img/Vector_29.png" alt="" class="default_img">
                  <img src="@/assets/img/Vector_30.png" alt="" class="replacement_img">
                </div>
                
              </div>
              <div class="center_categories">
                <div v-if="select_plug1" class="please_select_box">
                  Select category!
                </div>
                <div 
                v-else
                class="center_category" 
                v-for="category_value in Object.values(center_categories)"
                >
                  <div 
                  v-if="categories_visibiltiy[category_value[0]+'_visible']"
                  v-for="center_category in category_value[1]"
                  >
                    <span @mouseover="showCategories(center_category, true)">
                      {{ center_category }}
                    </span>
                  </div>
                  
                </div>
              </div>
              <div class="right_categories">
                <div v-if="select_plug2" class="please_select_box">
                  Select subcategory!
                </div>
                <div class="right_category" 
                v-else
                v-for="category_value in Object.values(right_categories)"
                @click="selectRightCategory(category_value)"
                >
                  <div
                  v-if="categories_visibiltiy[category_value[0]+'_visible']"
                  v-for="right_category in category_value[1]"
                  >
                    <a>
                      {{ right_category }}
                    </a>
                  </div>
                  
                </div>
              </div>
            </div>
        </div>
        <form action="" class="bottom_nav__search_form">
          <img src="@/assets/img/Search.png" alt="">
          <input type="text" placeholder="Введите запрос для поиска">
          <button type="submit">Найти</button>
        </form>
        
        <div class="bottom_nav__profile_box">
              <div class="log_or_reg">
                  <img src="@/assets/img/Profile1.png" alt="">
                  <div>
                      <a class="login" @click="auth_modal_visible = true">Войти</a><br>
                      <a class="register" @click="$router.push('/register')">Регистрироватся</a>
                  </div>
              </div>
              <!-- <div class="authorintacated">
                  <span>N</span>
              </div> -->
        </div>
        <a 
        @click="redirectTo('liked')"
        class="bottom_nav__liked" 
        :data-count='likes'
        >
          <img src="@/assets/img/Liked.png" alt="">
        </a>
        <a 
        @click="redirectTo('orders')"
        class="bottom_nav__basket"
        :data-basket='basket'
        >
          <img src="@/assets/img/Basket.png" alt="">
        </a>
    </div>
</header>
</template>

<script>
// Header for project without slots, with dropwdown mega menu and many hrefs

import redirectTo from '@/mixins/redirectToProfilePart'


export default {
    name: 'Header',
    mixins: [redirectTo],
    props: {
      likes: {
        type: [Number],
        default: 0
      },
      basket: {
        type: [Number],
        default: 0
      },
    },
    // props: {
    //   categories: Object
    // }
    data(){
      return {
        mega_menu_visible: false,
        auth_modal_visible: false,
        categories:{
          // tech:{
          //   housewifely: [
          //     'vacuum_cleaners'
          //   ],
          //   programming:[
          //     'computers', 
          //     'phones'
          //   ],
          //   GGTT:[
          //     'GGTTcomputers', 
          //     'GGTTphones'
          //   ],

            
          // },
          // cloth: {
          //   mans: [
          //     'trousers',
          //     'shorts',
          //     'shoes',
          //     'cap',
          //     'jacket',
          //     'gloves',
          //     'socks',
          //     'leggings',
          //     'underpants',
          //   ],
          //   womens: [
          //     'shoes'
          //   ]
          // }
        },
        categories_without_images: {},
        categories_visibiltiy: {
          left_categories: {},
          center_categories: {}
        },
        center_categories: [],
        right_categories: [],
        select_plug1: true,
        select_plug2: true,
      }
    },
    methods: {
      selectLeftCategory(category){
        this.mega_menu_visible=false
        this.$router.push(`/mega_category/${category}`)
        this.$emit('selectedCategory', category)
      },
      selectRightCategory(category){
        this.mega_menu_visible=false
        
      },
      getImage(category){
        return `http://localhost:8000${this.categories[category]['image']}`
      },
      getImageReplace(category){
        return `http://localhost:8000${this.categories[category]['image_replace']}`
      },
      showCategories(category, center=false){
        
        if (center){
          Object.keys(this.categories_visibiltiy['center_categories']).forEach( key => {
            this.categories_visibiltiy[key] = false
          })
          this.select_plug2  = false
        }
        else{
          Object.keys(this.categories_visibiltiy['left_categories']).forEach( key => {
            this.categories_visibiltiy[key] = false
          })
          this.select_plug1 = false
        }
        this.categories_visibiltiy[category+'_visible']=true
        
      },
    },
    async beforeMount(){
      this.categories = await this.$store.getters.fetchCategories()
      let categories_without_images = {}
      Object.keys(this.categories).forEach( left_category_key => {
        categories_without_images[left_category_key]={}
        Object.keys(this.categories[left_category_key]).forEach( left_category_content_key => {
          if (left_category_content_key != 'image' && left_category_content_key != 'image_replace') {
            categories_without_images[left_category_key][left_category_content_key] = 
            this.categories[left_category_key][left_category_content_key]
          }
        })

      })

      this.categories_without_images = categories_without_images
      for (let [category_key, category_value] of Object.entries(this.categories_without_images)) {
        this.center_categories = [
          ...this.center_categories, 
          [category_key, [...Object.keys(category_value)]]
        ]
        for (let [key2, value2] of Object.entries(category_value)) {
          this.categories_visibiltiy['left_categories'][`${category_key}_visible`] = false
          this.categories_visibiltiy['center_categories'][`${key2}_visible`] = false
          this.right_categories = [
            ...this.right_categories, 
            [key2, [...Object.values(value2)]]
          ]
        }
      }
    },
    watch: {
      auth_modal_visible(newValue){
        if (newValue) {
          window.onscroll = function () { window.scrollTo(0, 0); };
        } 
        else {
          window.onscroll = function () { window.scrollTo(scrollX, scrollY); };
        }
      }
    }
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
  padding: 0px 5%;
}
header .top_nav > img{
  cursor: pointer;
}
header .top_nav ul {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 40%;
}
header .top_nav ul a{
  cursor: pointer;
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
  padding: 0px 5%;
  border-top: 1px solid #E4E7EE;
  border-bottom: 1px solid #E4E7EE;
}
header .bottom_nav__categories {
  position: relative;
  height: 100%;
  border-left: 1px solid #E4E7EE;
  border-right: 1px solid #E4E7EE;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-right: 17%;
}
header .bottom_nav__categories .mega_menu {
  position: absolute;
  left: 0px;
  bottom: 0px;
  width:100%;
  box-shadow: 0px 4px 11px rgba(68, 97, 132, 0.08);
  transform: translateY(100%);
  height: calc(100%/3);
  z-index: 999;
}
.mega_menu .left_categories {
  background: white;
  width: 100%;
  height: 500px;
  cursor: pointer;
  border-bottom-left-radius: 10px;
  box-shadow: 0px 4px 11px rgba(68, 97, 132, 0.08);
  position: relative;
  z-index: 9;
  border: 1px solid #74CCD8;
}
.mega_menu .center_categories {
  background: white;
  width: 100%;
  height: 500px;
  transform: translateX(100%) translateY(-100%);
}
.mega_menu .right_categories {
  background: #F4F5F9;
  width: 100%;
  height: 500px;
  border-bottom-right-radius: 10px;
  padding: 27px 29px 0px 27px;
  border: 1px solid #E4E7EE;
  transform: translateX(200%) translateY(-200%);
}
.left_category{
  width: 100%;
  padding: 15px 20px;
  font-size: 18px;
  color: #090F24;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #74CCD8;
}
.left_category:hover{
  background: linear-gradient(180deg, #ED9BC1 0%, #ED9BB9 100%);
  color: white;
  border:none
}
.left_category:hover .default_img{
  display: none;
}
.left_category:hover .replacement_img{
  display: block;
}
.left_category > div{
  display: flex;
  align-items: center;
  justify-content: center;

}
.left_category > div > img{
  margin-right: 15px;
}
.left_category .replacement_img{
  display: none;
}
.left_category img:last-child{
  color: #74CCD8;
}
.center_category{
  width: 100%;
  font-weight: 500;
  font-size: 16px;
  color: #B7B8C5;
}
.center_category span{
  width: 100%;
  padding: 15px 20px;
  display: inline-block;
  line-height: 25px;
  cursor: alias;
  border: 1px solid #E4E7EE;

}
.center_category span:hover{
  background: #F4F5F9 !important;
}
.right_category a{
  font-size: 14px;
  color: #3C3C50;
  margin-bottom: 10px;
  font-size: 14px;
  line-height: 19px;
  display: inline-block;
  cursor: pointer;
}
.right_category a:hover{
  text-decoration-line: underline;
}
.please_select_box{
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 25px;
}
.to_scroll{
  overflow-y: scroll;
}

header .bottom_nav__categories:hover {
  background: #74CCD8;
}
header .bottom_nav__categories:hover h2{
  color: white;
}
header .bottom_nav__categories:hover span {
  background: white;
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
header .bottom_nav__profile_box .log_or_reg a {
  cursor: pointer;
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
  cursor: pointer;
}

header .bottom_nav__profile_box .authorintacated span {
  font-weight: 500;
  font-size: 18px;
  line-height: 22px;
  right: 50px;
}

header .bottom_nav__liked {
  margin-left: 17.09677%;
  margin-right: 1.93548%;
  position: relative;
  cursor:pointer
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
  cursor:pointer
}

header .bottom_nav__basket {
  position: relative;
  cursor:pointer;
}

header .bottom_nav__basket::after {
  cursor:pointer;
  content: attr(data-basket);
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


.auth_modal_wrapper{
  width: 100%;
  height: 100vh;
  position: fixed;
  z-index: 15;
  background: #16625e;
  filter: blur(100px);
}
.auth_modal{
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  width: 35%;
  background: #F4F5F9;
  border-radius: 15px;
  padding: 45px;
  display: flex;
  flex-direction: column;
  box-shadow: 5px 5px 50px gray;
  z-index: 16; 
}
.auth_modal_close_img{
  position: absolute;
  cursor: pointer;
  width: 15px;
  height: 15px;
  right: 20px;
  top: 20px;
}
.auth_modal h2{
  text-align: center;
  margin-bottom: 22px;
}
.auth_modal input{
  border: 1px solid #B7B8C5;
  border-radius: 57px;
  padding: 10px 20px;
  font-size: 15px;
  line-height: 157.02%;
  color: #B7B8C5;
  margin-bottom: 15px;
}
.basic_auth{
  text-align: center;
  font-size: 16px;
  color: white;
  background: #74CCD8;
  border-radius: 51px;
  border: none;
  padding: 10px 0px;
  cursor: pointer;
}
.or_span{
  display: block;
  text-align: center;
  margin: 10px 0px;
  font-size: 15px;
}
.google_auth{
  background: white;
  border: 1px solid #E4E7EE;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 0px;
  font-size: 15px;
  box-shadow: 0px 2px 4px rgba(43, 90, 99, 0.06);
  border-radius: 48px;
  cursor: pointer;
}
.auth_modal h3{
  margin: 30px 0px 10px 0px;
}
.auth_modal > span{
  font-size: 17px;
  line-height: 155.02%;
  color: #686877;
}
.auth_modal .or_reg_btn{
  width: 100%;
  border: 1px solid #B7B8C5;
  border-radius: 47px;
  background: transparent;
  font-size: 16px;
  color: #686877;
  text-align: center;
  margin-top: 15px;
  padding: 15px 0px;
  cursor: pointer;
}






















</style>