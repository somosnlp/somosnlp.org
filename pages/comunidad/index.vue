<script setup lang="ts">
import { useHead } from '@vueuse/head'
useHead({
    meta: [
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: '@somosnlp_' },
        { name: 'twitter:creator', content: '@somosnlp_' },
        { name: 'twitter:title', content: 'Comunidad SomosNLP' },
        { name: 'twitter:description', content: 'Únete a nuestra comunidad internacional de personas apasionadas por el PLN' },
        { name: 'twitter:image', content: 'https://somosnlp.github.io/assets/logo.png' },
        { name: 'twitter:image:alt', content: 'Logo de la comunidad SomosNLP' }
    ]
})
</script>

<template>
    <Container class="mx-36 my-12">
        <header class="m-auto text-center prose">
            <h1>Comunidad</h1>
            <p class="text-lg">
                Somos una comunidad internacional en la que todas las personas interesadas en el PLN son bienvenidas,
                ¡únete! 🚀
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="flex justify-center">
            <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">
                <img src="https://somosnlp.github.io/assets/images/blog/ya_somos_1500.gif" alt="Ya Somos 1500"
                    width="500" height="289.71" />
            </a>
        </div>

        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <CommunityList />
            <div class="mx-auto mt-8 prose grid gap-4 lg:grid-cols-2">
                <a href="https://discord.com/invite/my8w7JUxZR" target="_blank" class="button-accent">
                    <carbon:user-multiple />
                    Únete a Discord
                </a>
                <router-link to="/nuestra-mision" target="_blank" class="button-gray">
                    <carbon:bullhorn />
                    Quiero contribuir
                </router-link>
            </div>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <div class="m-auto justify-center m-auto text-center prose ">
                <h2>Ponentes</h2>
                <p class="text-lg">
                    ¡Gracias a todas las personas que habéis compartido vuestra experiencia con la comunidad mediante
                    mentorías
                    y ponencias!
                </p>
            </div>
            <br />
            <SpeakerList />
            <div class="mx-auto mt-8 prose grid gap-4 lg:grid-cols-2">
                <router-link to="/eventos" target="_blank" class="button-accent">
                    <carbon:logoYoutube />
                    Todos los eventos
                </router-link>
                <a href="https://forms.gle/YpUvifDNLG6E56Cy9" target="_blank" class="button-gray">
                    <carbon:bullhorn />
                    Quiero ser ponente
                </a>
            </div>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <div class="m-auto text-center prose">
                <h2>Colaboraciones</h2>
                <p class="text-lg">
                    ¡Gracias también a todas las universidades, centros de investigación y empresas que nos habéis
                    apoyado en nuestro camino!
                </p>
            </div>
            <br />
            <SponsorList />
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-lg">
                ¿Te gustaría formar parte del equipo?
                ¿Dar una charla?
                ¿Lanzar un proyecto?
                ¿Patrocinar un evento?...
                ¿Te gustaría apoyarnos en <a class="contents" href="http://somosnlp.org/nuestra-mision"
                    target="_blank">nuestra misión</a>?
                <br /><br />
                Contáctanos por
                <a class="contents" href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a>
                o manda un email a info@somosnlp.org
                <br /><br />
                ¡Estamos impacientes por conocerte! 🚀
            </p>
        </div>
    </Container>
</template>
