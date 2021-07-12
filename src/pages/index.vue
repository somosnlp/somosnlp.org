<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <Container>
    <div class="my-16 grid gap-16 justify-items-center">
      <h1 class="flex flex-col text-center gap-1 items-center">
        <span
          class="font-semibold text-lg tracking-wider text-accent-500 uppercase"
          dark="text-accent-400"
        >{{ t('landing-page.introducing') }}</span>
        <span class="font-bold text-xl tracking-tight text-3xl">{{ t('landing-page.heading') }}</span>
      </h1>
      <img alt="NLP en ES logo" src="../assets/logo.svg" />
      <div class="flex gap-4">
        <div
          class="rounded-lg cursor-pointer bg-accent-300 shadow py-3 px-6 text-accent-900 hover:shadow-lg"
          border="1 accent-400 dark:2 dark:accent-500"
        >{{ t('landing-page.read-the-announcement') }}</div>
        <div
          class="rounded-lg cursor-pointer shadow py-3 px-6 hover:shadow-lg"
          border="1 gray-200 dark:gray-700 dark:2"
        >Another Button</div>
      </div>
    </div>
  </Container>
</template>
