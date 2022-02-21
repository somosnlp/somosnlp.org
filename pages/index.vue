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
    border="b-1 t-1 accent-100 dark:accent-600"
    dark="bg-accent-400 text-accent-900"
  >
    <div
      @click="showBanner = false"
      class="flex flex-wrap font-semibold text-sm text-center gap-2 items-center justify-center"
    >
      <router-link to="/hackathon" hover="text-accent-700">{{ t('landing-page.banner') }}</router-link>
      <carbon:close class="cursor-pointer text-lg ml-2" hover="text-accent-700" />
    </div>
  </Container>
  <Container>
    <!-- <div grid="~ md:cols-2 gap-8" class="place-items-center md:my-32">
    <img alt="Somos NLP logo" src="https://somosnlp.github.io/assets/logo.svg" />-->
    <div class="mx-auto my-8 text-center lg:max-w-1/2">
      <h1 class="flex flex-col mb-6 gap-1">
        <span
          class="font-medium text-xl tracking-wider text-accent-500 uppercase"
          dark="text-accent-400"
        >{{ t('landing-page.introducing') }}</span>
        <span class="font-medium tracking-tighter text-3xl">{{ t('landing-page.heading') }}</span>
      </h1>
      <img
        class="mx-auto my-8"
        alt="Somos NLP logo"
        src="https://somosnlp.github.io/assets/logo.svg"
      />
      <p text="lg">{{ t('landing-page.heading-2') }}</p>
      <div class="mt-10 grid gap-4 lg:grid-cols-2">
        <a href="https://discord.gg/u2wWMHsc" target="_blank" class="button-accent">
          <carbon:user-multiple />
          {{ t('landing-page.join-us') }}
        </a>
        <router-link to="/blog/hola-mundo" class="button-gray">
          <carbon:bullhorn />
          {{ t('landing-page.read-the-announcement') }}
        </router-link>
      </div>
    </div>
    <!-- </div> -->
  </Container>
  <Container class="bg-gray-50 dark:bg-dark-700">
    <div grid="~ lg:cols-2" class="my-16 place-items-center">
      <div class="px-4">
        <h2
          class="font-medium text-center mb-8 tracking-tight text-3xl"
        >{{ t('landing-page.why.heading') }}</h2>
        <p>{{ t('landing-page.why.text') }}</p>
        <div class="my-8 grid gap-y-8 gap-x-6 grid-cols-[auto,1fr] items-center">
          <div
            class="rounded-md p-2 text-accent-900"
            bg="accent-100 dark:accent-300"
            border="2 accent-200 dark:accent-600"
          >
            <carbon:earth text="lg" />
          </div>
          {{ t('landing-page.why.community') }}
          <div
            class="rounded-md p-2 text-accent-900"
            bg="accent-100 dark:accent-300"
            border="2 accent-200 dark:accent-600"
          >
            <carbon:education text="lg" />
          </div>
          {{ t('landing-page.why.education') }}
          <div
            class="rounded-md p-2 text-accent-900"
            bg="accent-100 dark:accent-300"
            border="2 accent-200 dark:accent-600"
          >
            <carbon:share-knowledge text="lg" />
          </div>
          <div>
            {{ t('landing-page.why.jobs') }}
            <span
              text="xs accent-900"
              class="rounded-md font-medium bg-accent-100 ml-1 p-1 uppercase"
              border="2 accent-300"
            >{{ t('landing-page.why.coming-soon') }}</span>
          </div>
        </div>
      </div>
      <img
        src="https://somosnlp.github.io/assets/images/undraw_Traveling_re_weve.svg"
        alt="Comunidad internacional"
      />
    </div>
  </Container>
  <Container class="bg-gray-white dark:bg-dark-900">
    <div class="my-16">
      <h2
        class="font-medium text-center mb-6 tracking-wider text-4xl"
      >{{ t('landing-page.contribute.heading') }}</h2>
      <p
        class="mx-auto text-lg text-center max-w-65ch opacity-75"
      >{{ t('landing-page.contribute.text') }}</p>
      <div class="grid gap-16 place-items-center lg:grid-cols-2 my-8">
        <img
          class="p-8"
          src="https://somosnlp.github.io/assets/images/undraw_content_team_3epn.svg"
          alt="Proyectos open-source"
        />
        <div class="grid gap-6 justify-center md:grid-cols-2">
          <a
            href="https://discord.gg/u2wWMHsc"
            target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)"
          >
            <carbon:logo-discord text="xl" />
            <span text="center">{{ t('landing-page.contribute.discord') }}</span>
          </a>
          <a
            href="https://github.com/somosnlp"
            target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)"
          >
            <carbon:logo-github text="xl" />
            <span text="center">{{ t('landing-page.contribute.github') }}</span>
          </a>
          <a
            href="https://twitter.com/somosnlp_"
            target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)"
          >
            <carbon:logo-twitter text="xl" />
            <span text="center">{{ t('landing-page.contribute.twitter') }}</span>
          </a>
          <a
            href="https://www.linkedin.com/company/somosnlp"
            target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)"
          >
            <carbon:logo-linkedin text="xl" />
            <span text="center">{{ t('landing-page.contribute.linkedin') }}</span>
          </a>
          <router-link to="/blog/como-contribuir" class="col-span-full button-accent">
            <carbon:binoculars />
            {{ t('landing-page.contribute.button') }}
          </router-link>
        </div>
      </div>
    </div>
  </Container>
</template>
