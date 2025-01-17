<script setup lang="ts" >
import { useHead } from '@vueuse/head'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

useHead({
    title: 'SomosNLP - Recursos open-source de NLP en español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'SomosNLP - Recursos open-source de PLN en español' },
        { name: 'twitter:description', content: '¡Fórmate con el equipo de SomosNLP!' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/logo.png' },
        { name: 'twitter:image:alt', content: 'Logo de la comunidad SomosNLP' }
    ]
})
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>{{ t('resources.title') }}</h1>
            <p>{{ t('resources.subtitle') }}</p>
        </header>

        <hr class="mx-auto mt-8 mb-12 prose" />
        <div class="my-8 flex justify-center">
            <img src="https://somosnlp.github.io/assets/images/ilustraciones/undraw_education_edited.svg" alt="Recursos"
                width="200" height="230" />
        </div>  
        <ResourcesList />
    </Container>
</template>

<!-- 
- Para aprender de ML si sabes programar, fast.ai 
- Un curso que a mi me gusta mucho y es abierto y bonito https://lena-voita.github.io/nlp_course/language_modeling.html
- Un curso que hicimos que explican muuuuy a fondo varios de los tasks de transformers y como entrenar modelos para ti https://huggingface.co/course/chapter1/1  -->
