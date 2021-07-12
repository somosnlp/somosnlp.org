<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>

<template>
  <Container>
    <div class="my-64 grid text-2xl gap-4 place-items-center">
      <div class="font-bold tracking-wide text-4xl">404</div>
      <div class="tracking-tight">{{ t('not-found') }} :(</div>
    </div>
  </Container>
</template>
