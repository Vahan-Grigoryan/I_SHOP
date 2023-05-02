<template>
<div class="pagination">
    <button class="prevnextpage_btn">
        <img src="@/assets/img/prevnextbtn.png" alt="">
    </button>
    
    <a 
    class="page_a"
    v-for="_ in pages_per_view"
    @click="goToPage(_)"
    :ref="`page_${_}`"
    >
        {{ _ }}
    </a>

    <button class="prevnextpage_btn">
        <img src="@/assets/img/prevnextbtn.png" alt="">
    </button>
    
</div>
</template>

<script>
export default {
    name: 'ui-pagination',
    props: {
        pages_per_view: Number
    },
    methods: {
        goToPage(page){
            Object.keys(this.$refs).forEach( page_key => {
                this.$refs[page_key][0].classList.remove('pagination_a_active')
            })
            console.log(this.$refs[`page_${page}`][0].classList.add('pagination_a_active'))
            // CONTINUOUS...
        },
        // PREV, NEXT BUTTONS LOGIC...
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