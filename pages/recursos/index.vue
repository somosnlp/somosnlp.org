<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    title: 'Somos NLP - Recursos open-source de NLP en español',
    meta: [
        { property: 'og:title', content: 'Somos NLP - Recursos open-source de NLP en español' },
        { property: 'og:description', content: '¡Fórmate con el equipo de Somos NLP!' },
        { property: 'og:image', content: 'https://github.com/somosnlp/assets/raw/main/logo.png' },
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
    ]
})
</script>

<template>
    <Container class="my-12">
        <ResourcesList />
    </Container>
</template>
