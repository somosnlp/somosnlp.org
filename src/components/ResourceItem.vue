<script setup lang="ts">
defineProps<{
    name: string
    tags: string[]
    dominio: string
    description: string
    website: string
    github: string
    paper: string
    hf_dataset_name: string
    hf_model_name: string
    hf_contributor_handle: string
}>()
</script>

<template>
    <div
        class="rounded-md grid p-4 gap-4 grid-cols-[auto,1fr,auto]"
        hover="bg-gray-50 dark:bg-gray-800"
    >
        <div class="grid gap-2">
            <div class="font-bold text-lg">{{ name }}</div>
            <div class="flex flex-wrap gap-3">
                <div
                    v-for="(tag, index) in tags"
                    :key="index"
                    class="border rounded bg-gray-50 border-gray-100 text-sm py-0.5 px-2 select-none dark:border-black dark:bg-gray-700"
                >{{ tag }}</div>
            </div>
        </div>
        <div class="grid gap-2">
            <div class="flex flex-wrap gap-2 justify-self-end items-center" text="lg">
                <IconButtonLink v-if="website" :url="website" class="contents">
                    <carbon:link />
                </IconButtonLink>
                <IconButtonLink v-if="paper" :url="paper" class="contents">
                    <carbon:document />
                </IconButtonLink>
                <IconButtonLink v-if="github" :url="github" class="contents">
                    <carbon:logo-github />
                </IconButtonLink>
                <IconButtonLink
                    v-if="hf_dataset_name"
                    :url="'https://huggingface.co/datasets/' + hf_dataset_name"
                    class="contents"
                >
                    <noto:hugging-face />
                </IconButtonLink>
                <IconButtonLink
                    v-if="hf_model_name"
                    :url="'https://huggingface.co/' + hf_contributor_handle + '/' + hf_model_name"
                    class="contents"
                >
                    <noto:hugging-face />
                </IconButtonLink>
            </div>
            <a
                v-if="hf_contributor_handle"
                :href="'https://hf.co/' + hf_contributor_handle"
                target="_blank"
                class="justify-self-end"
            >
                <div class="text-sm mb-1">@{{ hf_contributor_handle }}</div>
            </a>
        </div>
        <div class="col-span-2 text-sm mb-1">{{ description }}</div>
    </div>
</template>
