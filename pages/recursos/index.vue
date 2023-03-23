<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    title: 'Somos NLP - Recursos open-source de NLP en español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Somos NLP - Recursos open-source de PLN en español' },
        { name: 'twitter:description', content: '¡Fórmate con el equipo de Somos NLP!' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/logo.png' },
        { name: 'twitter:image:alt', content: 'Logo de la comunidad Somos NLP' }
    ]
})
</script>

<template>
    <Container class="my-12">
        <ResourcesList />
    </Container>
</template>

<!-- 
- Para aprender de ML si sabes programar, fast.ai 
- Un curso que a mi me gusta mucho y es abierto y bonito https://lena-voita.github.io/nlp_course/language_modeling.html
- Un curso que hicimos que explican muuuuy a fondo varios de los tasks de transformers y como entrenar modelos para ti https://huggingface.co/course/chapter1/1  -->
