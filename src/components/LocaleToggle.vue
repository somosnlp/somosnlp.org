<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
const { locale } = useI18n()
const router = useRouter()

const switchToSpanish = () => {
    locale.value = 'es'
    router.push(router.currentRoute.value.path.replace('/en', ''))
}

const switchToEnglish = () => {
    locale.value = 'en'
    router.push(`/en${router.currentRoute.value.path}`)
}
</script>

<template>
    <IconButton @click="switchToSpanish" class="flex gap-2 items-center">
        <twemoji:flag-for-flag-spain />
        <span class="font-medium text-sm">Español</span>
    </IconButton>
    <IconButton @click="switchToEnglish" class="flex gap-2 items-center">
        <twemoji:flag-for-flag-united-kingdom />
        <span class="font-medium text-sm">English</span>
    </IconButton>
</template>
