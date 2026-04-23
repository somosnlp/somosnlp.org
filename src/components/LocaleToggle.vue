<script setup lang="ts">
import { useLanguage } from '~/composables/useLanguage'
import { usePageTranslations } from '~/composables/usePageTranslations'

const { language, setLanguage } = useLanguage()
const { hasPageTranslation } = usePageTranslations()
</script>

<template>
    <div class="flex gap-2">
        <IconButton
            @click="setLanguage('es')"
            class="flex gap-2 items-center"
            :class="{ 'opacity-50': language !== 'es' }"
        >
            <twemoji:flag-for-flag-spain />
            <span class="font-medium text-sm">ES</span>
        </IconButton>
        <IconButton
            @click="setLanguage('en')"
            class="flex gap-2 items-center"
            :class="{ 'opacity-50': language !== 'en' }"
            :title="hasPageTranslation('en') ? '' : 'UI only'"
        >
            <twemoji:flag-for-flag-united-kingdom />
            <span class="font-medium text-sm">EN</span>
        </IconButton>
        <IconButton
            @click="setLanguage('pt')"
            class="flex gap-2 items-center"
            :class="{ 'opacity-50': language !== 'pt' }"
            :title="hasPageTranslation('pt') ? '' : 'UI only'"
        >
            <twemoji:flag-for-flag-brazil />
            <span class="font-medium text-sm">PT</span>
        </IconButton>
    </div>
</template>
