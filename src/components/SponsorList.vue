<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/patrocinios/')
            && !i.path.startsWith('/patrocinios/0-plantilla')
            && (i.meta as any).frontmatter.type
    )
    .sort(
        (a, b) =>
            ((a.meta as any).frontmatter.type.localeCompare((b.meta as any).frontmatter.type)) ||
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    );

</script>

<template>
    <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
        <SponsorInfoRouter v-for="route in routes" :route="route" />
    </div>
</template>
