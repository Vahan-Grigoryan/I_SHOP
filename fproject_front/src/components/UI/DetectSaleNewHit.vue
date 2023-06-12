<template>
    <div v-if="sale_new_hit.length > 4" :class="getBoxClass('sale')">
        -{{ sale_new_hit.slice(4) }}%
    </div>
    <div v-else-if="sale_new_hit.toLowerCase().includes('hit')" :class="getBoxClass('hit')">
        {{ sale_new_hit }}
    </div>
    <div v-else :class="getBoxClass('new')">
        {{ sale_new_hit }}
    </div>
</template>

<script>
export default {
    name: 'ui-detect-salenewhit',
    props: {
        sale_new_hit: String
    },
    methods: {
        getBoxClass(productSaleNewHit){
            const definition = {
                sale: {sale_hit_new_box50: true},
                new: {sale_hit_new_boxnew: true},
                hit: {sale_hit_new_boxhit: true},
            }
            return definition[productSaleNewHit]
            
        }
    }
}
</script>

<style scoped>

</style>