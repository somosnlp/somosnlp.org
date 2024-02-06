<script setup lang="ts">
import { useHead } from '@vueuse/head'

// https://github.com/vueuse/head
// you can use this to manipulate the document head in any components,
// they will be rendered correctly in the html results with vite-ssg
useHead({
  title: 'SomosNLP - Democratizando el NLP en español',
  meta: [
    {
      name: 'description', content: 'Comunidad internacional de hispanohablantes que estudian, trabajan e investigan en el campo del PLN, ¡únete!'
    },
    { name: 'keywords', content: 'NLP, PLN, español, divulgación, IA' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:site', content: '@somosnlp_' },
    { name: 'twitter:creator', content: '@somosnlp_' },
    { name: 'twitter:title', content: 'SomosNLP - Democratizando el NLP en español' },
    { name: 'twitter:description', content: 'Comunidad internacional de hispanohablantes que estudian, trabajan e investigan en el campo del PLN, ¡únete!' },
    { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/logo.png' },
    { name: 'twitter:image:alt', content: 'Logo de la comunidad SomosNLP' }
  ],
})
</script>

<template>
  <Container class="overflow-x-auto" border="b gray-200 dark:gray-700">
    <NavBar />
  </Container>
  <router-view />
  <Container border="t gray-200 dark:gray-700">
    <Footer />
  </Container>
</template>
