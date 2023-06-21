<template>
    <!-- <Header 
    v-model:search_query="search_query"
    /> -->
    <div class="filters_container">
        <ui-bread-crumbs style="margin-bottom: 40px;"/>
        <br>
        <span class="filter_result_plug" v-if="search_query?.length>2">Результаты поиска: </span>
        <span class="filter_result_plug" v-else>Введите запрос для поиска</span>
        <span class="filter_result_header" v-if="search_query?.length>2"> {{ search_query }}</span>
        <br><br>
        <span class="filter_result_plug" style="color:#74CCD8">Все фильтры комбинируются!</span>
        
        <div class="filters_and_products">
            <div class="filters_box">
                <div class="cats">
                    <div class="filter_categories">
                        <div class="filter_categories__burger">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                        <span class="categories_header">Категории</span>
                    </div>
                    <ui-select 
                    v-for="[left_category_key, left_category_value] in Object.entries(categories)"
                    :ref="left_category_key"
                    :selected_option="left_category_key"
                    >
                        <template #custom_content>
                            <div 
                            v-for="[center_category_key, center_category_value] in Object.entries(left_category_value)"
                            >
                                <div 
                                class="filter_center_category"
                                v-if="!center_category_key.includes('image')"
                                >
                                    <span 
                                    class="center_category"
                                    @click="setCenterCategoryActive(center_category_key, center_category_value)"
                                    >
                                        {{ center_category_key }}
                                    </span>
                                    <label 
                                    class="checkbox_input_container filter_right_category"
                                    v-for="right_category in center_category_value"
                                    >
                                        <span class="checkbox_value">
                                            {{ right_category }}
                                        </span>
                                        <input 
                                        type="checkbox" 
                                        :value="right_category"
                                        @click="addOrDelFilterEntity('categories', right_category)"
                                        v-if="selected_filters['categories'].has(right_category)"
                                        checked
                                        >
                                        <input 
                                        type="checkbox" 
                                        :value="right_category"
                                        @click="addOrDelFilterEntity('categories', right_category)"
                                        v-else
                                        >
                                        <span class="checkmark"></span>
                                    </label>
                                </div>
                                
                                
                            </div>
                        </template>
                    </ui-select>
                </div>
                <div class="filters">
                    <div class="filter_categories">
                        <img src="@/assets/img/filter.png">&nbsp; &nbsp;
                        <span class="categories_header">Другие фильтры</span>
                    </div>
                    <div class="point_filters">

                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="price_available=!price_available"
                            >
                                <span class="subfilter_header">По цене:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!price_available">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="price_available">
                            </div>
                            
                            <div class="price_between_box" v-if="price_available">
                                <input type="number" v-model="selected_filters['priceGte']">
                                <span class="separator">-</span>
                                <input type="number" v-model="selected_filters['priceLte']">
                            </div>
                        </div>
                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="brand_available=!brand_available"
                            >
                                <span class="subfilter_header">Бренды:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!brand_available">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="brand_available">
                            </div>
                            
                            <div class="brands_box" v-if="brand_available">
                                <label 
                                class="checkbox_input_container"
                                v-for="brand in brands"
                                >
                                    <span class="checkbox_value">
                                        {{ brand }}
                                    </span>
                                    
                                    <input 
                                    type="checkbox"
                                    @change="addOrDelFilterEntity('brands', brand)"
                                    v-if="selected_filters['brands'].has(brand)"
                                    checked
                                    >
                                    <input 
                                    type="checkbox"
                                    @change="addOrDelFilterEntity('brands', brand)"
                                    v-else
                                    >
                                    <span class="checkmark"></span>
                                </label><br>
                            </div>
                        </div>
                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="color_available=!color_available"
                            >
                                <span class="subfilter_header">По цветам:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!color_available">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="color_available">
                            </div>
                            
                            <div class="brands_box" v-if="color_available">
                                <label 
                                class="checkbox_input_container"
                                v-for="color in colors"
                                >
                                    <span class="checkbox_value">
                                        {{ color }}
                                    </span>
                                    
                                    <input 
                                    type="checkbox"
                                    @change="addOrDelFilterEntity('colors', color)"
                                    v-if="selected_filters['colors'].has(color)"
                                    checked
                                    >
                                    <input
                                    @change="addOrDelFilterEntity('colors', color)" 
                                    type="checkbox"
                                    v-else
                                    >
                                    <span class="checkmark"></span>
                                </label><br>
                            </div>
                        </div>

                    </div>
                </div>
                
            </div>

            <div class="products_box">
                <div 
                class="current_filters"
                v-if="active_filters_visible"
                >
                    <div class="slug_and_close">
                        <h3>Активные фильтры</h3>
                        <div class="close" @click="active_filters_to_null">&nbsp; Очистить все</div>
                    </div>
                    <hr>
                    <div class="selected_filters">
                        <div 
                        class="filter_row"
                        v-for="[filterKey, filterValue] in active_filters"
                        >
                            <span>{{ active_filters_ru[filterKey] }}:</span>
                            <div 
                            class="filter_with_close"
                            v-if="typeof filterValue === 'object'"
                            v-for="filter in filterValue"
                            >
                                {{ filter }} &nbsp; 
                                <img src="@/assets/img/clear.png" @click="filterUnselect(filterKey, filter)">
                            </div>
                            <div 
                            class="filter_with_close"
                            v-else
                            >
                                {{ filterValue }} &nbsp; 
                                <img src="@/assets/img/clear.png" @click="filterUnselect(filterKey, filterValue)">
                            </div>
                        </div>
                    </div>

                </div>
                <div class="products_count_and_sort_select">
                    <span>Найдено {{ products.count }} товаров</span>
                    <ui-select 
                    :purpose="'detail'"
                    v-model:selected_option="products_sort_option"
                    :options="['newest', 'latest']"
                    />
                </div>
                
                <div class="found_products" v-if="products.results.length">
                    <ui-slide
                    v-for="product in products.results"
                    :key="product.id"
                    :product="product"
                    >
                    </ui-slide>
                    
                </div>
                <h1 v-else>
                    По вашим критериям продуктов не найдено
                </h1>
                <ui-pagination
                v-if="getPagesCount()" 
                :pages_per_view="getPagesCount()"
                @paginated_to="(page) => getFilteredProducts(page)"
                v-model:page_active="current_pagination_page"
                />
            </div>
            
        </div>

    </div>
    
    

