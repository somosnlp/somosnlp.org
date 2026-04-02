<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const routes = router.getRoutes()
    .filter(i => i.path.startsWith('/conferencias/') && (i.meta as any).frontmatter?.title)
</script>

<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Conferencias</h1>
            <p>Encuentros presenciales, "Birds-of-a-Feather" y eventos sociales, ¡te esperamos!</p>
        </header>

        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="auto-rows-fr grid gap-2 lg:grid-cols-2">
            <router-link v-for="route in routes" :key="route.path" :to="route.path" class="contents">
                <div class="rounded-md grid p-4 gap-4 place-items-center <sm:grid-cols-1 <lg:grid-cols-2"
                    hover="bg-gray-50 dark:bg-gray-800">
                    <div>
                        <img class="bg-white rounded-md object-cover max-h-200px" dark="bg-gray-900"
                            :src="(route.meta as any).frontmatter?.cover || '/images/logo.svg'"
                            :alt="(route.meta as any).frontmatter?.title" />
                    </div>
                    <div class="text-center grid gap-2">
                        <div class="font-bold text-lg mb-1">{{ (route.meta as any).frontmatter?.title }}</div>
                        <div class="text-sm mx-10 mb-1">{{ (route.meta as any).frontmatter?.description }}</div>
                    </div>
                </div>
            </router-link>
        </div>
    </Container>
</template>
