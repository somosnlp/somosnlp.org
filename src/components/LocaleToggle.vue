<script setup lang="ts">
import { useI18n } from 'vue-i18n'
const { locale } = useI18n()

const setSpanish = () => { locale.value = 'es' }
const setEnglish = () => { locale.value = 'en' }
</script>

<template>
    <!-- <div @click="setSpanish">Spanish</div> -->
    <div class="flex gap-2">
        <IconButton @click="setSpanish">
            <div class="flex font-medium text-sm gap-1 items-center">
                <twemoji:flag-for-flag-spain />
                <span>ES</span>
            </div>
        </IconButton>
        <IconButton @click="setEnglish">
            <div class="flex font-medium text-sm gap-1 items-center">
                <twemoji:flag-for-flag-united-kingdom />
                <span>EN</span>
            </div>
        </IconButton>
    </div>
    <!-- <div @click="setEnglish">English</div> -->
</template>
