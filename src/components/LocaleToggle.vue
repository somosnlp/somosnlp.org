<script setup lang="ts">
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()
</script>

<template>
    <IconButton @click="locale = 'es'" class="flex gap-2 items-center">
        <twemoji:flag-for-flag-spain />
        <span class="font-medium text-sm">Español</span>
    </IconButton>
    <IconButton @click="locale = 'en'" class="flex gap-2 items-center">
        <twemoji:flag-for-flag-united-kingdom />
        <span class="font-medium text-sm">English</span>
    </IconButton>
</template>
