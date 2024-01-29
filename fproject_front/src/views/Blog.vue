<template>

<div class="blog_container">
    <ui-bread-crumbs />

    <div class="blog_box">
        <h1>Блог</h1>
        <div class="blog_categories">
            <span 
            :class="{
                active_blog_category: !blogs_of_category
            }" 
            @click="blogs_of_category = ''"
            >
                Все статьи
            </span>
            <span 
            v-for="cat in blogs_categories"
            @click="blogs_of_category = cat.name"
            :class="{
                category_span: true,
                active_blog_category: blogs_of_category == cat.name
            }"
            >
                {{cat.name}}
            </span>
        </div>
        <ui-select 
        v-model:selected_option="sort_by"
        :purpose="'detail'"
        :options="blog_date_filters"
        />
        <br><br>
        <div class="blog_articles">
            <ui-blog-slide 
            v-for="blog in blogs.results"
            :key="blog.id"
            :blog="blog"
            />
        </div>
        <ui-pagination 
        :pages="$store.getters.calculatePagesCount(blogs.count, 2)"
        @paginated_to="(paginate_to) => current_page = paginate_to"
        v-model:page_active="current_page"
        />
    </div>
</div>


</template>

<script setup>
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount, watchEffect } from 'vue'


const store = useStore()

const blog_date_filters = reactive(['newest', 'latest'])
const sort_by = ref('newest')
const blogs = reactive({})
const blogs_categories = reactive({})
const blogs_of_category = ref('')
const blogs_of_category_old = ref('')
const current_page = ref(1)


onBeforeMount(async () => {
    Object.assign(
        blogs_categories,
        await store.dispatch('fetchBlogCategories')
    )

    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Blog')
})


watchEffect(async () => {
    const new_category_selected = blogs_of_category.value != blogs_of_category_old.value

    if(current_page.value > 1 && new_category_selected) current_page.value = 1
    if(new_category_selected){
        blogs_of_category_old.value = blogs_of_category.value
    }

    Object.assign(
        blogs,
        await store.dispatch(
            'fetchBlogs', 
            `sort_by=${sort_by.value}&category=${blogs_of_category.value}&pg=${current_page.value}`
        )
    )
})
</script>

<style scoped>
    @import url('@/assets/css/blog.css');
</style>
