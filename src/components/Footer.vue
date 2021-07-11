<template>
  <nav class="my-6 grid lg:grid-cols-3 gap-6 place-items-center">
    <Logo class="col-span-full lg:justify-self-start" />
    <div class="text-sm lg:justify-self-start">© 2021 nlp-en-es.org All rights reserved.</div>
    <div class="flex gap-2 items-center justify-self-center">
      <SocialMediaButtons />
    </div>
    <div class="flex gap-4 items-center lg:justify-self-end">
      <LocaleToggle />
      <DarkThemeToggle />
    </div>
  </nav>
</template>
