<script setup lang="ts">
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()
</script>

<template>
    <div class="flex gap-2">
        <IconButton @click="locale = 'es'">
            <div class="flex font-medium text-sm gap-1 items-center">
                <twemoji:flag-for-flag-spain />
                <span>ES</span>
            </div>
        </IconButton>
        <IconButton @click="locale = 'en'">
            <div class="flex font-medium text-sm gap-1 items-center">
                <twemoji:flag-for-flag-united-kingdom />
                <span>EN</span>
            </div>
        </IconButton>
    </div>
</template>
