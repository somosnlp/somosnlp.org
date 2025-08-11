<script setup lang="ts">
interface Organizer {
  name: string
  university: string
  profileImage?: string
}

const organizers: Organizer[] = [
  {
    name: 'María Grandury',
    university: 'Universidad Politécnica de Madrid',
    profileImage: 'https://somosnlp.github.io/assets/images/comunidad/maria_grandury.png'
  },
  {
    name: 'Selene Báez',
    university: 'University of Zurich',
    profileImage: 'https://somosnlp.github.io/assets/images/comunidad/selene_baez.jpg'
  },
  {
    name: 'Diana Galván',
    university: 'University of Cambridge',
    profileImage: 'https://somosnlp.github.io/assets/images/comunidad/diana_galvan.png'
  },
  {
    name: 'Helena Gómez',
    university: 'Universidad Nacional Autónoma de México',
    profileImage: 'https://somosnlp.github.io/assets/images/comunidad/helena_gomez_adorno.jpg'
  },
  {
    name: 'Danae Sánchez',
    university: 'University of Copenhagen',
    profileImage: 'https://somosnlp.github.io/assets/images/comunidad/danae_sanchez.jpeg'
  }
]
</script>

<template>
  <div class="flex flex-wrap justify-center gap-6 md:gap-8 my-8">
    <div 
      v-for="organizer in organizers" 
      :key="organizer.name"
      class="flex flex-col items-center text-center w-32 md:w-40"
    >
    <div
  class="w-20 h-20 md:w-24 md:h-24 rounded-full overflow-hidden mb-3 shadow-md bg-gray-200 dark:bg-gray-700 bg-center bg-cover"
  :style="{ backgroundImage: `url(${organizer.profileImage})` }"
  @error="(event) => { /* fallback isn’t supported on divs—if you need one, you can swap in a <img> in JS instead */ }"
/>

      <div class="text-sm font-semibold mb-1 leading-tight">{{ organizer.name }}</div>
      <div class="text-xs text-gray-600 dark:text-gray-400 leading-tight px-1">{{ organizer.university }}</div>
    </div>
  </div>
</template> 