</template>

<script>
import emitsForApp from '@/mixins/emitsForApp'

export default {
    inject: [
        'search_query', 'change_brand',
        'change_center_category', 'change_right_category'
    ],
    data(){
        return {
            price_available: false,
            brand_available: false,
            color_available: false,
            products_sort_option: 'newest',
            current_pagination_page: 1,
            categories: JSON.parse(localStorage.getItem('cats_formated')), 
            brands: [],
            colors: [],
            products: [],
            active_filters_visible: false,
            active_filters_ru: {
                categories: 'Категории',
                priceGte: 'Цена больше чем или равно',
                priceLte: 'Цена меньше чем или равно', 
                colors: 'Цвета',
                brands: 'Бренды',
            },
            active_filters: new Map(),
            selected_filters: {
                categories: new Set(),
                centerCategoriesCheckedState: new Map(),
                priceGte: '',
                priceLte: '', 
                colors: new Set(),
                brands: new Set(),
            },

        }
    },
    mixins: [emitsForApp],
    methods: {
        setCenterCategoryActive(center_category_key, center_category_value){
            // Set all subcategories of center category active
            const centerCategoryState = this.selected_filters['centerCategoriesCheckedState'].get(center_category_key)
            if (centerCategoryState) {
                for (const right_category of center_category_value) {
                    this.selected_filters['categories'].delete(right_category)
                }
                this.selected_filters['centerCategoriesCheckedState'].set(center_category_key, false)
            } else {
                for (const right_category of center_category_value) {
                    this.selected_filters['categories'].add(right_category)
                }
                this.selected_filters['centerCategoriesCheckedState'].set(center_category_key, true)
            }
        },
        addOrDelFilterEntity(filters_key, entity){
            // Set filter entity active(ex. category, brand, color by each one)
            this.selected_filters[filters_key].has(entity)?
                this.selected_filters[filters_key].delete(entity):
                this.selected_filters[filters_key].add(entity)
        },
        check_all_values(){
            // Check if at least one filter selected
            return this.selected_filters['categories'].size ||
                this.selected_filters['brands'].size ||
                this.selected_filters['colors'].size ||
                this.selected_filters['priceGte'] ||
                this.selected_filters['priceLte'] 
        },
        getActiveFilters(){
            // Set or del(empty filters type) active filters for page and request to server
            const filters = this.selected_filters
            for (const key in filters) {
                if (
                    key !== 'centerCategoriesCheckedState' && 
                    (
                        filters[key].size || !['string', 'object'].includes(typeof filters[key])
                    )
                ) {
                    // In this if checking what filter changed and her value add to active filters
                    this.active_filters.set(key, filters[key])
                }else{
                    this.active_filters.delete(key)
                }
                
            }
            
        },
        active_filters_to_null(){
            // Reset active filters, it visible, and selected categories
            this.selected_filters = {
                categories: new Set(),
                centerCategoriesCheckedState: new Map(),
                priceGte: '',
                priceLte: '', 
                colors: new Set(),
                brands: new Set(),
            }
        },
        filterUnselect(active_filters_key, filter){
            // Unselect pointed filter of active filters
            if (typeof this.active_filters.get(active_filters_key) === 'object') {
                this.active_filters.get(active_filters_key).delete(filter)

            } else {
                this.active_filters.delete(active_filters_key)
                this.selected_filters[active_filters_key] = ''
            }
        },
        getActiveFiltersByUrlParams(){
            // Construct url params for request like: param=paramValue1,paramValue2&priceLte=9 of active_filters
            let requestUrlParams = ''
            for (const [key, value] of this.active_filters.entries()) {
                const filterUrlParamValue = typeof value == 'object'? [...value].join(','): value
                requestUrlParams += `${key}=${filterUrlParamValue}&`
            }
            requestUrlParams = requestUrlParams.slice(0, requestUrlParams.length-1)
            return requestUrlParams
        },
        getPagesCount(){
            // Count pagination pages
            const pages = Math.ceil(this.products.count/4)
            return pages<=1 ? '' : pages
        },
        async getFilteredProducts(paginate_to=1){
            // Add additional url params(or not) to filter and straightaway fetch new products
            // Also paginate to page if needs
            const urlParams = this.getActiveFiltersByUrlParams()
            let url = ``
            url += urlParams? `&${urlParams}`: ''
            url += this.search_query? `&name=${this.search_query}`: ''
            try{
                this.products = await this.$store.dispatch(
                    'fetchFilteredProducts', 
                    `?sort_by=${this.products_sort_option}${url}&pg=${paginate_to}`
                )
                this.current_pagination_page = paginate_to
            }catch(err){}
            
        }
    },
    async beforeMount(){
        this.$store.state.pagesInCrumbs.clear()
        this.$store.state.pagesInCrumbs.add('Search and filter products')

        const availableFilters = await this.$store.dispatch('fetchAvailableFilters')
        this.brands = await availableFilters.brands
        this.colors = await availableFilters.colors
        await this.getFilteredProducts()
        if(this.change_center_category){
            const [left_cat, center_cat] = this.change_center_category.split(',')
            for (const iterator of this.categories[left_cat][center_cat]) {
                this.selected_filters['categories'].add(iterator);
            }
            this.$refs[left_cat][0].options_visible_filters=true;
            this.$refs[left_cat][0].click
        }
        else if(this.change_right_category){
            this.selected_filters['categories'].add(this.change_right_category)
        }
        else if(this.change_brand){
            this.selected_filters['brands'].add(this.change_brand)
        }
    },
    beforeUnmount(){
        this.$emit('rerender_header', 'set_search_text_empty')
        this.active_filters_to_null() 
    },
    watch: {
        selected_filters: {
            async handler(newValue){
                // If at least one filter selected show active filters box.
                // Get new active filters,
                this.active_filters_visible = this.check_all_values()
                this.getActiveFilters()
                await this.getFilteredProducts()
                
            },
            deep: true
        },
        async search_query(newValue){
            await this.getFilteredProducts()
            
        },
        async products_sort_option(newValue){
            await this.getFilteredProducts()
        },
        change_center_category(newValue){
            this.selected_filters['categories'].clear()
            const [left_cat, center_cat] = this.change_center_category.split(',')
            for (const iterator of this.categories[left_cat][center_cat]) {
                this.selected_filters['categories'].add(iterator);
            }
            this.$refs[left_cat][0].options_visible_filters=true;
            this.$refs[left_cat][0].click()
        },
        change_right_category(newValue){
            this.selected_filters['categories'].clear()
            this.selected_filters['categories'].add(this.change_right_category)
        },
    },
}
</script>

<style scoped>
    @import url('@/assets/css/product_filters.css');
</style>