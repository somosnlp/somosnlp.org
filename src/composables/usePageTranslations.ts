import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { LOCALES, DEFAULT_LOCALE, type Language } from './useLanguage'

/**
 * Returns the list of available locales for the current page.
 * Uses route metadata (basePath, locale) set by vite-plugin-pages extendRoute
 * to find all locale variants of the current page.
 */
export function usePageTranslations() {
  const router = useRouter()
  const route = useRoute()

  const availableLocales = computed<Language[]>(() => {
    const basePath = route.meta.basePath as string | undefined
    if (!basePath) return [DEFAULT_LOCALE]

    const allRoutes = router.getRoutes()

    return LOCALES.filter((locale) => {
      const targetPath = locale === DEFAULT_LOCALE
        ? basePath
        : `/${locale}${basePath === '/' ? '' : basePath}`
      return allRoutes.some(r => r.path === targetPath && r.meta?.locale === locale)
    })
  })

  const currentLocale = computed<Language>(() => {
    return (route.meta.locale as Language) || DEFAULT_LOCALE
  })

  return {
    availableLocales,
    currentLocale,
  }
}
