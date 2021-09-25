<script setup lang="ts">
defineProps<{
    description: string
    video: string
    slides: string
    name: string
    twitter: string
    linkedin: string
    github: string
}>()
</script>

<template>
    <p class="contents" :description="description">{{ description }}</p>

    <div class="contents">
        <iframe
            class="mx-auto my-8"
            width="560"
            height="315"
            :src="video"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media;
            gyroscope; picture-in-picture"
            allowfullscreen
        ></iframe>
    </div>

    <div class="grid grid-cols-2">
        <div>
            <p class="contents" :name="name">Imparte: {{ name }}</p>

            <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
                <LinkIconButton :url="twitter" class="contents">
                    <carbon:logo-twitter />
                </LinkIconButton>
                <LinkIconButton :url="linkedin" class="contents">
                    <carbon:logo-linkedin />
                </LinkIconButton>
                <LinkIconButton :url="github" class="contents">
                    <carbon:logo-github />
                </LinkIconButton>
            </div>
        </div>
        <div class="flex justify-end">
            <a class="contents" :href="slides" target="_blank" rel="noreferrer">Diapositivas</a>
        </div>
    </div>
</template>