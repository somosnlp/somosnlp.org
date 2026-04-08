<script setup lang="ts">
import { ref, computed } from 'vue';

const searchQuery = ref('');
const sortKey = ref('');
const sortOrder = ref(1);

const props = defineProps({
    resourceItems: {
        type: Array,
        required: true
    }
});

function sortBy(key: string) {
    if (sortKey.value === key) {
        sortOrder.value *= -1;
    } else {
        sortKey.value = key;
        sortOrder.value = 1;
    }
}

const filteredItems = computed(() => {
    let items = props.resourceItems.filter(item =>
        item.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        item.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        item.tags.some(tag => tag.toLowerCase().includes(searchQuery.value.toLowerCase()))
    );
    if (sortKey.value) {
        items = items.slice().sort((a, b) => {
            const aVal = String(a[sortKey.value] || '').toLowerCase();
            const bVal = String(b[sortKey.value] || '').toLowerCase();
            return (aVal === bVal ? 0 : aVal > bVal ? 1 : -1) * sortOrder.value;
        });
    }
    return items;
});
</script>

<template>
    <Container class="my-12">

        <div class="search-container">
            <input type="text" v-model="searchQuery" placeholder="Buscar..." class="search-input" />
        </div>

        <div class="table-container">
            <table class="table border-solid border-1 rounded-3px">
                <thead>
                    <tr>
                        <th class="centered-header sortable" @click="sortBy('name')" :class="{ active: sortKey === 'name' }">
                            Nombre <span class="arrow" :class="sortKey === 'name' ? (sortOrder > 0 ? 'asc' : 'dsc') : ''"></span>
                        </th>
                        <th class="centered-header">Tareas</th>
                        <th class="centered-header sortable" @click="sortBy('domain')" :class="{ active: sortKey === 'domain' }">
                            Dominio <span class="arrow" :class="sortKey === 'domain' ? (sortOrder > 0 ? 'asc' : 'dsc') : ''"></span>
                        </th>
                        <th class="centered-header sortable" @click="sortBy('languages')" :class="{ active: sortKey === 'languages' }">
                            Idiomas <span class="arrow" :class="sortKey === 'languages' ? (sortOrder > 0 ? 'asc' : 'dsc') : ''"></span>
                        </th>
                        <th class="centered-header sortable" @click="sortBy('countries')" :class="{ active: sortKey === 'countries' }">
                            Países <span class="arrow" :class="sortKey === 'countries' ? (sortOrder > 0 ? 'asc' : 'dsc') : ''"></span>
                        </th>
                        <th class="centered-header">Página Web</th>
                        <th class="centered-header">GitHub</th>
                        <th class="centered-header">Paper</th>
                        <th class="centered-header">Hugging Face Hub</th>
                        <th class="centered-header sortable" @click="sortBy('contributor')" :class="{ active: sortKey === 'contributor' }">
                            Gracias A <span class="arrow" :class="sortKey === 'contributor' ? (sortOrder > 0 ? 'asc' : 'dsc') : ''"></span>
                        </th>
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
                            <div class="tag-cell mx-5 flex flex-wrap gap-3">
                                <template v-if="item.tags && item.tags.length > 0">
                                    <span
                                        class="border rounded bg-gray-50 border-gray-100 text-sm py-0.5 px-2 select-none dark:border-black dark:bg-gray-700"
                                        v-for="tag in item.tags">{{ tag }}</span>
                                </template>
                                <template v-else>
                                    <span class="centered-cell">-</span>
                                </template>
                            </div>
                        </td>
                        <td style="text-align: justify;">
                            <div class="tag-cell mx-5">
                                <template v-if="item.domain !== ''">
                                    {{ item.domain }}
                                </template>
                                <template v-else>
                                    <span class="centered-cell">-</span>
                                </template>
                            </div>
                        </td>
                        <td style="text-align: justify;">
                            <div class="tag-cell mx-5">
                                <template v-if="item.languages !== ''">
                                    {{ item.languages }}
                                </template>
                                <template v-else>
                                    <span class="centered-cell">-</span>
                                </template>
                            </div>
                        </td>
                        <td style="text-align: justify;">
                            <div class="tag-cell mx-5">
                                <template v-if="item.countries !== ''">
                                    {{ item.countries }}
                                </template>
                                <template v-else>
                                    <span class="centered-cell">-</span>
                                </template>
                            </div>
                        </td>
                        <td style="text-align: center;">
                            <div class="website-cell mx-5 centered-content">
                                <template v-if="item.página_web !== ''">
                                    <IconButtonLink :url="item.página_web" style="display: block; width: 37px;">
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
                                    <IconButtonLink :url="'https://huggingface.co/datasets/' + item.hf_dataset_name"
                                        style="display: block; width: 37px;">
                                        <noto:hugging-face />
                                    </IconButtonLink>
                                </template>
                                <template v-else>
                                    <span class="centered-cell">-</span>
                                </template>
                            </div>
                        </td>
                        <td style="text-align: center;">
                            <div class="name-cell mx-5">
                                <template v-if="item.contributor !== ''">
                                    {{ item.contributor }}
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
            ¡Ayúdanos a recolectar bases de datos de todas las variedades del español!
            Te animamos a <b>abir una PR</b> <a
                href="https://github.com/somosnlp/somosnlp.org/edit/main/pages/recursos/open-source/datasets.md"
                target='_blank'><u><b>aquí</b></u></a> y contribuir a la lista 🚀
        </p>
    </Container>
</template>
 
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

.sortable {
    cursor: pointer;
    user-select: none;
}

.sortable:hover {
    opacity: 0.85;
}

th.active {
    font-weight: bold;
}

.arrow {
    display: inline-block;
    vertical-align: middle;
    width: 0;
    height: 0;
    margin-left: 5px;
    opacity: 0.66;
}

.arrow.asc {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-bottom: 4px solid #000;
}

.arrow.dsc {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #000;
}
</style>
