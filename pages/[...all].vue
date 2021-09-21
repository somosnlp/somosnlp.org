<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <Container>
    <div class="mx-auto my-16 text-center max-w-600px grid text-2xl gap-4 place-items-center">
      <img src="https://nlp-en-es.github.io/assets/images/undraw_not_found_60pq.svg" alt="Not found" />
      <div class="font-bold tracking-wide text-4xl">404</div>
      <div class="tracking-tight">{{ t('not-found') }} :(</div>
    </div>
  </Container>
</template>
