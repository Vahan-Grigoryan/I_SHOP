<template>
    <div class="filters_container">
        <ui-bread-crumbs style="margin-bottom: 40px;"/>
        <br>
        <span class="filter_result_plug" v-if="$route.query[ 'search_query' ]?.length>2">Результаты поиска: </span>
        <span class="filter_result_plug" v-else>Введите запрос для поиска</span>
        <span class="filter_result_header" v-if="$route.query[ 'search_query' ]?.length>2"> {{ $route.query[ 'search_query' ] }}</span>
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
                    :ref="el => left_cat_refs[left_category_key] = el"
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
                            @click="price_box_visible=!price_box_visible"
                            >
                                <span class="subfilter_header">По цене:</span>
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="price_box_visible">
                                <img src="@/assets/img/Vector_44.png" v-else>
                            </div>
                            
                            <div class="price_between_box" v-if="price_box_visible">
                                <input type="number" v-model="selected_filters['priceGte']">
                                <span class="separator">-</span>
                                <input type="number" v-model="selected_filters['priceLte']">
                            </div>
                        </div>
                        <div class="subfilter">
                            <div 
                            class="subfilter_available" 
                            @click="brand_box_visible=!brand_box_visible"
                            >
                                <span class="subfilter_header">Бренды:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!brand_box_visible">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="brand_box_visible">
                            </div>
                            
                            <div class="brands_box" v-if="brand_box_visible">
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
                            @click="color_box_visible=!color_box_visible"
                            >
                                <span class="subfilter_header">По цветам:</span>
                                <img src="@/assets/img/Vector_44.png" v-if="!color_box_visible">
                                <img src="@/assets/img/Vector_44.png" style="transform: rotateX(180deg);" v-if="color_box_visible">
                            </div>
                            
                            <div class="brands_box" v-if="color_box_visible">
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
                            <div class="categories_in_grid">
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

                </div>
                <div class="products_count_and_sort_select">
                    <span>Найдено {{ products.count }} товаров</span>
                    <ui-select 
                    :purpose="'detail'"
                    v-model:selected_option="products_sort_option"
                    :options="['newest', 'latest']"
                    />
                </div>
                
                <div class="found_products" v-if="products.results">
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
                :pages="$store.getters.calculatePagesCount(products.count)"
                @paginated_to="getFilteredProducts"
                v-model:page_active="current_pagination_page"
                />
            </div>
            
        </div>

    </div>
    
    

</template>

<script setup>
/*
This page logic:
All filters received from other pages will override all previously filters,
and will be active only received filter(the only one).
All filters that selected on filters page(this page) will be added to active filters 
*/

import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import { ref, reactive, onBeforeMount, watch } from 'vue'


const store = useStore()
const route = useRoute()

const price_box_visible = ref(false)
const brand_box_visible = ref(false)
const color_box_visible = ref(false)
const products_sort_option = ref('newest')
const current_pagination_page = ref(1)
const categories = reactive(JSON.parse(localStorage.getItem('cats_formated')))
const brands = reactive([])
const colors = reactive([])
const products = reactive({})
const active_filters_visible = ref(false)
const left_cat_refs = reactive({})
const active_filters_ru = {
    categories: 'Категории',
    priceGte: 'Цена больше чем или равно',
    priceLte: 'Цена меньше чем или равно', 
    colors: 'Цвета',
    brands: 'Бренды',
}
const active_filters = reactive(new Map())
const selected_filters = reactive({
    categories: new Set(),
    centerCategoriesCheckedState: new Map(),
    priceGte: '',
    priceLte: '', 
    colors: new Set(),
    brands: new Set(),
})


onBeforeMount(async () => {
    // Get available filters from server.
    // Check if user redirected there with any 
    // $route.query param(excluded search_query), activate relevant filters
    // else just get all products without filters.
    // After above clear $route.query
    store.state.pagesInCrumbs.clear()
    store.state.pagesInCrumbs.add('Search and filter products')

    const availableFilters = await store.dispatch('fetchAvailableFilters')
    brands.splice(0, brands.length, ...await availableFilters['brands'])
    colors.splice(0, colors.length, ...await availableFilters['colors'])

    if(route.query['center_category']){
        //if provided center category, set all right categories(children cats) of pointed center category
        const [left_cat, center_cat] = route.query['center_category'].split(',')
        for (const right_category of categories[left_cat][center_cat]) {
            selected_filters['categories'].add(right_category)
        }
        left_cat_refs[left_cat].options_visible_filters=true 
        left_cat_refs[left_cat].click 
    }
    if(route.query['right_category']){
        // if provided right_category, add it into categories for filtering
        selected_filters['categories'].add(route.query['right_category'])
    }
    if(route.query['brand']){
        // if provided brand, add it into brands for filtering
        selected_filters['brands'].add(route.query['brand'])
    }
    if(await !products.length) await getFilteredProducts()
    window.location.href = window.location.href.split('?')[0]

})


