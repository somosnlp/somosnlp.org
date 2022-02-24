<template>
  <nav class="my-6 grid gap-6 place-items-center lg:grid-cols-3">
    <Logo class="col-span-full lg:justify-self-start" />

    <div class="text-sm text-center lg:text-left lg:justify-self-start grid grid-rows-2 gap-2">
      © {{ (new Date()).getFullYear() }} SomosNLP.org All Rights Reserved
      <div>
        <router-link to="/aviso-legal" class="whitespace-nowrap hover:text-accent-500">{{ "Aviso Legal | " }}
        </router-link>
        <router-link to="/politica-privacidad" class="whitespace-nowrap hover:text-accent-500">
          {{ "Política de Privacidad" }}
        </router-link>
      </div>
    </div>

    <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
      <SocialMediaButtons />
    </div>

    <div class="flex gap-4 items-center <md:(flex-wrap justify-center) lg:justify-self-end">
      <LocaleToggle />
      <DarkThemeToggle />
    </div>

  </nav>
</template>
