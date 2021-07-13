<script setup lang="ts">
import { computed } from 'vue'
import type { RouteRecordNormalized } from 'vue-router'

const props = defineProps<{
    route: RouteRecordNormalized
}>()

const frontmatter = computed(() => (props.route.meta as any).frontmatter)
</script>

<template>
    <router-link :to="route.path" :key="route.path" class="contents">
        <div
            class="rounded-md grid p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2"
            hover="bg-gray-50 dark:bg-gray-800"
        >
            <div>
                <img
                    class="bg-white rounded-md object-cover max-h-200px"
                    dark="bg-gray-900"
                    :src="frontmatter.cover ? frontmatter.cover : 'images/logo.svg'"
                />
            </div>
            <div class="text-center grid gap-2">
                <div class="font-bold text-lg mb-1">{{ frontmatter.title }}</div>
                <div class="text-sm opacity-60">
                    <i18n-d
                        v-if="frontmatter.date"
                        :value="new Date(frontmatter.date)"
                        format="long"
                    />
                    <span v-if="frontmatter.duration">· {{ frontmatter.duration }}</span>
                </div>
                <div class="text-sm mb-1">{{ frontmatter.description }}</div>
            </div>
        </div>
    </router-link>
</template>
