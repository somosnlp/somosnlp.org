<template>
  <nav class="my-6 grid gap-2">
    <Logo />
    <div class="grid lg:grid-cols-3 gap-6 items-center">
      <div class="text-sm">© 2021 nlp-en-es.org All rights reserved.</div>
      <div class="flex gap-2 items-center lg:justify-self-center">
        <SocialMediaButtons />
      </div>
      <div class="flex items-center lg:justify-self-end gap-4">
        <LocaleToggle />
        <DarkThemeToggle />
      </div>
    </div>
  </nav>
</template>
