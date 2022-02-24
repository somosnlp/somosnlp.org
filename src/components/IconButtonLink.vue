<script setup lang="ts">
defineProps<{
    url: string
}>()
</script>

<template>
    <a class="contents" :href="url" target="_blank" rel="noreferrer">
        <IconButton>
            <slot></slot>
        </IconButton>
    </a>
</template>
