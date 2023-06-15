<!--
    Person profile that gets the info from the route to an .md file.
    If you want to pass it params use ProfileItemProps.
-->

<script setup lang="ts">
import { computed } from 'vue'
import type { RouteRecordNormalized } from 'vue-router'

const props = defineProps<{
    route: RouteRecordNormalized
}>()

const frontmatter = computed(() => (props.route.meta as any).frontmatter)
</script>

<template>
    <router-link :to="route.path" :key="route.path" target="_blank" class="contents">
        <div class="rounded-md grid p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2"
            hover="bg-gray-50 dark:bg-gray-800">
            <div>
                <img class="bg-white rounded-md object-cover max-h-200px" dark="bg-gray-900" width="180" height="180"
                    :src="frontmatter.cover ? frontmatter.cover : 'images/logo.svg'" :alt="frontmatter.title" />
            </div>
            <div class="text-center grid gap-2">
                <div class="font-bold text-lg mb-1">{{ frontmatter.title }}</div>
                <div class="text-sm mb-1">{{ frontmatter.description }}</div>

                <!--
                The social buttons are already shown in each profile page.

                    <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
                    <IconButtonLink v-if="frontmatter.website" :url="frontmatter.website" class="contents">
                        <carbon:user-avatar-filled-alt />
                    </IconButtonLink>
                    <IconButtonLink v-if="frontmatter.twitter" :url="frontmatter.twitter" class="contents">
                        <carbon:logo-twitter />
                    </IconButtonLink>
                    <IconButtonLink v-if="frontmatter.linkedin" :url="frontmatter.linkedin" class="contents">
                        <carbon:logo-linkedin />
                    </IconButtonLink>
                    <IconButtonLink v-if="frontmatter.github" :url="frontmatter.github" class="contents">
                        <carbon:logo-github />
                    </IconButtonLink>
                    </div> 
                -->
            </div>
        </div>
    </router-link>
</template>
