<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useHead } from '@vueuse/head'
import { columnas, ofertas } from './ofertas'

const { t } = useI18n()
const searchQuery = ref('')

useHead({
    meta: [
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Bolsa de Empleo PLN' },
        { name: 'twitter:description', content: 'Ofertas de empleo e investigación en el ámbito del PLN.' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/logo.png' },
        { name: 'twitter:image:alt', content: 'Logo de la comunidad Somos NLP' }
    ]
})
</script>
    
<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Bolsa de Empleo de PLN</h1>
            <p class="text-lg">
                Encuentra ofertas de empleo e investigación relacionadas con el Procesamiento del Lenguaje Natural 🚀
            </p>
            <div class="justify-center items-center mx-65">
                <IconButtonLink
                    :url='`https://twitter.com/intent/tweet?text=¡Nuevas ofertas en la bolsa de empleo de @SomosNLP_! \n\n\n Descúbrelas aquí: https://somosnlp.org/empleo`'>
                    <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                    <span class="font-medium text-sm">Compartir</span>
                </IconButtonLink>
            </div>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div class="m-auto text-center grid px-10">
            <form id="search">
                {{ t('jobs.search') }} <input name="query" v-model="searchQuery"
                    class="border-accent-200 border-2px rounded-sm outline-transparent bg-transparent">
            </form>
            <br />
            <TableJobs :data="ofertas" :columns="columnas" :filter-key="searchQuery">
            </TableJobs>
        </div>
        <div class="mt-8 mb-12">
            <p class="m-auto text-center prose italic">
                Las entidades son responsables de publicar información correcta y actualizarla.
            </p>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-2xl">
                👏 Total Ofertas Publicadas: 37 👏
            </p>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div class="grid grid-cols-2">
            <div>
                <p class="m-auto text-center prose text-2xl">BUSCO EMPLEO</p>
                <p class="m-auto text-center prose">¡Síguenos! Anunciamos las ofertas en</p>
                <p class="m-auto text-center prose">
                    <a href="https://twitter.com/SomosNLP_" target="_blank">Twitter</a>,
                    <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a> y el canal #empleo de
                    <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a> ✅
                </p>
            </div>
            <div>
                <p class="m-auto text-center prose text-2xl">BUSCO TALENTO</p>
                <p class="m-auto text-center prose">
                    Para que aparezca aquí tu oferta de empleo
                </p>
                <p class="m-auto text-center prose">
                    <a class="contents" href="https://forms.gle/H4LenjP1FGWgE6r4A" target="_blank">rellena este
                        formulario</a> 📝
                </p>
            </div>
        </div>
    </Container>
</template>
