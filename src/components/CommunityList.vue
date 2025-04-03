<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const founder_routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/maria-grandury')
            || i.path.startsWith('/comunidad/manuel-romero')
            || i.path.startsWith('/comunidad/flor-plaza')

    )
const routes = router.getRoutes()
    .filter(
        i => i.path.startsWith('/comunidad/')
            && !i.path.startsWith('/comunidad/maria-grandury')
            && !i.path.startsWith('/comunidad/manuel-romero')
            && !i.path.startsWith('/comunidad/flor-plaza')
            && !i.path.startsWith('/comunidad/0-plantilla')
            && (i.meta as any).frontmatter.community
            && !(i.meta as any).frontmatter.community.includes('Ponente')
    )
    .sort(
        (a, b) =>
            ((a.meta as any).frontmatter.community.localeCompare((b.meta as any).frontmatter.community)) ||
            a.path.toLowerCase().localeCompare(b.path.toLowerCase())
    )
</script>

<template>

    <div class="flex flex-col justify-center m-auto text-center prose ">
        <h2>Equipo</h2>
        <br />
    </div>
    <div class="auto-rows-fr mx-12 grid gap-6 lg:mx-36 lg:grid-cols-3">
        <ProfileItemRouter v-for="route in founder_routes" :route="route" />
    </div>

    <br />
    <div class="flex flex-col justify-center m-auto text-center prose ">

        <hr class="mx-auto mt-8 mb-12 prose" />
        <h2>Comunidad</h2>

        <p class="text-lg">
            La fuerza de SomosNLP reside en la comunidad de +2000 personas comprometidas con el PLN abierto que la
            forman.
            Aquí te
            presentamos a las que colaboran o han colaborado más activamente con
            <a class="contents" href="http://somosnlp.org/nuestra-mision" target="_blank">nuestra misión</a>,
            <a class="contents" href="https://discord.com/invite/my8w7JUxZR" target="_blank">¡únete!</a>
        </p>
        <p class="text-sm">
            <span class="italic">Lista en continua evolución... </span>⏳
        </p>
    </div>
    <br />
    <div class="auto-rows-fr mx-12 grid gap-6 lg:grid-cols-3">
        <ProfileItemRouter v-for="route in routes" :route="route" />
    </div>
</template>
