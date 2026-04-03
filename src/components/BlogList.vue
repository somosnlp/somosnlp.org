<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useLanguage } from '~/composables/useLanguage'
import { computed } from 'vue'

const props = defineProps<{ tag?: string }>()

const isProduction = import.meta.env.PROD
const router = useRouter()
const { language } = useLanguage()

const routes = computed(() => {
    const allRoutes = router.getRoutes()

    const blogRoutes = allRoutes.filter(i => {
        // Blog post filters
        const isBlogPost = i.path.startsWith('/blog/')
        const hasDate = (i.meta as any).frontmatter?.date
        const notExample = !isProduction || !i.path.startsWith('/blog/examples')

        // Filter out English translations in Spanish mode
        // and Spanish versions in English mode
        const isEnglishPost = i.path.endsWith('.en')
        const matchesLanguage = language.value === 'en' ? isEnglishPost : !isEnglishPost
        return isBlogPost && hasDate && notExample && matchesLanguage
    })

    const conferenciaRoutes = allRoutes.filter(i =>
        i.path.startsWith('/conferencias/') && (i.meta as any).frontmatter?.title
    )

    const combined = [...blogRoutes, ...conferenciaRoutes]

    const filtered = props.tag
        ? combined.filter(i => ((i.meta as any).frontmatter?.tags ?? []).includes(props.tag))
        : combined

    return filtered.sort((a, b) => {
        const dateA = (a.meta as any).frontmatter?.date
        const dateB = (b.meta as any).frontmatter?.date
        if (dateA && dateB) return +new Date(dateB) - +new Date(dateA)
        if (dateA) return -1
        if (dateB) return 1
        return 0
    })
})
</script>

<template>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes" :key="route.path" :route="route" />
    </div>
</template>
