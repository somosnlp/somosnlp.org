<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useLanguage } from '~/composables/useLanguage'
import { computed } from 'vue'

const isProduction = import.meta.env.PROD
const router = useRouter()
const { language } = useLanguage()

const routes = computed(() => {
    return router.getRoutes()
        .filter(i => {
            // Basic blog post filters
            const isBlogPost = i.path.startsWith('/blog/')
            const hasDate = (i.meta as any).frontmatter?.date
            const notExample = !isProduction || !i.path.startsWith('/blog/examples')
            
            // Filter out English translations in Spanish mode
            // and Spanish versions in English mode
            const isEnglishPost = i.path.endsWith('.en')
            const matchesLanguage = language.value === 'en' ? isEnglishPost : !isEnglishPost
            
            return isBlogPost && hasDate && notExample && matchesLanguage
        })
        .sort((a, b) => +new Date((b.meta as any).frontmatter.date) - +new Date((a.meta as any).frontmatter.date))
})
</script>

<template>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
        <BlogItem v-for="route in routes" :key="route.path" :route="route" />
    </div>
</template>
