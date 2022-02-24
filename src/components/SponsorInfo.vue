<script setup lang="ts">
defineProps<{
    sponsor: string
    url: string
    logo: string
    logo_dark: string
}>()
</script>

<template>
    <a class="contents" :href="url" target="_blank" rel="noreferrer">
        <picture>
            <source :srcset="logo_dark" media="(prefers-color-scheme: dark)" />
            <img :src="logo" :alt="sponsor" class="w-screen" />
        </picture>
    </a>
</template>
