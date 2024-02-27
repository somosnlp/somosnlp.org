<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const founder_routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/maria-grandury')
    )
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/')
            && !i.path.startsWith('/comunidad/maria-grandury')
            && !i.path.startsWith('/comunidad/0-plantilla')
            && (i.meta as any).frontmatter.community
            && (i.meta as any).frontmatter.community !== 'Ponente'
    )
    .sort(
        (a, b) =>
            ((a.meta as any).frontmatter.community.localeCompare((b.meta as any).frontmatter.community)) ||
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    )
</script>

<template>
    <div class="auto-rows-fr mx-12 grid gap-6 lg:mx-36 lg:grid-cols-2">
        <ProfileItemRouter v-for="route in founder_routes" :route="route" />
        <div class="flex flex-col justify-center m-auto text-center prose ">
            <p class="text-lg">
                La fuerza de la comunidad reside en las +1500 personas apasionadas por el PLN que la forman. Aquí te
                presentamos a las que colaboran o han colaborado más activamente con
                <a class="contents" href="http://somosnlp.org/nuestra-mision" target="_blank">nuestra misión</a>,
                <a class="contents" href="https://discord.com/invite/my8w7JUxZR" target="_blank">¡únete!</a>
            </p>
            <p class="text-sm">
                <span class="italic">Lista en continua evolución... </span>⏳
            </p>
        </div>
    </div>
    <div class="auto-rows-fr mx-12 grid gap-6 lg:grid-cols-3">
        <ProfileItemRouter v-for="route in routes" :route="route" />
    </div>
</template>
