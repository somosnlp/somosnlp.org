<script setup lang="ts">
import { computed } from 'vue';
import { useHead } from '@vueuse/head'
import { useI18n } from "vue-i18n";
import { useRoute } from 'vue-router';
const { d } = useI18n();

const { frontmatter } = defineProps<{ frontmatter: any }>()

useHead({
    title: 'Somos NLP - Democratizando el NLP en español',
    meta: [
        {
            property: 'og:title',
            content: computed(
                () => frontmatter.title
                    ? frontmatter.title
                    : 'Somos NLP - Democratizando el NLP en español')
        },
        {
            property: 'og:description',
            content: computed(
                () => frontmatter.description
                    ? frontmatter.description
                    : '¡Mira que artículo tan interesante!')
        },
        {
            property: 'og:image',
            content: computed(
                () => frontmatter.cover
                    ? frontmatter.cover
                    : 'https://somosnlp.github.io/assets/logo.png')
        },
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
    ]
})

const route = useRoute()
const base = 'https://somosnlp.org'
const tweetUrl = computed(() => `https://twitter.com/intent/tweet?text=${encodeURIComponent(`¡Qué interesante este artículo de @SomosNLP_! \n\n ${base}${route.path}`)}`)
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>{{ frontmatter.title }}</h1>
            <p class="text-lg">{{ frontmatter.description }}</p>
            <div class="text-lg opacity-50">
                <span v-if="frontmatter.date">{{ d(frontmatter.date, 'long') }}</span>
                <span v-if="frontmatter.duration">· {{ frontmatter.duration }}</span>
            </div>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <article class="m-auto prose">
            <slot />
        </article>
        <hr v-if="frontmatter.author" class="mx-auto mt-8 mb-4 prose" />
        <footer class="m-auto prose">
            <div class="grid grid-cols-2 items-baseline">
                <h3 text="lg" v-if="frontmatter.author">{{ frontmatter.author }}</h3>
                <div class="justify-self-end border-2 border-accent-400 rounded">
                    <IconButtonLink :url="tweetUrl">
                        <carbon:logo-twitter class="inline align-middle mr-2 text-lg" />
                        <span class="font-medium text-sm">Compartir</span>
                    </IconButtonLink>
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
            </div>
        </footer>
    </Container>
</template>
