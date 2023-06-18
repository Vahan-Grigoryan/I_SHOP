<template>


<div class="article_container">
    <ui-bread-crumbs />
    <h1>{{ blog.header }}</h1>
    <span>{{ blog.pub_date }}</span>

    <p ref="blog_content"></p>

    <!-- <h1>Фотоотчет</h1>
    <div class="article_gallery">
        <img src="@/assets/img/Rectangle_19-3.png" alt="">
        <img src="@/assets/img/Rectangle_19-3.png" alt="">
        <img src="@/assets/img/Rectangle_19-3.png" alt="">
        <img src="@/assets/img/Rectangle_19-3.png" alt="">
        <img src="@/assets/img/Rectangle_19-3.png" alt="">
        <img src="@/assets/img/Rectangle_19-3.png" alt="">
    </div> -->
</div>

<ui-href-blog-box 
@change_blog="getBlog"
:header_text="'Похожие статьи'"
/>

</template>

<script>
import emitsForApp from '@/mixins/emitsForApp';

export default {
    data(){
        return {
            blog: {}
        }
    },
    methods: {
        async getBlog(id){
            window.scrollTo(0,0)
            this.blog = await this.$store.dispatch('fetchBlog', id)
            this.blog.desc = this.blog.desc.replaceAll('/media', `${this.$store.state.server_href}media`)
            this.$refs['blog_content'].innerHTML = this.blog.desc
        }
    },
    async beforeMount(){
        this.getBlog(this.$route.params.id)

        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Article')
    },
    mixins: [emitsForApp],
}
</script>

<style scoped>
    @import url('@/assets/css/blog_detail.css');
</style>