watch(
    selected_filters,
    async () => {
        // If at least one filter selected show active filters box.
        // Get new active filters,
        active_filters_visible.value = check_all_values()
        getActiveFilters()
        await getFilteredProducts()
    },
    {deep: true}
)
watch(
    () => route.query,
    async newValue => {
        // if received any filter from other page add it to relevant this.selected_filters key
        // or just call getFilteredProducts()
        if(newValue['right_category']){
            selected_filters['categories'].add(newValue['right_category'])
        }
        if(newValue['search_query'] || newValue['search_query'] == ''){
            // if search_query url param exists
            // (this mean search_query=any or search_query=''(if deleted after search))
            // because it can be deleted after
            // searching, we need to get new filtered products in both of cases
            await getFilteredProducts()
        }
    },
    {deep: true}
)
watch(
    products_sort_option,
    async () => {
        await getFilteredProducts(current_pagination_page.value)
    }
)


function setCenterCategoryActive(center_category_key, center_category_value){
    // Activate all subcategories of center category or deactivate if activated
    const centerCategoryState = selected_filters['centerCategoriesCheckedState'].get(center_category_key)
    if (centerCategoryState) {
        for (const right_category of center_category_value) {
            selected_filters['categories'].delete(right_category)
        }
        selected_filters['centerCategoriesCheckedState'].set(center_category_key, false)
    } else {
        for (const right_category of center_category_value) {
            selected_filters['categories'].add(right_category)
        }
        selected_filters['centerCategoriesCheckedState'].set(center_category_key, true)
    }
}
function addOrDelFilterEntity(filters_key, entity){
    // Set/remove filter entity active(ex. category, brand, color by each one)
    selected_filters[filters_key].has(entity)?
        selected_filters[filters_key].delete(entity):
        selected_filters[filters_key].add(entity)
}
function check_all_values(){
    // Check if at least one filter selected
    return selected_filters['categories'].size ||
        selected_filters['brands'].size ||
        selected_filters['colors'].size ||
        selected_filters['priceGte'] ||
        selected_filters['priceLte'] 
}
function getActiveFilters(){
    // Set or del(key in this.active_filters) active filters for page ui and request to server
    const filters = selected_filters
    for (const key in filters) {
        if (
            key !== 'centerCategoriesCheckedState' && 
            (
                filters[key].size || !['string', 'object'].includes(typeof filters[key])
            )
        ) {
            // In this if checking what filter changed and her value add to active filters
            active_filters.set(key, filters[key])
        }else{
            active_filters.delete(key)
        }
        
    }
}
function active_filters_to_null(){
    // Reset active filters, it visible, and selected categories
    Object.assign(
        selected_filters,
        {
            categories: new Set(),
            centerCategoriesCheckedState: new Map(),
            priceGte: '',
            priceLte: '', 
            colors: new Set(),
            brands: new Set(),
        }
    )
}
function filterUnselect(active_filters_key, filter){
    // Unselect pointed filter of active filters
    if (typeof active_filters.get(active_filters_key) === 'object') {
        active_filters.get(active_filters_key).delete(filter)

    } else {
        active_filters.delete(active_filters_key)
        selected_filters[active_filters_key] = ''
    }
}
function convertActiveFiltersToUrlParamsForRequest(){
    // Construct url params for request like: param=paramValue1,paramValue2&priceLte=9 of active_filters
    let requestUrlParams = ''
    for (const [key, value] of active_filters.entries()) {
        const filterUrlParamValue = typeof value == 'object'? [...value].join(','): value
        requestUrlParams += `${key}=${filterUrlParamValue}&`
    }
    requestUrlParams = requestUrlParams.slice(0, requestUrlParams.length-1)
    return requestUrlParams
}
async function getFilteredProducts(paginate_to=1){
    // Add additional url params(or not) to filter and straightaway fetch new products
    // Also paginate to page if needs
    
    const urlParams = convertActiveFiltersToUrlParamsForRequest()
    let url = urlParams? `&${urlParams}`: ''
    url += route.query['search_query']? `&name=${route.query['search_query']}`: ''
    Object.assign(
        products,
        ...[await store.dispatch(
            'fetchFilteredProducts', 
            `?sort_by=${products_sort_option.value}${url}&pg=${paginate_to}`
        )]
    )
    current_pagination_page.value = paginate_to
    
}

</script>

<style scoped>
    @import url('@/assets/css/product_filters.css');
</style>
