<template>
    <slot v-if="!loading_circle" />
    <div v-else class="loading_circle"></div>
</template>

<script setup>

const props = defineProps({
    loading_circle: false,
})
</script>
<style>
.loading_circle {
  display: inline-block;
  width: 40px;
  height: 40px;
}
.loading_circle:after {
  content: " ";
  display: block;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 6px solid #fff;
  border-color: #fff transparent #fff transparent;
  animation: loading_circle_animation 1.2s linear infinite;
}
@keyframes loading_circle_animation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>
