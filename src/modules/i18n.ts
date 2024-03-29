import { createI18n } from 'vue-i18n'
import { UserModule } from '~/types'

// import i18n resources
// https://vitejs.dev/guide/features.html#glob-import
const messages = Object.fromEntries(
  Object.entries(
    import.meta.globEager('../../locales/*.y(a)?ml'))
    .map(([key, value]) => {
      const yaml = key.endsWith('.yaml')
      return [key.slice(14, yaml ? -5 : -4), value.default]
    }),
)

export const install: UserModule = ({ app }) => {
  const i18n = createI18n({
    legacy: false,
    locale: 'es',
    fallbackLocale: 'en',
    messages,
    datetimeFormats: {
      'en': {
        long: {
          weekday: "long", year: 'numeric', month: 'long', day: 'numeric',
        },
        short: {
          year: 'numeric', month: 'short', day: 'numeric'
        },
      },
      'es': {
        long: {
          weekday: "long", year: 'numeric', month: 'long', day: 'numeric',
        },
        short: {
          year: 'numeric', month: 'short', day: 'numeric'
        },
      }
    },
  })

  app.use(i18n)
}
