<script setup lang="ts">
import { RouteRecordNormalized, useRouter } from 'vue-router'

const router = useRouter()

function sort_alphabetically(a: RouteRecordNormalized, b: RouteRecordNormalized) {
    return a.path.localeCompare(b.path);
}

function filterRoutes(startsWith: string[], notStartsWith: string[] = []) {
    return router.getRoutes()
        .filter(route => startsWith.some(sw => route.path.startsWith(sw)) && !notStartsWith.some(nsw => route.path.startsWith(nsw)))
        .sort(sort_alphabetically);
}

const routes_open_source = filterRoutes(['/recursos/datasets', '/recursos/modelos']);
const route_nlp_de_0_a_100 = filterRoutes(['/recursos/curso-nlp-de-0-a-100'])[0];
const routes = filterRoutes(['/recursos/'], ['/recursos/datasets', '/recursos/modelos', '/recursos/curso-nlp-de-0-a-100', '/recursos/tutoriales', '/recursos/wip']);
const routes_notebooks = filterRoutes(['/recursos/tutoriales']);
</script>
        
<template>
    <header class="m-auto text-center prose">
        <h1>Recursos Open-Source</h1>
        <p>Recursos abiertos y gratuitos para toda la comunidad hispanohablante</p>
    </header>

    <hr class="mx-auto mt-8 mb-12 prose" />
    <div class="my-8 flex justify-center">
        <img src="https://somosnlp.github.io/assets/images/undraw_education_edited.svg" alt="Recursos" width="200"
            height="230" />
    </div>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes_open_source" :key="route.path" :route="route" />
    </div>

    <hr class="mx-auto mt-8 mb-12 prose" />

    <div class="mx-auto mt-12 text-center max-w-200">
        <BlogItem :key="route_nlp_de_0_a_100.path" :route="route_nlp_de_0_a_100" />
    </div>

    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes" :key="route.path" :route="route" />
    </div>

    <hr class="mx-auto mt-12 mb-12 prose" />
    <h2 class="text-3xl font-bold m-auto text-center prose">Tutoriales</h2>

    <div class="mx-auto mt-12 text-center max-w-100">
        <a href="https://youtube.com/c/somosnlp?sub_confirmation=1" target="_blank" class="button-accent">
            <carbon:logo-youtube />
            Vídeo Tutoriales
        </a>
    </div>

    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes_notebooks" :key="route.path" :route="route" />
    </div>

    <div class="my-12 flex justify-center">
        <img src="https://somosnlp.github.io/assets/images/undraw_video_upload_3d4u.svg" alt="Tutoriales" width="300"
            height="365" />
    </div>

    <hr class="mx-auto mt-8 mb-12 prose" />
    <p class="m-auto text-center prose my-12">
        ¿Tu asociación o empresa tiene recursos abiertos y gratuitos de PLN en español? Compártenos el enlace por MD,
        Discord o
        mándalo a
        info@somosnlp.org, lo incluiremos en la lista para que llegue a más gente 🚀
    </p>
</template>
        