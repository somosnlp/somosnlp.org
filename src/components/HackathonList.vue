<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/hackathon/')
            && (i.meta as any).frontmatter.date
    )
    .sort((a, b) => +new Date((b.meta as any).frontmatter.date) + +new Date((a.meta as any).frontmatter.date))
</script>

<template>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-3">
        <BlogItem v-for="route in routes" :key="route.path" :route="route" />
    </div>
</template>
