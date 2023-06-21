<template>


<div class="article_container">
    <ui-bread-crumbs />
    <h1>{{ blog.header }}</h1>
    <span>{{ blog.pub_date }}</span>

    <p ref="blog_content"></p>

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
            // Get blog by id,
            // in desc replace all images urls to valid urls
            // update blog content
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