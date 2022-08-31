<script setup lang="ts">
defineProps<{
    name: string
    website: string
    twitter: string
    linkedin: string
    github: string
    bio: string
}>()
</script>

<template>
    <div>
        <div class="grid grid-cols-2">
            <p class="contents font-bold" :name="name">{{  name  }}</p>
            <div class="mt-2 flex flex-wrap gap-2 justify-end" text="lg">
                <IconButtonLink v-if="website" :url="website" target="_blank" class="contents">
                    <carbon:user-avatar-filled-alt />
                </IconButtonLink>
                <IconButtonLink v-if="twitter" :url="twitter" target="_blank" class="contents">
                    <carbon:logo-twitter />
                </IconButtonLink>
                <IconButtonLink v-if="linkedin" :url="linkedin" target="_blank" class="contents">
                    <carbon:logo-linkedin />
                </IconButtonLink>
                <IconButtonLink v-if="github" :url="github" target="_blank" class="contents">
                    <carbon:logo-github />
                </IconButtonLink>
            </div>
        </div>
        <div class="mb-8">{{  bio  }}</div>
    </div>
</template>