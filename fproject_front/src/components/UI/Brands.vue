<template>
<div class="brands_box">
    <h1 v-if="header_have">Бренды</h1>
    <div class="brands">
        <div class="brand">
            <img src="@/assets/img/brand1.png" alt="">
            <p>Philips Avent</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand2.png" alt="">
            <p>Hipp</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand3.png" alt="">
            <p>Omron</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand4.png" alt="">
            <p>NUK</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand5.png" alt="">
            <p>Nutrilon</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand6.png" alt="">
            <p>Britax Romer</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand7.png" alt="">
            <p>Puky</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand8.png" alt="">
            <p>The name of Brand</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand9.png" alt="">
            <p>Ergobaby</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand10.png" alt="">
            <p>Alvi</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand11.png" alt="">
            <p>Baby Born</p>
        </div>
        <div class="brand">
            <img src="@/assets/img/brand12.png" alt="">
            <p>Chicco</p>
        </div>
    </div>
    <slot name="pagination_or_href">
        <button @click="$router.push('/brands')">Смотреть все бренды</button>
    </slot> 
</div>
</template>

<script>
// Component for Index and Brands pages,
// with custom pagination_or_href section


export default {
    name: 'ui-brands',
    props: {
        header_have:{
            type: Boolean,
            default: true
        }
    }
}
</script>

<style scoped>
.brands_box{
  text-align: center;
  background: #F4F5F9;
  padding: 60px 80px;
  margin: 0;
}
.brands{
  margin: 30px 0px;
  display: grid;
  grid-template-columns: auto auto auto auto auto auto;
  grid-gap: 25px;
}
.brand{
    cursor: pointer;
}
.brand > p{
  font-size: 15px;
  line-height: 142%;
  margin-top: 10px;
}
.brand > img{
  padding: 25px 30px;
  background: white;
  border: 1px solid #E4E7EE;
  border-radius: 10px;
}
.brands_box > button{
  color: #090F24;
  background: white;
  line-height: 20px;
  font-size: 15px;
  padding: 15px 30px;
  border: 1px solid #B7B8C5;
  border-radius: 53px;
  cursor: pointer;
}
.brands_box > button:hover{
  background: #a3a3a4;
  color: white;
}
</style>