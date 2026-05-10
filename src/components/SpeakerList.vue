<script setup lang="ts">
import { computed } from 'vue'
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
            && (!props.year || (i.meta as any).frontmatter.community.includes(`Ponente ${props.year}`))
    )
    .sort(
        (a, b) =>
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    )

const gridClass = computed(() => {
    switch (props.cols) {
        case 1: return 'auto-rows-fr grid gap-6 lg:grid-cols-1'
        case 2: return 'auto-rows-fr grid gap-6 lg:grid-cols-2'
        case 3: return 'auto-rows-fr grid gap-6 lg:grid-cols-3'
        default: return 'auto-rows-fr grid gap-6 lg:grid-cols-4'
    }
})
</script>

<template>
    <div :class="gridClass">
        <ProfileItemRouter v-for="route in routes" :route="route" />
    </div>
</template>
