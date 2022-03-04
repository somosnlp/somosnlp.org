<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const routes_open_source = router.getRoutes()
    .filter(
        i => i.path.startsWith('/resources/open_source')
    )
const routes_notebooks = router.getRoutes()
    .filter(
        i => i.path.startsWith('/resources/notebook')
    )
</script>

<template>
    <header class="m-auto text-center prose">
        <h1>Recursos Open-Source</h1>
    </header>

    <hr class="mx-auto mt-8 mb-12 prose" />

    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes_open_source" :key="route.path" :route="route" />
    </div>

    <hr class="mx-auto mt-12 mb-12 prose" />

    <h2 class="text-3xl font-bold m-auto text-center prose">Notebooks</h2>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes_notebooks" :key="route.path" :route="route" />
    </div>
    <div class="my-12 flex justify-center">
        <img
            src="https://somosnlp.github.io/assets/images/undraw_education_edited.svg"
            width="300"
            height="365"
        />
    </div>
</template>
