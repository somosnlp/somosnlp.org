<script setup lang="ts">
import { useRouter } from 'vue-router'

const props = defineProps<{
    year?: number
    cols?: number
}>()

const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/')
            && (i.meta as any).frontmatter.community
            && (i.meta as any).frontmatter.community.includes('Ponente')
            && (!props.year || (i.meta as any).frontmatter.community.includes(props.year.toString()))
    )
    .sort(
        (a, b) =>
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    )
</script>

<template>
    <div :class="`auto-rows-fr grid gap-6 lg:grid-cols-${props.cols || 4}`">
        <ProfileItemRouter v-for="route in routes" :route="route" />
    </div>
</template>
