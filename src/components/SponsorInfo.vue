<script setup lang="ts">
import { isDark } from "~/logic"

defineProps<{
    sponsor: string
    url: string
    logo: string
    logo_dark: string
}>()
</script>

<template>
    <a :href="url" target="_blank">
        <img v-if="!isDark" class="w-screen" :src="logo" :alt="sponsor" />
        <img v-if="isDark" class="w-screen" :src="logo_dark" :alt="sponsor" />
    </a>
</template>
