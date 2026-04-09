<script setup lang="ts">
defineProps<{
    icon: string
    title: string
    description: string
    linkText?: string
    linkUrl?: string
    variant?: 'default' | 'highlight'
}>()
</script>

<template>
    <div class="rounded-lg p-6 transition-all duration-200 text-center"
        :class="variant === 'highlight'
            ? 'bg-blue-900 text-white hover:bg-blue-800 dark:hover:bg-blue-950'
            : 'border border-gray-200 dark:border-gray-700 hover:shadow-lg hover:border-yellow-400 dark:hover:border-yellow-400'"
    >
        <div class="text-4xl mb-3">{{ icon }}</div>
        <h3 class="font-bold text-lg mb-2">{{ title }}</h3>
        <p class="text-sm mb-4" :class="variant === 'highlight' ? 'opacity-90' : 'text-gray-600 dark:text-gray-400'">
            {{ description }}
        </p>
        <a v-if="linkUrl" :href="linkUrl" target="_blank"
            class="inline-block px-4 py-2 rounded text-sm font-semibold transition-colors no-underline"
            :class="variant === 'highlight'
                ? 'bg-yellow-400 text-gray-900 hover:bg-yellow-300'
                : 'bg-yellow-400 text-white hover:bg-yellow-500'"
        >
            {{ linkText || 'Saber más' }}
        </a>
    </div>
</template>
