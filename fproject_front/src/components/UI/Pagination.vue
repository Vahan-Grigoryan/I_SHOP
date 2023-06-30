<template>
<div class="pagination" v-if="pages > 1">
    <button 
    class="prevnextpage_btn"
    @click="page_active-1 > 0 && $emit('paginated_to', page_active-1)"
    >
        <img src="@/assets/img/prevnextbtn.png" alt="">
    </button>
    
    <a 
    v-for="page in pages"
    :class="getClasses(page)"
    @click="$emit('paginated_to', page)"
    >
        {{ page }}
    </a>

    <button 
    class="prevnextpage_btn"
    @click="page_active+1 <= pages && $emit('paginated_to', page_active+1)"
    >
        <img src="@/assets/img/prevnextbtn.png" alt="">
    </button>
    
</div>
</template>

<script>
// Pagination for this project, used in many places
// props:
//      pages: how many pages are available for redirect in each pagination page


export default {
    name: 'ui-pagination',
    props: {
        pages: Number,
        page_active: Number,
    },
    methods: {
        getClasses(page){
            return {
                page_a: true,
                pagination_a_active: this.page_active == page
            }
        },
    },
}
</script>

<style scoped>
.pagination{
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.prevnextpage_btn{
    background: #F4F5F9;
    border: 1px solid #E4E7EE;
    cursor: pointer;
    border-radius: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 50px;
}
.prevnextpage_btn:first-child > img{
    transform: rotateZ(180deg);
}
.page_a{
    display: inline-block;
    background: white;
    width: 50px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #E4E7EE;
    font-size: 18px;
    cursor: pointer;
    border-radius: 50px;
}
.page_a:hover{
    border: 1px solid #74CCD8;
}
.pagination_a_active{
    background: #74CCD8;
    color:white;
    border: none
}



















</style>