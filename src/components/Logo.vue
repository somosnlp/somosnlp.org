<script setup lang="ts">
import { localePath } from '~/composables/useLanguage'
</script>

<template>
    <router-link :to="localePath('/')">
        <div class="flex gap-4 items-center">
            <LogoMark />
            <div class="font-semibold text-xl whitespace-nowrap">SomosNLP</div>
        </div>
    </router-link>
</template>
