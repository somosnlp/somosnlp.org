<script setup lang="ts" >
import { useHead } from '@vueuse/head'

useHead({
    meta: [
        { property: 'og:title', content: 'Recursos Open-Source de NLP en Español' },
        { property: 'og:description', content: '¡Fórmate con el equipo de Somos NLP!' },
        { property: 'og:image', content: 'https://somosnlp.github.io/assets/logo.svg' },
        { name: 'twitter:card', content: 'Recursos Open-Source de NLP en Español' },
        { name: 'twitter:creator', content: '@somosnlp_' },
    ]
})
</script>

<template>
    <Container class="my-12">
        <ResourcesList />
    </Container>
</template>
