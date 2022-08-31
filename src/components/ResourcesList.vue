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
        i => i.path.startsWith('/recursos/open-source')
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
    </header>

    <hr class="mx-auto mt-8 mb-12 prose" />
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes_open_source" :key="route.path" :route="route" />
    </div>
    <div class="my-12 flex justify-center">
        <img src="https://somosnlp.github.io/assets/images/undraw_education_edited.svg" width="300" height="365" />
    </div>

    <hr class="mx-auto mt-12 mb-12 prose" />
    <h2 class="text-3xl font-bold m-auto text-center prose">Tutoriales</h2>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes_notebooks" :key="route.path" :route="route" />
    </div>
    <div class="mx-auto text-center">
        <a href="https://youtube.com/c/somosnlp" target="_blank" class="button-accent">
            <carbon:logo-youtube />
            Vídeo Tutoriales
        </a>
    </div>
    <div class="my-12 flex justify-center">
        <img src="undraw_video_upload_3d4u.svg" width="300" height="365" />
    </div>
</template>
