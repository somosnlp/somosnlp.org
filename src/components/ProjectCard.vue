<script setup lang="ts">
defineProps<{
    year: string
    prize: string
    title: string
    description?: string
    variant?: 'default' | 'highlight'
    wide?: boolean
}>()
</script>

<template>
    <div class="border border-l-4 bg-gray-50 dark:bg-gray-800 rounded-r-lg rounded-l-sm p-5 transition-all duration-200 border-gray-200 dark:border-gray-700 hover:shadow-lg hover:border-yellow-400 dark:hover:border-yellow-400"
        :class="[
            variant === 'highlight' ? 'border-l-accent-500' : 'border-l-blue-500',
            wide ? 'md:col-span-2' : '',
        ]"
    >
        <div class="flex items-center gap-2 mb-2">
            <span class="text-xs font-bold text-white px-2 py-0.5 rounded"
                :class="variant === 'highlight' ? 'bg-accent-500' : 'bg-blue-500'"
            >{{ year }}</span>
            <span class="text-xs text-gray-500">{{ prize }}</span>
        </div>
        <h4 class="font-bold text-base mb-1">{{ title }}</h4>
        <p class="text-sm text-gray-600 dark:text-gray-400">
            <slot>{{ description }}</slot>
        </p>
    </div>
</template>
