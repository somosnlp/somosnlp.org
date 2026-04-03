<script setup lang="ts">
import { ref } from 'vue'

const TAGS = ['comunidad', 'charlas', 'recursos', 'hackathon', 'conferencias']
const selectedTag = ref<string | null>(null)

function toggleTag(tag: string) {
    selectedTag.value = selectedTag.value === tag ? null : tag
}
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Blog #NLP</h1>
            <p>Colección de anuncios, proyectos, recursos y eventos relevantes para la comunidad. ¿Te gustaría compartir
                algo?
                <a class="text-md" target="_blank"
                    href="https://github.com/somosnlp/somosnlp.org/blob/main/CONTRIBUTING.md">
                    ¡Publica en el blog!
                </a>
            </p>
        </header>

        <hr class="mx-auto mt-8 mb-8 prose" />

        <div class="flex flex-wrap gap-2 justify-center mb-8">
            <button v-for="tag in TAGS" :key="tag" @click="toggleTag(tag)"
                class="px-4 py-1 rounded-full text-sm border transition-colors" :class="selectedTag === tag
                    ? 'bg-yellow-400 border-yellow-400 text-white font-semibold'
                    : 'border-gray-300 dark:border-gray-600 hover:border-yellow-400 dark:hover:border-yellow-400'">#{{
        tag }}</button>
        </div>

        <BlogList :tag="selectedTag ?? undefined" />

        <hr class="mx-auto mt-8 mb-12 prose" />
        <footer class="m-auto text-center prose">
            <p>¿Te gustaría compartir algo con la comunidad?</p>
            <a class="text-md" target="_blank"
                href="https://github.com/somosnlp/somosnlp.org/blob/main/CONTRIBUTING.md#-publicar-un-art%C3%ADculo-en-el-blog">
                Publica en nuestro blog
            </a>
        </footer>
    </Container>
</template>
