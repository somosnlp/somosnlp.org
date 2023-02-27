<!--
    Person profile that gets the information needed as parameters. If you want to pass it as a route use ProfileItemParams, the component template is the same.
-->

<script setup lang="ts">
defineProps<{
    name: string
    title: string
    cover: string
    website: string
    twitter: string
    linkedin: string
    github: string
    bio: string
}>()
</script>

<template>
    <div class="rounded-md grid p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2"
        hover="bg-gray-50 dark:bg-gray-800">
        <div>
            <img class="bg-white rounded-md object-cover max-h-200px" dark="bg-gray-900" width="180" height="180"
                :src="cover ? cover : 'images/logo.svg'" :alt="name" />
        </div>
        <div class="text-center grid gap-2">
            <div class="font-bold text-lg mb-1">{{ name }}</div>
            <div class="text-sm mb-1">{{ title }}</div>
            <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
                <IconButtonLink v-if="website" :url="website" class="contents">
                    <carbon:user-avatar-filled-alt />
                </IconButtonLink>
                <IconButtonLink v-if="twitter" :url="twitter" class="contents">
                    <carbon:logo-twitter />
                </IconButtonLink>
                <IconButtonLink v-if="linkedin" :url="linkedin" class="contents">
                    <carbon:logo-linkedin />
                </IconButtonLink>
                <IconButtonLink v-if="github" :url="github" class="contents">
                    <carbon:logo-github />
                </IconButtonLink>
            </div>
        </div>
    </div>
</template>
