<template>
<Header />
<div class="blog_container">
    <ui-bread-crumbs />

    <div class="blog_box">
        <h1>Блог</h1>
        <div class="blog_categories">
            <span class="active_article_category">Все статьи</span>
            <span>Здоровье малыша</span>
            <span>Детское питание</span>
            <span>Психология ребенка</span>
            <span>Детское питание</span>
            <span>Детское питание</span>
        </div>
        <ui-select 
        v-model:selected_option="current_date_filter"
        :purpose="'detail'"
        :options="blog_date_filters"
        />
        <br><br>
        <div class="blog_articles">
            <ui-blog-slide 
            :blog="blog_ex"
            />
            <ui-blog-slide 
            :blog="blog_ex"
            />
            <ui-blog-slide 
            :blog="blog_ex"
            />
            <ui-blog-slide 
            :blog="blog_ex"
            />
            <ui-blog-slide 
            :blog="blog_ex"
            />
        </div>
        <ui-pagination 
        :pages_per_view="10"
        />
    </div>
</div>

<ui-footer />
</template>

<script>
export default {
    data(){
        return {
            blog_date_filters: ['by newest', 'by latest'],
            current_date_filter: 'sort by',
            blog_ex: {
                date: '25.05.2022',
                name: 'Как понять, чего хочет малыш?',
                desc: 'Модель Mica предлагает простую установку при помощи основания Isofix с упором в пол и...'
            },
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Blog')
    }
}
</script>

<style scoped>
    @import url('@/assets/css/blog.css');
</style>