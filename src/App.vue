<script setup lang="ts">
import { useHead } from '@vueuse/head'

// https://github.com/vueuse/head
// you can use this to manipulate the document head in any components,
// they will be rendered correctly in the html results with vite-ssg
useHead({
  title: 'NLP en ES',
  meta: [
    {
      name: 'description', content: 'Comunidad de profesionales, investigadores y estudiantes acelerando el avance del NLP en Español.'

    },
    { property: 'og:title', content: 'NLP en ES' },
    { property: 'og:image', content: 'https://nlp-en-es.github.io/assets/logo.png' },
    { name: 'twitter:card', content: 'summary' },
    { name: 'twitter:creator', content: '@NLP_en_ES' },
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
