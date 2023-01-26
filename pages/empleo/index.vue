<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useHead } from '@vueuse/head'
import { columnas, ofertas } from './ofertas'

const { t } = useI18n()
const searchQuery = ref('')

useHead({
    meta: [
        { property: 'og:title', content: 'Bolsa de Empleo NLP' },
        { property: 'og:description', content: 'Ofertas de empleo e investigación en el ámbito del PLN.' },
        { property: 'og:image', content: 'https://somosnlp.github.io/assets/logo.png' },
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
    ]
})
</script>
    
<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Bolsa de Empleo de NLP</h1>
            <p class="text-lg">
                Encuentra ofertas de empleo e investigación relacionadas con el Procesamiento del Lenguaje Natural.
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div class="m-auto text-center grid px-10">
            <form id="search">
                {{ t('jobs.search') }} <input name="query" v-model="searchQuery"
                    class="border-accent-200 border-2px rounded-sm outline-transparent bg-transparent">
            </form>
            <br />
            <Table :data="ofertas" :columns="columnas" :filter-key="searchQuery">
            </Table>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-lg">
                ¿Estás buscando talento y quieres que aparezca aquí tu oferta de empleo?
            </p>
            <p class="m-auto text-center prose text-lg">
                <a class="contents" href="https://forms.gle/H4LenjP1FGWgE6r4A" target="_blank">Rellena este
                    formulario</a>.
            </p>
        </div>
    </Container>
</template>
