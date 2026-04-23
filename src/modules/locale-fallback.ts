import { UserModule } from '~/types'

const NON_DEFAULT_LOCALES = ['en', 'pt']

export const install: UserModule = ({ router }) => {
  router.beforeEach((to) => {
    const match = to.path.match(/^\/(en|pt)(?:\/(.*))?$/)
    if (!match) return

    const [, locale, rest] = match
    if (!NON_DEFAULT_LOCALES.includes(locale)) return

    const hasRealRoute = router.getRoutes().some(
      r => r.path === to.path && r.meta?.locale === locale
    )

    if (!hasRealRoute) {
      const fallbackPath = rest ? `/${rest}` : '/'
      return fallbackPath
    }
  })
}
