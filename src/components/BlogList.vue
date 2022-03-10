<script setup lang="ts">
import { useRouter } from 'vue-router'

const isProduction = import.meta.env.PROD;
const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/blog/')
            && (i.meta as any).frontmatter.date
            && (!isProduction || !i.path.startsWith('/blog/examples'))
    )
    .sort((a, b) => +new Date((b.meta as any).frontmatter.date) - +new Date((a.meta as any).frontmatter.date))
</script>

<template>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <EventHackathonItem v-for="route in routes" :key="route.path" :route="route" />
    </div>
</template>
