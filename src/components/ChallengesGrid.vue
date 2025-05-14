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
        <div class="grid gap-4 <sm:grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
            <ChallengeItem v-for="challenge in challenges" :key="challenge.title" :challenge="challenge" />
        </div>
    </div>
</template> 