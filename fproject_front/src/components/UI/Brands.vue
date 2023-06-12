<template>
<div class="brands_box">
    <h1 v-if="header_have">Бренды</h1>
    <div class="brands">
        <div 
        class="brand"
        v-for="brand in brands"
        @click="toFiltersPage(brand.name)"
        >
          <img :src="brand.image" alt="">
          <p>{{ brand.name }}</p>
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
        header_have: {
            type: Boolean,
            default: true
        },
        brands: Array
    },
    methods: {
      toFiltersPage(brand_name){
        this.$router.push('/product_filters')
        this.$emit('selectedBrand', brand_name)
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