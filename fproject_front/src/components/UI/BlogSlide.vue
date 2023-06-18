<template>
<SplideSlide 
class="splide_slide" 
v-if="splide_slide"
@click="$router.push(`/blog_detail/${blog.id}`)"
>
    <img :src="blog.thumbnail" alt="">
    <div class="blog_slide_content">
        <span class="date_span">{{ blog.pub_date }}</span>
        <h4>{{ blog.header }}</h4>
        <span class="desc">
            {{ blog.short_desc }}
        </span>
        <strong class="read_detail" @click="toBlogDetail(blog.id)">
            Читать подробнее &nbsp; &nbsp; 
            <img src="@/assets/img/arrow_5.png">
        </strong>
    </div>
</SplideSlide>
<div 
class="blog_slide" 
v-else
@click="$router.push(`/blog_detail/${blog.id}`)"
>
    <img :src="$store.getters.getImageUrl(blog.thumbnail)" alt="">
    <div class="blog_slide_content">
        <span class="date_span">{{ blog.pub_date }}</span>
        <h4>{{ blog.header }}</h4>
        <span class="desc">
            {{ blog.short_desc }}
        </span>
        <strong class="read_detail" @click="toBlogDetail(blog.id)">
            Читать подробнее &nbsp; &nbsp; 
            <img src="@/assets/img/arrow_5.png">
        </strong>
    </div>
</div>
</template>

<script>
// Blog slide for HrefBlogBox component(slider) and blog page
// props:
//      splide_slid: defines purpose of this component
//      blog: one blog with params to view(see above)

export default {
    name: 'ui-blog-slide',
    props: {
        splide_slide: {
            type: Boolean,
            default: false
        },
        blog: {
            type: Object
        }
    },
    methods: {
        toBlogDetail(id){
            this.$router.push(`/blog_detail/${id}`)
            this.$emit('change_blog', id)
        }
    }
}
</script>

<style scoped>
.splide_slide, .blog_slide{
    display: flex;
    padding: 10px;
    background: white;
    border: 1px solid #74CCD8;
    border-radius: 15px;
    width: 100%;
}
.splide_slide > img, .blog_slide > img{
    width: 180px;
    height: 240px;
    object-fit: cover;
    border-radius: 7px;
}
.blog_slide_content{
    margin: 20px 25px;
    text-align: left;
}
.blog_slide_content span:first-child{
    font-size: 14px;
    line-height: 139.02%;
    color: #B7B8C5;
}
.blog_slide_content h4{
    margin: 12px 0px;
}
.blog_slide_content .desc{
    font-size: 17px;
    line-height: 155.02%;
    color: #686877;
}
</style>