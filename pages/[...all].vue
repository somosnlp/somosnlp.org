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

const isBlogPath = computed(() => {
  return path.value.startsWith('blog/') || path.value.startsWith('en/blog/')
})

async function loadContent() {
  try {
    content.value = null
    const cleanPath = path.value.replace(/^en\//, '')
    
    if (isBlogPath.value && language.value === 'en') {
      try {
        const module = await import(`../pages/${cleanPath}.en.md`)
        content.value = module.default
      } catch {
        const module = await import(`../pages/${cleanPath}.md`)
        content.value = module.default
      }
    } else {
      const module = await import(`../pages/${cleanPath}.md`)
      content.value = module.default
    }
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
      <img src="https://somosnlp.github.io/assets/images/ilustraciones/undraw_not_found_60pq.svg" alt="Not found" />
      <div class="font-bold tracking-wide text-4xl">404</div>
      <div class="tracking-tight">{{ t('not-found') }} :(</div>
      <div class="tracking-tight">{{ t('not-found-cache') }}</div>
    </div>
  </Container>
  <Container v-else>
    <component :is="content" />
  </Container>
</template>
