<template>
  <nav class="my-6 grid gap-6 place-items-center lg:grid-cols-3">
    <Logo class="col-span-full lg:justify-self-start" />
    <div
      class="text-sm lg:justify-self-start"
    >© {{ (new Date()).getFullYear() }} nlp-en-es.org All rights reserved.</div>
    <div class="flex flex-wrap gap-2 items-center justify-self-center" text="lg">
      <SocialMediaButtons />
    </div>
    <div class="flex gap-4 items-center <md:(flex-wrap justify-center) lg:justify-self-end">
      <LocaleToggle />
      <DarkThemeToggle />
    </div>
  </nav>
</template>
