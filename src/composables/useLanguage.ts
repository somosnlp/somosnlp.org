import { ref, Ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'

export type Language = 'es' | 'en' | 'pt'

export const LOCALES: Language[] = ['es', 'en', 'pt']
export const DEFAULT_LOCALE: Language = 'es'

const currentLanguage: Ref<Language> = ref(DEFAULT_LOCALE)

/**
 * Strips the locale prefix from a path to get the base path.
 * /en/blog/post → /blog/post
 * /pt/hackathon → /hackathon
 * /blog/post → /blog/post
 */
function getBasePath(routePath: string): string {
  for (const loc of LOCALES) {
    if (loc === DEFAULT_LOCALE) continue
    if (routePath.startsWith(`/${loc}/`)) return routePath.slice(loc.length + 1)
    if (routePath === `/${loc}`) return '/'
  }
  return routePath
}

/**
 * Builds the localized path for a given base path and target locale.
 */
function buildLocalizedPath(basePath: string, lang: Language): string {
  if (lang === DEFAULT_LOCALE) return basePath
  return `/${lang}${basePath === '/' ? '' : basePath}`
}

/**
 * Returns the localized path for a given base path using the current language.
 * Useful in templates: :to="localePath('/hackathon')"
 */
export function localePath(path: string): string {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`
  return buildLocalizedPath(normalizedPath, currentLanguage.value)
}

export function useLanguage() {
  const router = useRouter()
  const route = useRoute()
  const { locale } = useI18n()

  const setLanguage = async (lang: Language): Promise<void> => {
    if (currentLanguage.value === lang) return

    currentLanguage.value = lang
    locale.value = lang

    // Compute target path from current route's basePath (set by vite-plugin-pages)
    const basePath = (route.meta.basePath as string) || getBasePath(route.path)
    const targetPath = buildLocalizedPath(basePath, lang)

    if (targetPath !== route.path) {
      // Check if a real route exists for the target (not just the catch-all)
      const resolved = router.resolve(targetPath)
      const isCatchAll = resolved.matched.some(m => m.path === '/:all(.*)')

      if (!isCatchAll) {
        await router.push(targetPath)
      }
    }
  }

  // Initialize language from current route
  const detectedLocale = (route.meta.locale as Language) || (() => {
    for (const loc of LOCALES) {
      if (loc !== DEFAULT_LOCALE && route.path.startsWith(`/${loc}/`)) return loc
      if (loc !== DEFAULT_LOCALE && route.path === `/${loc}`) return loc
    }
    return DEFAULT_LOCALE
  })()

  currentLanguage.value = detectedLocale
  locale.value = detectedLocale

  return {
    language: currentLanguage,
    setLanguage,
    getBasePath,
    buildLocalizedPath,
  }
}
