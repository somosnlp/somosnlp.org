<script setup lang="ts">
import { useHead } from '@vueuse/head'

// https://github.com/vueuse/head
// you can use this to manipulate the document head in any components,
// they will be rendered correctly in the html results with vite-ssg
useHead({
  title: 'Somos NLP - Democratizando el NLP en español',
  meta: [
    {
      name: 'description', content: 'Comunidad internacional de estudiantes, profesionales y investigadores acelerando el avance del NLP en español, ¡únete!'

    },
    { property: 'og:title', content: 'Somos NLP - Democratizando el NLP en español' },
    { property: 'og:description', content: 'Comunidad internacional de estudiantes, profesionales y investigadores acelerando el avance del NLP en español, ¡únete!' },
    { property: 'og:image', content: 'https://somosnlp.github.io/assets/logo.png' },
    { name: 'twitter:card', content: 'summary' },
    { name: 'twitter:site', content: '@somosnlp_' },
    { name: 'twitter:creator', content: '@somosnlp_' },
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
