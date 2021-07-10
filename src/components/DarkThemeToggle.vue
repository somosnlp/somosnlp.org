
<script setup lang="ts">
import { isDark } from "~/logic"
</script>
<template>
    <div class="flex text-gray-800 gap-2 items-center" dark="text-white">
        <fluent-weather-sunny-24-regular class="cursor-pointer" @click="isDark = false" />
        <div
            @click="isDark = !isDark"
            :class="
                isDark ? 'border-accent-900' : ' border-accent-500'
            "
            class="border rounded-full cursor-pointer bg-accent-400 h-6 w-12 relative inline-flex items-start focus:outline-none"
        >
            <span
                :style="`transform: translate(${Number(isDark) * 24 - 1}px, -1px)`"
                class="bg-white border rounded-full h-6 transition-transform top-0 w-6 absolute"
                border="2 accent-600"
            ></span>
        </div>
        <fluent-weather-moon-24-regular class="cursor-pointer" @click="isDark = true" />
    </div>
</template>
