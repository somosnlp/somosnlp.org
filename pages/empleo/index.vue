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
        { name: 'twitter:card', content: 'Bolsa de Empleo NLP' },
        { name: 'twitter:creator', content: '@somosnlp_' },
    ]
})

const searchQuery = ref('')
const gridColumns = ['título', 'contrato', 'institución', 'nº trabajadores/as', 'localización', 'fecha', 'descripción']

const somos_nlp_data_scientist = {
    título: 'Data Scientist',
    contrato: 'T. Completo',
    institución: 'Somos NLP',
    "nº trabajadores/as": '0 - 9',
    localización: 'Remoto 100%',
    fecha: '2022/09/09',
    descripción: 'somosnlp.org'
}

const somos_nlp_nlp_engineer = {
    título: 'NLP Engineer',
    contrato: 'T. Parcial',
    institución: 'Somos NLP',
    "nº trabajadores/as": '10 - 49',
    localización: 'Presencial Madrid',
    fecha: '2022/10/01',
    descripción: 'somosnlp.org'
}

const somos_nlp_volunteer = {
    título: 'Volunteer',
    contrato: 'Prácticas',
    institución: 'Somos NLP',
    "nº trabajadores/as": 'Más de 250',
    localización: 'Híbrido Alicante',
    fecha: '2022/07/01',
    descripción: 'somosnlp.org'
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
        <div class="m-auto text-center grid">
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
                Rellena
                <a class="contents" href="https://forms.gle/H4LenjP1FGWgE6r4A" target="_blank">este
                    formulario</a>.
            </p>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-sm">
                Esta bolsa de empleo sigue en proceso de desarrollo, agradecemos feedback en forma de
                <a class="contents" href="https://github.com/somosnlp/somosnlp.org" target="_blank">issues</a>
                o por email a mariagrandury@gmail.com.
            </p>
        </div>
    </Container>
</template>
