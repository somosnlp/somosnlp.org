<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const showBanner = ref(true);
</script>

<template>
  <Container
    v-show="showBanner"
    class="bg-accent-50 -top-1px text-accent-900 relative"
    border="b t accent-200 dark:accent-600"
    dark="bg-accent-400 text-accent-900"
  >
    <div
      @click="showBanner = false"
      class="flex flex-wrap font-semibold text-sm text-center gap-2 items-center justify-center"
    >
      <router-link
        to="/blog/nlp-de-cero-a-cien"
        hover="text-accent-700"
      >{{ t('landing-page.banner') }}</router-link>
      <carbon:close class="cursor-pointer text-lg ml-2" hover="text-accent-700" />
    </div>
  </Container>
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
