<script setup lang="ts">
import { computed } from 'vue'
import { formatDate } from '~/logic'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const { frontmatter } = defineProps<{ frontmatter: any }>()
const date = computed(() => formatDate(frontmatter.date, locale.value))
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>{{ frontmatter.title }}</h1>
            <p class="text-lg">{{ frontmatter.description }}</p>
            <div class="text-lg opacity-50">
                {{ date }}
                <span v-if="frontmatter.duration">· {{ frontmatter.duration }}</span>
            </div>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <article class="m-auto prose">
            <slot />
        </article>
    </Container>
</template>
