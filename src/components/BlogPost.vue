<script setup lang="ts">
const { frontmatter } = defineProps<{ frontmatter: any }>()
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>{{ frontmatter.title }}</h1>
            <p class="text-lg">{{ frontmatter.description }}</p>
            <div class="text-lg opacity-50">
                <i18n-d v-if="frontmatter.date" :value="new Date(frontmatter.date)" format="long" />
                <span v-if="frontmatter.duration">· {{ frontmatter.duration }}</span>
            </div>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <article class="m-auto prose">
            <slot />
        </article>
    </Container>
</template>
