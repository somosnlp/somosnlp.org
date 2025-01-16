import { ref, Ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

type Language = 'es' | 'en'
const currentLanguage: Ref<Language> = ref('es')

export function useLanguage() {
    const router = useRouter()
    const route = useRoute()
    const { locale } = useI18n()

    const setLanguage = async (lang: Language): Promise<void> => {
        if (currentLanguage.value === lang) return

        currentLanguage.value = lang
        locale.value = lang

        // Only modify URL for blog pages
        if (route.path.includes('/blog/')) {
            const cleanPath = route.path.replace(/^\/?(en\/)?/, '')
            const newPath = lang === 'es' ? `/${cleanPath}` : `/en/${cleanPath}`

            if (newPath !== route.path) {
                await router.replace(newPath)
            }
        }
    }

    // Initialize language state
    if (route.path.startsWith('/en/') && route.path.includes('/blog/')) {
        currentLanguage.value = 'en'
        locale.value = 'en'
    } else {
        currentLanguage.value = locale.value as Language
    }

    return {
        language: currentLanguage,
        setLanguage,
    }
} 