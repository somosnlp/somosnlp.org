<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useHead } from '@vueuse/head'
import { columnas, ofertas } from './ofertas'

const { t } = useI18n()
const searchQuery = ref('')

useHead({
    title: 'Bolsa de Empleo de PLN - SomosNLP',
    meta: [
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Bolsa de Empleo PLN - SomosNLP' },
        { name: 'twitter:description', content: 'Ofertas de empleo e investigación en el ámbito del PLN.' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/logo.png' },
        { name: 'twitter:image:alt', content: 'Logo de la comunidad SomosNLP' }
    ]
})
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>{{ t('jobs.title') }}</h1>
            <p class="text-lg">
                {{ t('jobs.subtitle') }} 🚀
            </p>
            <div class="justify-center items-center mx-65">
                <IconButtonLink
                    :url='`https://twitter.com/intent/tweet?text=¡Nuevas ofertas en la bolsa de empleo de @SomosNLP_! \n\n\n Descúbrelas aquí: https://somosnlp.org/empleo`'>
                    <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                    <span class="font-medium text-sm">{{ t('share') }}</span>
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
                {{ t('jobs.disclaimer') }}
            </p>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-2xl">
                👏 {{ t('jobs.total') }} - 51 👏
            </p>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div class="grid grid-cols-2">
            <div>
                <p class="m-auto text-center prose text-2xl">{{ t('jobs.looking_for_job') }}</p>
                <p class="m-auto text-center prose">{{ t('jobs.follow_us') }}</p>
                <p class="m-auto text-center prose">
                    <a href="https://twitter.com/SomosNLP_" target="_blank">Twitter</a>,
                    <a href="https://www.linkedin.com/company/somosnlp" target="_blank">LinkedIn</a> {{ t('jobs.and_discord') }}
                    <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a> ✅
                </p>
            </div>
            <div>
                <p class="m-auto text-center prose text-2xl">{{ t('jobs.looking_for_talent') }}</p>
                <p class="m-auto text-center prose">
                    {{ t('jobs.post_job_1') }}
                </p>
                <p class="m-auto text-center prose">
                    <a class="contents" href="https://forms.gle/H4LenjP1FGWgE6r4A" target="_blank">{{ t('jobs.post_job_2') }}</a> 📝
                </p>
            </div>
        </div>
    </Container>
</template>
