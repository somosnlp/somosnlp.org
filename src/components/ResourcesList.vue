<script setup lang="ts">
import { RouteRecordNormalized, useRouter } from 'vue-router'

const router = useRouter()

function sort_alphabetically(a: RouteRecordNormalized, b: RouteRecordNormalized) {
    let fa = a.path, fb = b.path;
    if (fa < fb) {
        return -1
    }
    if (fa > fb) {
        return 1
    }
    return 0
}

const routes_open_source = router.getRoutes()
    .filter(
        i => i.path.startsWith('/recursos/datasets') ||
            i.path.startsWith('/recursos/modelos')
    )
    .sort((a, b) => sort_alphabetically(a, b))

const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/recursos/')
            && !i.path.startsWith('/recursos/datasets')
            && !i.path.startsWith('/recursos/modelos')
            && !i.path.startsWith('/recursos/tutoriales')
            && !i.path.startsWith('/recursos/wip')
    )
    .sort((a, b) => sort_alphabetically(a, b))

const routes_notebooks = router.getRoutes()
    .filter(
        i => i.path.startsWith('/recursos/tutoriales')
    )
    .sort((a, b) => sort_alphabetically(a, b))

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
        ¿Tu asociación o empresa tiene recursos abiertos y gratuitos de PLN en español? Compártenos el enlace por Discord o
        mándalo a
        info@somosnlp.org, lo incluiremos en la lista para que llegue a más gente 🚀
    </p>
</template>
        