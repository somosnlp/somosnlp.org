<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const showBanner = ref(true);
const showUpcomingEvent = ref(false);
const showPastEvents = ref(true);
</script>

<template>
  <Container v-show="showBanner" class="bg-accent-50 -top-1px text-accent-900 relative"
    border="b-1 t-1 accent-100 dark:accent-600" dark="bg-accent-400 text-accent-900">
    <div @click="showBanner = false"
      class="flex flex-wrap font-semibold text-sm text-center gap-2 items-center justify-center">
      <a href="hackathon" target="_blank" hover="text-accent-700">
        {{ t('landing-page.banner') }}
      </a>
      <carbon:close class="cursor-pointer text-lg ml-2" hover="text-accent-700" />
    </div>
  </Container>
  <Container class="bg-gray-white dark:bg-dark-900">
    <div class="mx-auto my-8 text-center lg:max-w-1/2">
      <div class="flex flex-col mb-6 gap-1">
        <p class="font-medium text-xl tracking-wider text-accent-500 uppercase" dark="text-accent-400">{{
    t('landing-page.introducing')
  }}</p>
        <h1 class="font-medium tracking-tighter text-3xl">{{ t('landing-page.heading') }}</h1>
      </div>
      <img class="mx-auto my-8" alt="SomosNLP logo" width="320" length="320"
        src="https://somosnlp.github.io/assets/logo.svg" />
      <p text="lg">{{ t('landing-page.heading-2') }}</p>
      <div class="mt-10 grid gap-4 lg:grid-cols-2">
        <a href="https://discord.com/invite/my8w7JUxZR" target="_blank" class="button-accent">
          <carbon:user-multiple />
          {{ t('landing-page.join-us') }}
        </a>
        <router-link to="/nuestra-mision" class="button-gray">
          <carbon:bullhorn />
          {{ t('landing-page.read-the-announcement') }}
        </router-link>
      </div>
    </div>
  </Container>
  <Container v-if="showUpcomingEvent" class="bg-gray-50 dark:bg-dark-700">
    <div class="mx-auto my-8 text-center lg:max-w-1/2">
      <h1 class="flex flex-col mb-6 gap-1">
        <span class="font-medium text-xl tracking-wider text-accent-500 uppercase" dark="text-accent-400">{{
    t('landing-page.events.upcoming-events')
  }}</span>
      </h1>
      <img class="mx-auto my-8" alt="Próximos eventos"
        src="https://somosnlp.github.io/assets/images/eventos/240301_hackathon.jpg" />
      <p class="my-8">{{ t('landing-page.events.event-description') }}</p>
      <a target="_blank" class="button-accent max-w-100 mx-auto" href="https://somosnlp.org/hackathon">
        {{ t('landing-page.events.join-event') }}
      </a>
    </div>
  </Container>
  <Container class="bg-gray-white dark:bg-dark-900">
    <div grid="~ lg:cols-2" class="my-16 place-items-center">
      <div class="px-4">
        <h2 class="font-medium text-center mb-8 tracking-tight text-3xl">{{ t('landing-page.why.heading') }}*</h2>
        <p>{{ t('landing-page.why.text') }}</p>
        <div class="my-8 grid gap-y-8 gap-x-6 grid-cols-[auto,1fr] items-center">

          <div class="rounded-md p-2 text-accent-900" bg="accent-100 dark:accent-300"
            border="2 accent-200 dark:accent-600">
            <carbon:earth text="lg" />
          </div>
          <div>
            {{ t('landing-page.why.community') }}
            <a href="https://discord.com/invite/my8w7JUxZR" target="_blank">
              <span text="xs accent-900" class="rounded-md font-medium bg-accent-100 ml-1 p-1 uppercase"
                border="2 accent-300">{{ t('landing-page.join-us') }}</span>
            </a>
          </div>

          <div class="rounded-md p-2 text-accent-900" bg="accent-100 dark:accent-300"
            border="2 accent-200 dark:accent-600">
            <carbon:education text="lg" />
          </div>
          <div>
            {{ t('landing-page.why.education') }}
            <a href="https://www.youtube.com/c/somosnlp?sub_confirmation=1" target="_blank">
              <span text="xs accent-900" class="rounded-md font-medium bg-accent-100 ml-1 p-1 uppercase"
                border="2 accent-300">{{ t('landing-page.learn-with-us') }}</span>
            </a>
          </div>

          <div class="rounded-md p-2 text-accent-900" bg="accent-100 dark:accent-300"
            border="2 accent-200 dark:accent-600">
            <carbon:share-knowledge text="lg" />
          </div>
          <div>
            {{ t('landing-page.why.jobs') }}
            <a href="empleo" target="_blank">
              <span text="xs accent-900" class="rounded-md font-medium bg-accent-100 ml-1 p-1 uppercase"
                border="2 accent-300">{{ t('landing-page.why.job-board') }}</span>
            </a>
          </div>
        </div>
        <br />
        <br />
        <a href="https://cvc.cervantes.es/lengua/anuario/anuario_23/informes_ic/p01.htm" target="_blank">
          <p class="italic text-sm">
            * "El español en cifras", El español en el mundo, Anuario del Instituto Cervantes 2024
          </p>
        </a>
      </div>
      <img src="https://somosnlp.github.io/assets/images/ilustraciones/undraw_Traveling_re_weve.svg"
        alt="Comunidad internacional" />
    </div>
  </Container>
  <Container v-if="showPastEvents" class="bg-gray-50 dark:bg-dark-700">
    <div class="mx-auto my-8 text-center lg:max-w-2/3">
      <h1 class="flex flex-col mb-6 gap-1">
        <span class="font-medium text-xl tracking-wider text-accent-500 uppercase" dark="text-accent-400">{{
    t('landing-page.events.recorded-events')
  }}</span>
      </h1>
      <div class="grid grid-cols-3 gap-8 my-12">

        <!-- HACKATHON 2024 -->
        <a href="/hackathon/ia_y_lms_retos_y_oportunidades" target="_blank">
          <img alt="Charla de Elena González-Blanco" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/240307_elena_gonzalez_blanco.png" />
        </a>
        <a href="/hackathon/crear_datasets_de_calidad_con_argilla_y_distilabel" target="_blank">
          <img alt="Charla de Gabriel Martín" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/240311_gabriel_martin_blazquez.jpg" />
        </a>
        <a href="/hackathon/empatia_y_emociones_en_ia" target="_blank">
          <img alt="Charla de Amanda Curry" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/240326_amanda_curry.jpg" />
        </a>

        <!-- HACKATHON 2023 -->
        <a href="/hackathon-2023/fine-tuning-llms" target="_blank">
          <img alt="Fine-tuning de grandes modelos de lenguaje" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/230320_fine_tuning_llms.jpg" />
        </a>
        <a href="/hackathon-2023/deteccion-del-lenguaje-ofensivo" target="_blank">
          <img alt="Detección del lenguaje ofensivo" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/230404_deteccion_del_lenguaje_ofensivo.jpg" />
        </a>
        <a href="/hackathon-2023/evaluacion-con-desacuerdo" target="_blank">
          <img alt="Evaluación con desacuerdo" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/230404_evaluacion_con_desacuerdo.jpg" />
        </a>

        <!-- EQUIPOS HACKATHON 2022 -->
        <a href="https://www.youtube.com/watch?v=ZTYAsEHUhPs&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M" target="_blank">
          <img alt="Evento 01" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/221208_modelo_juridico_mexicano.jpg" />
        </a>
        <a href="https://www.youtube.com/watch?v=XOaQKNauySo&list=PLTA-KAy8nxaAbyaBTYK68TZKQLv9V8L8M" target="_blank">
          <img alt="Evento 02" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/eventos/221213_neutralizacion_de_genero.jpg" />
        </a>
        <a href="https://www.youtube.com/watch?v=3OhArr1R2Lw&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">
          <img alt="Evento 03" width="650" height="365" src="https://somosnlp.github.io/assets/images/evento_iic.png" />
        </a>

        <!-- HACKATHON 2022 -->
        <a href="https://www.youtube.com/watch?v=GX4l3WhOy4o&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">
          <img alt="Evento 04" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/evento_cristina.png" />
        </a>
        <a href="https://www.youtube.com/watch?v=UQwWTykNFW0&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">
          <img alt="Evento 05" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/evento_paulo.png" />
        </a>
        <a href="https://www.youtube.com/watch?v=aNR7UM-E6vA&list=PLTA-KAy8nxaAbVZ2lVcycHnJ2qEDip7hG" target="_blank">
          <img alt="Evento 06" width="650" height="365"
            src="https://somosnlp.github.io/assets/images/evento_ximena.png" />
        </a>
      </div>
      <router-link to="/eventos" class="button-accent max-w-100 mx-auto">
        <Carbon:logoYoutube text="xl" />
        {{ t('landing-page.events.all-events') }}
      </router-link>
    </div>
  </Container>
  <Container class="bg-gray-white dark:bg-dark-900">
    <div class="my-16">
      <h2 class="font-medium text-center mb-6 tracking-wider text-4xl">{{ t('landing-page.contribute.heading') }}</h2>
      <p class="mx-auto text-lg text-center max-w-65ch opacity-75">{{ t('landing-page.contribute.text') }}</p>
      <div class="grid gap-16 place-items-center lg:grid-cols-2 my-8">
        <img class="p-8" src="https://somosnlp.github.io/assets/images/ilustraciones/undraw_content_team_3epn.svg"
          alt="Proyectos open-source" />
        <div class="grid gap-6 justify-center md:grid-cols-2">
          <a href="https://discord.com/invite/my8w7JUxZR" target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)">
            <carbon:logo-discord text="xl" />
            <span text="center">{{ t('landing-page.contribute.discord') }}</span>
          </a>
          <a href="https://forms.gle/YpUvifDNLG6E56Cy9" target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)">
            <carbon:microphone-filled text="xl" />
            <span text="center">{{ t('landing-page.contribute.speaker') }}</span>
          </a>
          <a href="https://github.com/somosnlp/somosnlp.org#-contribuye-al-blog" target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)">
            <carbon:document text="xl" />
            <span text="center">{{ t('landing-page.contribute.blog') }}</span>
          </a>
          <a href="https://github.com/somosnlp" target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)">
            <carbon:logo-github text="xl" />
            <span text="center">{{ t('landing-page.contribute.github') }}</span>
          </a>
          <a href="https://twitter.com/somosnlp_" target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)">
            <carbon:logo-twitter text="xl" />
            <span text="center">{{ t('landing-page.contribute.twitter') }}</span>
          </a>
          <a href="https://www.linkedin.com/company/somosnlp" target="_blank"
            class="md:flex-col rounded-md flex p-6 gap-4 items-center hover:(bg-gray-50 dark:bg-gray-800)">
            <carbon:logo-linkedin text="xl" />
            <span text="center">{{ t('landing-page.contribute.linkedin') }}</span>
          </a>
          <router-link to="/nuestra-mision" class="col-span-full button-accent max-w-100 mx-auto">
            <carbon:binoculars />
            {{ t('landing-page.contribute.button') }}
          </router-link>
        </div>
      </div>
    </div>
  </Container>
</template>
