
<script setup lang="ts">
import { isDark } from "~/logic"
</script>
<template>
    <div class="flex text-gray-800 gap-2 items-center" dark="text-white">
        <carbon:moon class="cursor-pointer" @click="isDark = true" />
        <div @click="isDark = !isDark" class="rounded-full cursor-pointer bg-accent-300 h-6 w-12 relative"
            dark="bg-gray-800" border="1 accent-500 dark:gray-600">
            <span :style="`transform: translate(${Number(!isDark) * 24 - 1}px, -1px)`"
                class="bg-white border rounded-full h-6 transition-transform top-0 w-6 absolute"
                border="1 accent-600 dark:gray-600" />
        </div>
        <carbon:sun class="cursor-pointer" @click="isDark = false" />
    </div>
    <!-- Alternative DarkThemeToggle -->
    <!-- <IconButton @click="isDark = !isDark">
        <carbon:sun v-if="!isDark" class="cursor-pointer" />
        <carbon:moon v-else class="cursor-pointer" />
    </IconButton>-->
</template>
