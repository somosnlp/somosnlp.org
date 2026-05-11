<script setup lang="ts">
import ChallengeItem from './ChallengeItem.vue'

interface Challenge {
    title: string
    description: string
    dates: string
    points: string
    requirements: string
    link: string
    cover?: string
}

defineProps<{
    challenges: Challenge[]
}>()
</script>

<template>
    <div class="full-width-container ">
        <div class="flex flex-wrap justify-center gap-4 max-w-1200px mx-auto">
            <div
                v-for="challenge in challenges"
                :key="challenge.title"
                class="flex w-full sm:w-[calc((100%-1rem)/2)] lg:w-[calc((100%-2rem)/3)]"
            >
                <ChallengeItem :challenge="challenge" />
            </div>
        </div>
    </div>
</template> 