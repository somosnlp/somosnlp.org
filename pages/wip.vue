<script setup lang="ts">
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>

<template>
      <Container>
            <div class="mx-auto my-16 text-center max-w-400px grid gap-4 place-items-center">
                  <img src="https://somosnlp.github.io/assets/images/undraw_good_team_re_j1kc.svg"
                        alt="Work In Progress..." />
                  <div class="font-bold tracking-wide text-4xl">404</div>
                  <div class="tracking-tight text-lg">{{ t('wip') }}</div>
            </div>
      </Container>
</template>
