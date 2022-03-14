<script setup lang="ts">
import { computed } from 'vue'
import type { RouteRecordNormalized } from 'vue-router'
import { useI18n } from "vue-i18n";

const props = defineProps<{
    route: RouteRecordNormalized
}>()

const { d } = useI18n();
const frontmatter = computed(() => (props.route.meta as any).frontmatter)
</script>

<template>
    <router-link :to="route.path" :key="route.path" class="contents">
        <div
            class="rounded-md grid p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2"
            hover="bg-gray-50 text-black dark:bg-gray-800 dark:text-white"
        >
            <div>
                <img
                    class="bg-white rounded-md object-cover max-h-200px"
                    dark="bg-gray-900"
                    :src="frontmatter.speaker_pic"
                    :alt="frontmatter.speaker"
                />
            </div>
            <div class="text-center grid gap-2">
                <div class="font-bold text-lg mb-1">{{ frontmatter.title }}</div>
                <div class="text-sm opacity-60">
                    <span v-if="frontmatter.date">{{ d(frontmatter.date, 'long') }}</span>
                    <span v-if="frontmatter.time">· {{ frontmatter.time }}</span>
                </div>
                <div class="text-sm font-bold mb-1">{{ frontmatter.speaker }}</div>
                <div class="text-sm mb-1">{{ frontmatter.speaker_bio }}</div>
            </div>
        </div>
    </router-link>
</template>
