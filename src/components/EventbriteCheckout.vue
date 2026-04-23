<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from 'vue'

const props = withDefaults(defineProps<{
  eventId: string
  height?: number
  fallbackUrl?: string
}>(), {
  height: 500,
})

const containerId = `eventbrite-widget-container-${props.eventId}`
const widgetReady = ref(false)
const loadError = ref(false)
const EB_SCRIPT_SRC = 'https://www.eventbrite.com/static/widgets/eb_widgets.js'

function loadScript(): Promise<void> {
  return new Promise((resolve, reject) => {
    if (typeof window === 'undefined') return resolve()
    if ((window as any).EBWidgets) return resolve()
    const existing = document.querySelector<HTMLScriptElement>(`script[src="${EB_SCRIPT_SRC}"]`)
    if (existing) {
      existing.addEventListener('load', () => resolve())
      existing.addEventListener('error', () => reject(new Error('Eventbrite script failed to load')))
      return
    }
    const script = document.createElement('script')
    script.src = EB_SCRIPT_SRC
    script.async = true
    script.onload = () => resolve()
    script.onerror = () => reject(new Error('Eventbrite script failed to load'))
    document.body.appendChild(script)
  })
}

onMounted(async () => {
  try {
    await loadScript()
    const EB = (window as any).EBWidgets
    if (!EB) throw new Error('EBWidgets unavailable')
    EB.createWidget({
      widgetType: 'checkout',
      eventId: props.eventId,
      iframeContainerId: containerId,
      iframeContainerHeight: props.height,
    })
    widgetReady.value = true
  } catch (err) {
    console.error('[EventbriteCheckout]', err)
    loadError.value = true
  }
})

onBeforeUnmount(() => {
  const container = document.getElementById(containerId)
  if (container) container.innerHTML = ''
})
</script>

<template>
  <div class="my-8">
    <div
      :id="containerId"
      class="eventbrite-checkout"
      :style="{ minHeight: `${height}px` }"
    />
    <p v-if="loadError" class="text-center text-sm mt-2">
      No se pudo cargar el checkout.
      <a
        :href="fallbackUrl || `https://www.eventbrite.com/e/${eventId}`"
        target="_blank"
        rel="noopener noreferrer"
      >Abrir en Eventbrite</a>
    </p>
    <p v-else class="text-center text-sm mt-2 opacity-75">
      <a
        :href="fallbackUrl || `https://www.eventbrite.com/e/${eventId}`"
        target="_blank"
        rel="noopener noreferrer"
      >Abrir en Eventbrite</a>
    </p>
  </div>
</template>

<style scoped>
.eventbrite-checkout {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
}
</style>
