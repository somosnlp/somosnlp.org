<script setup lang="ts">
defineProps<{
    description: string
    poster: string
    video: string
    slides: string
    name: string
    website: string
    twitter: string
    linkedin: string
    github: string
    bio: string
}>()
</script>

<template>
    <p class="contents" :description="description">{{ description }}</p>

    <div v-if="poster" class="flex justify-center">
        <img alt="Cartel Evento" :src="poster" />
    </div>

    <div v-if="video" class="contents">
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
            <p class="contents" :name="name">Ponente: {{ name }}</p>

            <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
                <IconButtonLink :url="website" target="_blank" class="contents">
                    <carbon:user-avatar-filled-alt />
                </IconButtonLink>
                <IconButtonLink :url="twitter" target="_blank" class="contents">
                    <carbon:logo-twitter />
                </IconButtonLink>
                <IconButtonLink :url="linkedin" target="_blank" class="contents">
                    <carbon:logo-linkedin />
                </IconButtonLink>
                <IconButtonLink :url="github" target="_blank" class="contents">
                    <carbon:logo-github />
                </IconButtonLink>
            </div>
        </div>
        <div v-if="slides" class="flex justify-end">
            <a class="contents" :href="slides" target="_blank" rel="noreferrer">Diapositivas</a>
        </div>
    </div>
    <div class="my-8">{{ bio }}</div>
</template>