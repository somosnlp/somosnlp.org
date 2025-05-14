<script setup lang="ts">
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
    challenge: Challenge
}>()
</script>

<template>
    <a :href="challenge.link" target="_blank" class="contents">
        <div class="rounded-md grid my-4 p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2 bg-blue-900 text-white"
            hover="bg-blue-800 dark:bg-gray-800">
            <!-- <div v-if="challenge.cover">
                <img class="bg-white rounded-md object-cover max-h-200px" dark="bg-gray-900"
                    :src="challenge.cover" />
            </div> -->
            <div class="text-center grid gap-2">
                <div class="font-bold text-lg mb-1">{{ challenge.title }}</div>
                <div class="text-sm mx-10 mb-1">{{ challenge.description }}</div>
                <div class="text-xs opacity-75">
                    <div>{{ challenge.dates }}</div>
                    <div>Puntos máximos: {{ challenge.points }}</div>
                    <div>Requisitos: {{ challenge.requirements }}</div>
                </div>
            </div>
        </div>
    </a>
</template> 