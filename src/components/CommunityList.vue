<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const founder_routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/maria-grandury') ||
            i.path.startsWith('/comunidad/manuel-romero')
    )
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/')
            && !i.path.startsWith('/comunidad/maria-grandury')
            && !i.path.startsWith('/comunidad/manuel-romero')
            && !i.path.startsWith('/comunidad/0-plantilla')
            && (i.meta as any).frontmatter.community
            && (i.meta as any).frontmatter.community !== 'Ponente'
    )
    .sort(
        (a, b) =>
            ((a.meta as any).frontmatter.community.localeCompare((b.meta as any).frontmatter.community)) ||
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    )
</script>

<template>
    <div class="auto-rows-fr mx-12 grid gap-6 lg:mx-36 lg:grid-cols-2">
        <ProfileItemRouter v-for="route in founder_routes" :route="route" />
    </div>
    <div class="auto-rows-fr mx-12 grid gap-6 lg:grid-cols-3">
        <ProfileItemRouter v-for="route in routes" :route="route" />
    </div>
</template>
