<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <Container>
    <div class="my-16 grid gap-10 justify-items-center">
      <h1 class="flex flex-col text-center gap-1 items-center">
        <span
          class="font-semibold text-lg tracking-wider text-accent-500 uppercase"
          dark="text-accent-400"
        >{{ t('landing-page.introducing') }}</span>
        <span class="font-bold tracking-tight text-2xl">{{ t('landing-page.heading') }}</span>
      </h1>
      <img alt="NLP en ES logo" src="https://nlp-en-es.github.io/assets/logo.svg" />
      <h2 class="text-center max-w-65ch">{{ t('landing-page.heading-2') }}</h2>
      <div class="flex gap-4">
        <router-link to="/blog/hola-mundo">
          <div
            class="rounded-lg cursor-pointer bg-accent-300 shadow py-3 px-6 text-accent-900 gap-2"
            border="1 accent-400 dark:accent-500"
            hover="shadow-md dark:ring"
          >
            {{ t('landing-page.read-the-announcement') }}
            <fluent:document-bullet-list-24-regular class="inline" />
          </div>
        </router-link>
        <!-- <div
          class="rounded-lg cursor-pointer shadow py-3 px-6 hover:shadow-lg"
          border="1 gray-200 dark:gray-700 "
        >Another Button</div>-->
      </div>
    </div>
  </Container>
</template>