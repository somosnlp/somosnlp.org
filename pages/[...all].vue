<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useLanguage } from '~/composables/useLanguage'
import { computed, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'

const route = useRoute()
const { language } = useLanguage()
const { t } = useI18n()

const content = ref(null)
const path = computed(() => {
  const segments = route.params.all as string[]
  return segments ? segments.join('/') : ''
})

/**
 * Attempts to load a markdown page, trying locale-specific variants first.
 * Lookup order for locale 'en' and path 'blog/post':
 *   1. blog/post.en.md  (co-located translation)
 *   2. en/blog/post.md  (legacy directory-based translation)
 *   3. blog/post.md     (fallback to default locale)
 */
async function loadContent() {
  try {
    content.value = null
    const lang = language.value
    const cleanPath = path.value.replace(/^(en|pt)\//, '')

    if (lang !== 'es') {
      // Try co-located locale file first: blog/post.en.md
      try {
        const module = await import(`../pages/${cleanPath}.${lang}.md`)
        content.value = module.default
        return
      } catch {}

      // Try legacy directory-based file: en/blog/post.md
      try {
        const module = await import(`../pages/${lang}/${cleanPath}.md`)
        content.value = module.default
        return
      } catch {}
    }

    // Fallback to default locale file
    const module = await import(`../pages/${cleanPath}.md`)
    content.value = module.default
  } catch (e) {
    console.error('Failed to load content:', e)
    content.value = null
  }
}

watch([() => route.path, language], loadContent, { immediate: true })
</script>

<template>
  <Container v-if="!content">
    <div class="mx-auto my-16 text-center max-w-600px grid text-2xl gap-4 place-items-center">
      <img src="/images/ilustraciones/undraw_not_found_60pq.svg" alt="Not found" />
      <div class="font-bold tracking-wide text-4xl">404</div>
      <div class="tracking-tight">{{ t('not-found') }} :(</div>
      <div class="tracking-tight">{{ t('not-found-cache') }}</div>
    </div>
  </Container>
  <Container v-else>
    <component :is="content" />
  </Container>
</template>
