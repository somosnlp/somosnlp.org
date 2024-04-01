<!--
    Sponsor profile that gets the info from the route to an .md file.
    If you want to pass it as params use SponsorInfo.
-->

<script setup lang="ts">
import { computed } from 'vue'
import type { RouteRecordNormalized } from 'vue-router'
import { isDark } from '~/logic'

const props = defineProps<{
    route: RouteRecordNormalized
}>()

const frontmatter = computed(() => (props.route.meta as any).frontmatter)
const imgSrc = computed(() => isDark.value ? frontmatter.value.cover_dark || frontmatter.value.cover: frontmatter.value.cover || 'images/logo.svg' )
</script>

<template>
    <router-link :to="route.path" :key="route.path" target="_blank" class="contents">
        <div class="rounded-md grid p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2"
            hover="bg-gray-50 dark:bg-gray-800">
            <div>
                <img class="bg-white rounded-md object-cover max-h-200px" 
                    dark="bg-dark-900" width="180" height="180"
                    :src="imgSrc"
                    :alt="frontmatter.title" 
                />
            </div>
        </div>
    </router-link>
</template>
                
