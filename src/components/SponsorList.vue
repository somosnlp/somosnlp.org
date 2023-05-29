<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/patrocinios/')
            && !i.path.startsWith('/patrocinios/0-plantilla')
    )
    .sort((a, b) => {
        return a.path.localeCompare(b.path);
    });
</script>

<template>
    <div class="auto-rows-fr grid gap-x-16 place-items-center lg:grid-cols-3">
        <SponsorInfoRouter v-for="route in routes" :route="route" />
    </div>
</template>
