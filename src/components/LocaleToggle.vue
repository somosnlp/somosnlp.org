<script setup lang="ts">
import { useLanguage } from '~/composables/useLanguage'

const { language, setLanguage } = useLanguage()
</script>

<template>
    <div class="flex gap-2">
        <IconButton 
            @click="setLanguage('es')" 
            class="flex gap-2 items-center"
            :class="{ 'opacity-50': language !== 'es' }"
        >
            <twemoji:flag-for-flag-spain />
            <span class="font-medium text-sm">Español</span>
        </IconButton>
        <IconButton 
            @click="setLanguage('en')" 
            class="flex gap-2 items-center"
            :class="{ 'opacity-50': language !== 'en' }"
        >
            <twemoji:flag-for-flag-united-kingdom />
            <span class="font-medium text-sm">English</span>
        </IconButton>
    </div>
</template>
