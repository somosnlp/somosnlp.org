<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const props = defineProps({
    data: Array,
    columns: Array,
    filterKey: String
})

const sortKey = ref('')
const sortOrders = ref(
    props.columns.reduce((o, key) => ((o[key] = 1), o), {})
)

const filteredData = computed(() => {
    let { data, filterKey } = props
    if (filterKey) {
        filterKey = filterKey.toLowerCase()
        data = data.filter((row) => {
            return Object.keys(row).some((key) => {
                return String(row[key]).toLowerCase().indexOf(filterKey) > -1
            })
        })
    }
    const key = sortKey.value
    if (key) {
        const order = sortOrders.value[key]
        data = data.slice().sort((a, b) => {
            a = a[key]
            b = b[key]
            return (a === b ? 0 : a > b ? 1 : -1) * order
        })
    }
    return data
})

function sortBy(key) {
    sortKey.value = key
    sortOrders.value[key] *= -1
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1)
}
</script>
    
<template>
    <table v-if="filteredData.length"
        class="text-md border-solid border-2 rounded-3px bg-accent-500 border-accent-500 dark: border-accent-500">
        <thead>
            <tr>
                <th v-for="key in columns" @click="sortBy(key)" :class="{ active: sortKey == key }"
                    class="py-20px cursor-pointer select-none bg-accent-500 text-accent-100 dark: bg-accent-500">
                    {{ capitalize(key) }}
                    <span class="arrow" :class="sortOrders[key] > 0 ? 'asc' : 'dsc'">
                    </span>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="entry in filteredData">
                <td v-for="key in columns" class="min-w-120px px-15px py-20px bg-accent-50 dark: bg-accent-400">
                    <a v-if="key === 'más'" :href="entry['más']" target="_blank">
                        <tabler:external-link class="inline align-middle mr-2 text-lg" />
                    </a>
                    <p v-else>{{ entry[key] }}</p>
                </td>
            </tr>
        </tbody>
    </table>
    <div v-else>
        <p>{{ t('jobs.not_found') }}</p>
        <p>{{ t('jobs.follow_us') }}</p>
    </div>
</template>
    
<style>
th.active {
    color: #fff;
}

th.active .arrow {
    opacity: 1;
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
    border-bottom: 4px solid #fff;
}

.arrow.dsc {
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #fff;
}
</style>
