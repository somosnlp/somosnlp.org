<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
    <nav class="flex gap-4 items-center justify-between select-none">
        <div class="flex gap-8 items-center">
            <Logo />
            <router-link to="/hackathon" class="whitespace-nowrap hover:text-accent-500 flex items-center gap-1.5">
                <span class="relative flex h-2.5 w-2.5">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-red-500"></span>
                </span>
                Hackathon
            </router-link>
            <router-link to="/recursos" class="whitespace-nowrap hover:text-accent-500">{{ t('navbar.resources') }}
            </router-link>
            <router-link to="/eventos" class="whitespace-nowrap hover:text-accent-500">{{ t('navbar.events') }}
            </router-link>
            <router-link to="/blog" class="whitespace-nowrap hover:text-accent-500">{{ t('navbar.blog') }}</router-link>
            <!-- <router-link to="/empleo" class="whitespace-nowrap hover:text-accent-500">{{ t('navbar.jobs') }}
            </router-link> -->
            <router-link to="/comunidad" class="whitespace-nowrap hover:text-accent-500">{{ t('navbar.team') }}
            </router-link>
        </div>
        <div class="flex gap-4 items-center">
            <div class="flex gap-2" text="lg">
                <SocialMediaButtons />
            </div>
            <DarkThemeToggle />
        </div>
    </nav>
</template>
