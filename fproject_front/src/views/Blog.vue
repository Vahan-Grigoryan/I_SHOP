<template>

<div class="blog_container">
    <ui-bread-crumbs />

    <div class="blog_box">
        <h1>Блог</h1>
        <div class="blog_categories">
            <span :class="{
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
        @paginated_to="paginateTo"
        v-model:page_active="current_page"
        />
    </div>
</div>


</template>

<script>
import emitsForApp from '@/mixins/emitsForApp';

export default {
    data(){
        return {
            blog_date_filters: ['newest', 'latest'],
            sort_by: 'newest',
            blogs: [],
            blogs_categories: [],
            blogs_of_category: '',
            current_page: 1,
        }
    },
    methods: {
        async paginateTo(paginated_to=1){
            // Paginate to pagination page consider selected category and sort_by
            if (this.blogs_of_category) {
                try{
                    this.blogs = await this.$store.dispatch(
                        'fetchBlogs', 
                        `sort_by=${this.sort_by}&category=${this.blogs_of_category}&pg=${paginated_to}`
                    )
                    this.current_page = paginated_to
                }catch(err){}
            }else{
                try{
                    this.blogs = await this.$store.dispatch('fetchBlogs', `sort_by=${this.sort_by}&pg=${paginated_to}`)
                    this.current_page = paginated_to
                }catch(err){}
            }
            
        }
    },
    async beforeMount(){
        this.blogs = await this.$store.dispatch('fetchBlogs', `sort_by=${this.sort_by}`)
        this.blogs_categories = await this.$store.dispatch('fetchBlogCategories')

        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Blog')
    },
    mixins: [emitsForApp],
    watch: {
        async blogs_of_category(newValue){
            // blogs_of_category = selected category
            // If it changed get new blogs of pointed category or all blogs(with sort_by)
            this.current_page=1
            if (newValue) {
                this.blogs = await this.$store.dispatch(
                    'fetchBlogs', 
                    `sort_by=${this.sort_by}&category=${newValue}`
                )
            }else{
                this.blogs = await this.$store.dispatch(
                    'fetchBlogs', 
                    `sort_by=${this.sort_by}`
                )
            }
        },
        async sort_by(newValue){
            // If sort_by changed get new blogs(by selected category if needed)
            if (this.blogs_of_category) {
                this.blogs = await this.$store.dispatch(
                    'fetchBlogs', 
                    `sort_by=${newValue}&category=${this.blogs_of_category}&pg=${this.current_page}`
                )
            }else{
                this.blogs = await this.$store.dispatch(
                    'fetchBlogs', 
                    `sort_by=${newValue}&pg=${this.current_page}`
                )
            }
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/css/blog.css');
</style>