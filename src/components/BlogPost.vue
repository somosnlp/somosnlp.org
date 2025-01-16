<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue';
import { useHead } from '@vueuse/head'
import { useRoute } from 'vue-router';

import { useI18n } from 'vue-i18n';
const { d } = useI18n();

interface SuggestedPost {
    path: string;
    title: string;
    cover?: string;
    description?: string;
}

const { frontmatter } = defineProps<{ frontmatter: any }>()

// Import all blog posts metadata
const modules = import.meta.glob('/pages/blog/*.md')
const blogPosts: Record<string, any> = {}

// Load all blog posts on mount
onMounted(async () => {
    await Promise.all(
        Object.entries(modules).map(async ([path, loader]) => {
            const mod = await loader() as any
            blogPosts[path] = mod
        })
    )
})

// Add computed property for suggested posts paths
const hasSuggestedPosts = computed(() => 
    frontmatter.suggestedPosts && 
    Array.isArray(frontmatter.suggestedPosts) && 
    frontmatter.suggestedPosts.length > 0
)

// Initialize suggestedPostsData ref
const suggestedPostsData = ref<SuggestedPost[]>([])

// Watch for blog posts loading and update suggested posts
watch(blogPosts, () => {
    if (!hasSuggestedPosts.value) return

    try {
        const posts = frontmatter.suggestedPosts.map((path: string) => {
            const fullPath = `/pages${path}.md`
            const post = blogPosts[fullPath]
            return {
                path,
                title: post?.frontmatter?.title || path.split('/').pop()?.replace(/-/g, ' ') || 'Related Post',
                cover: post?.frontmatter?.cover,
                description: post?.frontmatter?.description
            } as SuggestedPost
        })
        suggestedPostsData.value = posts
    } catch (error) {
        console.error('Error fetching suggested posts:', error)
    }
}, { immediate: true })

useHead({
    title: 'SomosNLP - Democratizando el NLP en español',
    meta: [
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        {
            name: 'twitter:title',
            content: computed(
                () => frontmatter.title
                    ? frontmatter.title
                    : 'SomosNLP - Democratizando el NLP en español')
        },
        {
            name: 'twitter:description',
            content: computed(
                () => frontmatter.description
                    ? frontmatter.description
                    : '¡Mira que artículo tan interesante!')
        },
        {
            name: 'twitter:image',
            content: computed(
                () => frontmatter.cover
                    ? frontmatter.cover
                    : 'https://somosnlp.github.io/assets/logo.png')
        },
        { name: 'twitter:image:alt', content: 'Logo de la comunidad SomosNLP' }
    ]
})

const route = useRoute()
const base = 'https://somosnlp.org'
const tweetUrl = computed(() => `https://twitter.com/intent/tweet?text=${encodeURIComponent(`¡Qué interesante este artículo de @SomosNLP_! \n\n ${base}${route.path}`)}`)
const linkUrl = computed(() => `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(`${base}${route.path}`)}`);
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>{{ frontmatter.title }}</h1>
            <p v-if="frontmatter.description" class="text-lg">{{ frontmatter.description }}</p>
            <div class="text-lg opacity-50">
                <span v-if="frontmatter.author">{{ frontmatter.author }}</span>
                <span v-if="frontmatter.date"> · {{ d(frontmatter.date, "short") }}</span>
                <span v-if="frontmatter.duration"> · {{ frontmatter.duration }}</span>
            </div>
            <div v-if="frontmatter.author" class="grid items-baseline">
                <div class="mt-5 grid lg:grid-cols-2">
                    <div class="justify-center mx-25">
                        <IconButtonLink :url='tweetUrl'>
                            <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                            <span class="font-medium text-sm">Compartir</span>
                        </IconButtonLink>
                    </div>
                    <div class="justify-center mx-25">
                        <IconButtonLink :url='linkUrl'>
                            <carbon:logo-linkedin class="inline align-middle mr-2 text-lg" />
                            <span class="font-medium text-sm">Compartir</span>
                        </IconButtonLink>
                    </div>
                </div>
            </div>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <!-- Diferenciación necesaria para la correcta visualización de las tablas en recursos -->
        <article v-if="frontmatter.tablePage">
            <slot />
        </article>
        <article v-else class="m-auto prose">
            <slot />
        </article>
        <hr v-if="frontmatter.author" class="mx-auto mt-8 mb-4 prose" />
        <footer class="m-auto prose">
            <div v-if="frontmatter.author" class="grid grid-cols-2 items-baseline">
                <h3 text="lg">{{ frontmatter.author }}</h3>
                <div class="flex flex-wrap gap-3 items-center justify-self-center">
                    <div class="border-2 border-accent-400 rounded">
                        <IconButtonLink :url="tweetUrl">
                            <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                            <span class="font-medium text-sm">Compartir</span>
                        </IconButtonLink>
                    </div>
                    <div class="border-2 border-accent-400 rounded">
                        <IconButtonLink :url="linkUrl">
                            <carbon:logo-linkedin class="inline align-middle mr-2 text-lg" />
                            <span class="font-medium text-sm">Compartir</span>
                        </IconButtonLink>
                    </div>
                </div>
            </div>
            <p class="text-md" v-if="frontmatter.bio">{{ frontmatter.bio }}</p>
            <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
                <IconButtonLink v-if="frontmatter.website" :url="frontmatter.website" class="contents">
                    <carbon:user-avatar-filled-alt />
                </IconButtonLink>
                <IconButtonLink v-if="frontmatter.twitter" :url="frontmatter.twitter" class="contents">
                    <carbon:logo-twitter />
                </IconButtonLink>
                <IconButtonLink v-if="frontmatter.linkedin" :url="frontmatter.linkedin" class="contents">
                    <carbon:logo-linkedin />
                </IconButtonLink>
                <IconButtonLink v-if="frontmatter.github" :url="frontmatter.github" class="contents">
                    <carbon:logo-github />
                </IconButtonLink>
                <IconButtonLink v-if="frontmatter.huggingface" :url="frontmatter.huggingface" class="contents">
                    🤗
                </IconButtonLink>
            </div>
            <div v-if="hasSuggestedPosts && suggestedPostsData.length > 0" class="mt-12">
                <hr class="mb-8" />
                <h3 class="text-xl font-bold mb-6">Artículos relacionados</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div v-for="post in suggestedPostsData" :key="post.path" 
                         class="border rounded-lg overflow-hidden hover:shadow-lg transition-shadow">
                        <RouterLink :to="post.path" class="block">
                            <img v-if="post.cover" :src="post.cover" :alt="post.title" 
                                 class="w-full h-48 object-cover" />
                            <div class="p-4">
                                <h4 class="text-lg font-semibold">{{ post.title }}</h4>
                                <p v-if="post.description" class="mt-2 text-sm text-gray-600">{{ post.description }}</p>
                            </div>
                        </RouterLink>
                    </div>
                </div>
            </div>
            <div v-if="$route.path.startsWith('/blog')" class="text-md text-center">
                <hr class="mt-8 mb-12" />
                <a target="_blank"
                    href="https://github.com/somosnlp/somosnlp.org/blob/main/CONTRIBUTING.md#-publicar-un-art%C3%ADculo-en-el-blog">
                    ¿Te gustaría publicar en nuestro blog?
                </a>
            </div>
        </footer>
    </Container>
</template>
