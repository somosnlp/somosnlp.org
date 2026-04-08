<script setup lang="ts">
const props = defineProps<{
  src: string
  title?: string
  height?: string
}>()
</script>

<template>
  <div class="my-8">
    <iframe
      :src="src"
      :title="title || 'Gradio Demo'"
      :style="{ height: height || '600px' }"
      class="gradio-demo"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
    <p class="text-center text-sm mt-2 opacity-75">
      <a :href="src" target="_blank" rel="noopener noreferrer">Abrir en una nueva pestaña</a>
    </p>
  </div>
</template>

<style scoped>
.gradio-demo {
  width: 100%;
  border: none;
  border-radius: 8px;
}
</style>
