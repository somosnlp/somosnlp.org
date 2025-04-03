<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/')
            && (i.meta as any).frontmatter.community
            && (i.meta as any).frontmatter.community.includes('Ponente')
    )
    .sort(
        (a, b) =>
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    )
</script>

<template>
    <div class="auto-rows-fr mx-12 grid gap-6 lg:grid-cols-3">
        <ProfileItemRouter v-for="route in routes" :route="route" />
    </div>
</template>
