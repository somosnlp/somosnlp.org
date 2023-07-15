<template>
    <Container class="my-12">
  
      <div class="search-container">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Buscar..."
          class="search-input"
        />
      </div>
  
      <div class="table-container">
        <table class="table border-solid border-1 rounded-3px">
          <thead >
            <tr>
              <th class="centered-header">Nombre</th>
              <th class="centered-header">Etiquetas</th>
              <th class="centered-header">Descripción</th>
              <th class="centered-header">Página Web</th>
              <th class="centered-header">GitHub</th>
              <th class="centered-header">Paper</th>
              <th class="centered-header">Dataset HF</th>
              <th class="centered-header">Usuario HF </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in filteredItems" :key="item.name">
              <td>
                <div class="name-cell mx-5">
                  <template v-if="item.name !== ''">
                    {{ item.name }}
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
              <td>
                <div class="tag-cell mx-5">
                    <template v-if="item.tags && item.tags.length > 0">
                    {{ item.tags.join(', ') }}
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
              <td style="text-align: justify;">
                <div class="desciption-cell mx-5">
                  <template v-if="item.description !== ''">
                    {{ item.description }}
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>              
              </td>
              <td style="text-align: center;">
                <div class="website-cell mx-5 centered-content">
                  <template v-if="item.website !== ''">
                    <IconButtonLink :url="item.website" style="display: block; width: 37px;">
                      <carbon:link />
                    </IconButtonLink>
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
              <td style="text-align: center;">
                <div class="github-cell mx-5 centered-content">
                  <template v-if="item.github !== ''">
                    <IconButtonLink :url="item.github" style="display: block; width: 37px;">
                      <carbon:logo-github />
                    </IconButtonLink>
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
              <td style="text-align: center;">
                <div class="paper-cell mx-5 centered-content">
                  <template v-if="item.paper !== ''">
                    <IconButtonLink :url="item.paper" style="display: block; width: 37px;">
                      <carbon:document />
                    </IconButtonLink>
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
              <td style="text-align: center;">
                <div class="HF Dataset Name-cell mx-5 centered-content">
                  <template v-if="item.hf_dataset_name !== ''">
                    <IconButtonLink :url="'https://huggingface.co/datasets/' + item.hf_dataset_name" style="display: block; width: 37px;">
                      <noto:hugging-face />
                    </IconButtonLink>
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
              <td style="text-align: center;">
                <div class="HF Contributor Handle mx-5 centered-content">
                  <template v-if="item.hf_contributor_handle !== ''">
                    <IconButtonLink :url="'https://huggingface.co/' + item.hf_contributor_handle" style="display: block; width: 37px;">
                      <noto:hugging-face />
                    </IconButtonLink>
                  </template>
                  <template v-else>
                    <span class="centered-cell">-</span>
                  </template>
                </div>
              </td>
            </tr>
            <tr v-if="filteredItems.length === 0">
              <td colspan="8" class="centered-cell"><b>No se han encontrado coincidencias</b></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p class="mx-auto mt-8 mb-12 prose">
        ¿Echas en falta alguna base de datos? Te animamos a <b>abir una PR</b> <a href="https://github.com/somosnlp/somosnlp.org/edit/main/pages/recursos/open-source/TableDatasets.md"><u><b>aquí</b></u></a> y contribuir a la lista 🚀
      </p>
    </Container>
  </template>

<script setup lang="ts">
import { ref, computed } from 'vue';

const searchQuery = ref('');

const props = defineProps({
  resourceItems: {
    type: Array,
    required: true
  }
});

const filteredItems = computed(() => {
  return props.resourceItems.filter(item =>
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.tags.some(tag => tag.toLowerCase().includes(searchQuery.value.toLowerCase()))
  );
});
</script>
 
<style>
.table-container {
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

.table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

th,
td {
  padding: 7px;
  border-bottom: 1px solid #ddd;
}

th.centered-header {
  text-align: center;
  background-color: #ffd21e;
  color: black;
}

.website-cell {
  margin: 0 20px;
}

.search-container {
  margin-bottom: 16px;
  text-align: center;
}

.search-input {
  padding: 8px;
  width: 300px;
  border: 1px solid #ddd;
  border-radius: 4px;
  color: #000;
}

.centered-cell {
  text-align: center;
  padding: 16px;
}

.centered-content {
    display: flex;
    justify-content: center;
  }
    
.desciption-cell {
  width: 300px !important;
  min-width: 300px !important;
  max-width: 300px !important;
}
</style>
