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
    </div>
  </Container>
</template>

<route lang="yaml">
meta:
  layout: default
</route>
