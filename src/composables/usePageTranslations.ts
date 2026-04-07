import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { LOCALES, DEFAULT_LOCALE, type Language } from './useLanguage'

/**
 * Returns translation availability info for the current page.
 * Uses route metadata (basePath, locale) set by vite-plugin-pages extendRoute.
 *
 * Two translation mechanisms coexist:
 * 1. YAML locale files (locales/*.yml) → UI strings via t() — always available
 * 2. Co-located page files (page.en.md) → full page translations — detected here
 */
export function usePageTranslations() {
  const router = useRouter()
  const route = useRoute()

  const pageLocales = computed<Language[]>(() => {
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

  /**
   * Check if a co-located page translation exists for the given locale.
   */
  function hasPageTranslation(lang: Language): boolean {
    return pageLocales.value.includes(lang)
  }

  return {
    pageLocales,
    currentLocale,
    hasPageTranslation,
  }
}
