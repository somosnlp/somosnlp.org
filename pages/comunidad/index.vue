<script setup lang="ts">
import { useHead } from '@vueuse/head'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

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
            <h1>{{ t('community.title') }}</h1>
            <p class="text-lg">
                {{ t('community.subtitle') }}
            </p>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="flex justify-center">
            <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">
                <img src="https://somosnlp.github.io/assets/images/blog/ya_somos_2000.gif" alt="¡Ya Somos 2000!"
                    width="500" height="289.71" />
            </a>
        </div>

        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <CommunityList />
            <div class="mx-auto mt-8 prose grid gap-4 lg:grid-cols-2">
                <a href="https://discord.com/invite/my8w7JUxZR" target="_blank" class="button-accent">
                    <carbon:user-multiple />
                    {{ t('community.join_discord') }}
                </a>
                <router-link to="/nuestra-mision" target="_blank" class="button-gray">
                    <carbon:bullhorn />
                    {{ t('community.contribute') }}
                </router-link>
            </div>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <div class="m-auto justify-center m-auto text-center prose ">
                <h2>{{ t('community.speakers.title') }}</h2>
                <p class="text-lg">
                    {{ t('community.speakers.subtitle') }}
                </p>
            </div>
            <br />
            <SpeakerList />
            <div class="mx-auto mt-8 prose grid gap-4 lg:grid-cols-2">
                <router-link to="/eventos" target="_blank" class="button-accent">
                    <carbon:logoYoutube />
                    {{ t('community.speakers.all_events') }}
                </router-link>
                <a href="https://forms.gle/YpUvifDNLG6E56Cy9" target="_blank" class="button-gray">
                    <carbon:bullhorn />
                    {{ t('community.speakers.become_speaker') }}
                </a>
            </div>
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <div class="m-auto text-center prose">
                <h2>{{ t('community.collaborations.title') }}</h2>
                <p class="text-lg">
                    {{ t('community.collaborations.subtitle') }}
                </p>
            </div>
            <br />
            <SponsorList />
        </div>
        <hr class="mx-auto mt-8 mb-12 prose" />
        <div>
            <p class="m-auto text-center prose text-lg">
                {{ t('community.contact.questions') }}
                <a class="contents" href="http://somosnlp.org/nuestra-mision" target="_blank">{{ t('community.contact.mission') }}</a>
                <br /><br />
                {{ t('community.contact.contact_us') }}
                <a class="contents" href="https://discord.com/invite/my8w7JUxZR" target="_blank">Discord</a>
                {{ t('community.contact.or_email') }} info@somosnlp.org
                <br /><br />
                {{ t('community.contact.closing') }}
            </p>
        </div>
    </Container>
</template>
