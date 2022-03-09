<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/core-team/')
    )
</script>

<template>
    <div class="auto-rows-fr grid gap-2 lg:grid-cols-3">
        <CoreTeamItem v-for="route in routes" :route="route" />
    </div>
</template>
