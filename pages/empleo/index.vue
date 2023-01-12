<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useHead } from '@vueuse/head'

const { t } = useI18n()

useHead({
    meta: [
        { property: 'og:title', content: 'Bolsa de Empleo NLP' },
        { property: 'og:description', content: 'Ofertas de empleo e investigación en el ámbito del PLN.' },
        { property: 'og:image', content: 'https://somosnlp.github.io/assets/logo.svg' },
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
    ]
})

const searchQuery = ref('')
const gridColumns = ['ocupación', 'contrato', 'entidad', 'nº trabajadores/as', 'localización', 'fecha publicación', 'más']

const somos_nlp_data_scientist = {
    ocupación: 'Data Scientist',
    "palabras clave": 'traducción',
    contrato: 'T. Completo',
    entidad: 'Somos NLP',
    "nº trabajadores/as": '0 - 9',
    localización: 'Remoto 100%',
    "fecha publicación": '2022/09/09',
    más: 'https://somosnlp.org'
}

const somos_nlp_nlp_engineer = {
    ocupación: 'NLP Engineer',
    "palabras clave": 'traducción',
    contrato: 'T. Parcial',
    entidad: 'Somos NLP',
    "nº trabajadores/as": '10 - 49',
    localización: 'Presencial Madrid',
    "fecha publicación": '2022/10/01',
    más: 'https://somosnlp.org/blog'
}

const somos_nlp_volunteer = {
    ocupación: 'Volunteer',
    "palabras clave": 'traducción',
    contrato: 'Prácticas',
    entidad: 'Somos NLP',
    "nº trabajadores/as": 'Más de 250',
    localización: 'Híbrido Alicante',
    "fecha publicación": '2022/07/01',
    más: 'https://somosnlp.org/hackathon'
}

const gridData = [
    somos_nlp_data_scientist,
    somos_nlp_nlp_engineer,
    somos_nlp_volunteer,
]
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
            <Table :data="gridData" :columns="gridColumns" :filter-key="searchQuery">
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
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-sm">
                Acabamos de publicar esta bolsa de empleo,
                agradecemos feedback y sugerencias en forma de
                <a class="contents" href="https://github.com/somosnlp/somosnlp.org" target="_blank">issues</a>
                o por email a info@somosnlp.org.
            </p>
        </div>
    </Container>
</template>
