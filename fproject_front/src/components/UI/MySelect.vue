<template>
    <div class="select_for_filters" v-if="purpose=='filters'">
        <div 
        :class="{
            selected_option_for_filters: true,
            select_clicked: options_visible_filters
        }"
        @click="setFilterOptionsVisible"
        >
            {{ selected_option }}
            <img src="@/assets/img/select_down_arrow.png" v-if="!options_visible_filters">
            <img src="@/assets/img/filter_top_arrow.png" v-if="options_visible_filters">
        </div>
        <div class="options_for_filters" v-if="options_visible_filters">
            <slot name="custom_content">
                <p v-for="option in options">
                    {{ option }}
                </p>
            </slot>
        </div>
    </div>
    <div class="select" v-else-if="purpose=='detail'">
        <div 
        :class="{
            selected_option: true,
            selected_option_focused: selected
        }"
        @click="show_options"
        >
            {{ selected_option }}
            <img src="@/assets/img/Vector_31.png" alt="">
        </div>
        <div class="options" v-if="options_visible">
            <div 
            class="option"
            v-for="option in options"
            @click="select_option_no_filters(option)"
            >
                {{ option }}
            </div>
        </div>
    </div>
    <div class="cart_order_select" v-else-if="purpose=='cart_products'">
        <div 
        :class="{
            row_info: true, 
            bbordered: options_visible_cart
        }"
        @click="setCartProductsVisible"
        >
            <slot name="row_info"></slot>
        </div>
        <slot name="products" v-if="options_visible_cart"></slot>
    </div>
</template>

<script>
// Best select for different purposes in this project,
// used in many places
// props: 
//      purpose: define template structure by purpose
//      selected_option: with purpose=detail can used with v-model in parent component => change select value
//      options: options for select 


export default {
    name: 'ui-select',
    props: {
        options: Array,
        selected_option: {
            type: String,
            default: 'Select option'
        },
        purpose: {
            type: String,
            default: 'filters'
        },

    },
    data(){
        return {
            selected: false,
            options_visible: false,
            options_visible_filters: false,
            options_visible_cart: false,
        }
    },
    methods: {
        show_options(){
            this.selected = !this.selected
            this.options_visible = !this.options_visible
        },
        select_option_no_filters(option){
            this.show_options()
            this.$emit('update:selected_option', option)
        },
        setFilterOptionsVisible(){

            this.options_visible_filters = !this.options_visible_filters
        },
        setCartProductsVisible(){
            this.options_visible_cart = !this.options_visible_cart
        }
    },
}
</script>

<style scoped>
.select{
    position: relative;
    z-index: 1;
}
.selected_option_focused{
    border-radius: 20px 20px 0px 0px !important;
}
.selected_option_focused img{
    transform: rotateX(180deg);
}
.selected_option{
    background: #F4F5F9;
    width: 100%;
    height: 100%;
    border-radius: 45px;
    padding: 10px 20px;
    font-size: 17px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.options{
    position: absolute;
    left: 0px;
    bottom: 0px;
    transform: translateY(100%);
    width: 100%;
}
.option{
    width: 100%;
    padding: 10px 20px;
    background: #F4F5F9;
    border-bottom: 1px solid #74CCD8;
    cursor: pointer;
}
.option:hover{
    background: #ededed;
}
.option:first-child{
    border-top: 1px solid #74CCD8;
}
.option:last-child{
    border:none;
    border-radius: 0px 0px 20px 20px;
}


.select_for_filters{
    position: relative;
    width: 100%;
    border-bottom: 1px solid #74CCD8;
}
.select_for_filters:last-child{
    border-bottom: none;
}
.selected_option_for_filters{
    width: 100%;
    padding: 15px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 18px;
    line-height: 139.02%;
    color: #090F24;         
}
.options_for_filters{
    padding: 15px;
}
.options_for_filters p{
    margin-bottom: 15px;
    cursor: pointer;
}
.options_for_filters p:hover{
    text-decoration: underline;
}
.options_for_filters p:last-child{
    margin: 0px;
}
.select_clicked{
    background: linear-gradient(180deg, #ED9BC1 0%, #ED9BB9 100%);
    color:white;
}



</style>