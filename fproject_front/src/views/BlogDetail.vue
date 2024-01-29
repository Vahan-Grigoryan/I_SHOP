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

<script setup>
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount } from 'vue'


const store = useStore()
const route = useRoute()

const blog = reactive({})
const blog_content = ref(null)


onBeforeMount(async () => {
    getBlog(route.params.id)

    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Article')
})


async function getBlog(id){
    // Get blog by id,
    // in desc replace all images urls to valid urls
    // update blog content
    window.scrollTo(0,0)
    Object.assign(blog, await store.dispatch('fetchBlog', id))
    blog.desc = blog.desc.replaceAll('/media', `${store.state.server_href}media`)
    blog_content.value.innerHTML = blog.desc
}

</script>

<style scoped>
    @import url('@/assets/css/blog_detail.css');
</style>
