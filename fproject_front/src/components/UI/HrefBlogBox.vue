<template>
    <mini-products-slider 
    :slidesPerPage="2"
    class="splide_blog_slide"
    >
        
        <template #header>
            <h1>{{ header_text }}</h1>
        </template>
        <slot>
            <ui-blog-slide 
            :splide_slide="true"
            v-for="blog in blogs"
            :blog="blog"
            >

            </ui-blog-slide>
        </slot>
        

        <template #bottom_button>
            <button @click="$router.push('/blog')">Читать блог</button>
        </template>
    </mini-products-slider>
</template>

<script>
// Component above footer in Index page, common slider,
// with custom header and bottom_button content


export default {
  name: 'ui-href-blog-box',
  data(){
    return {
        blogs: []
    }
  },
  props: {
    header_text: {
        type: String,
        default: 'Наш блог'
    }
  },
  async beforeMount(){
    const blogs = await this.$store.dispatch('fetchBlogsIndex')
    this.blogs = blogs
  }
}
</script>

<style scoped>
.splide_blog_slide{
    background: #D6F4FA;
    margin-top: 70px;
}
.splide_blog_slide button{
    font-size: 15px;
    line-height: 20px;
    background: linear-gradient(180deg, #ED9BC1 0%, #ED9BB9 100%);
    border-radius: 53px;
    color: white;
    padding: 10px 30px;
    border: none;
    cursor: pointer;
}
</style>