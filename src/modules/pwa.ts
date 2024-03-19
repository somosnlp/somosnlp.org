import { UserModule } from '~/types'

// https://vite-pwa-org.netlify.app/guide/auto-update.html
export const install: UserModule = ({ isClient, router }) => {
  if (!isClient)
    return

  router.isReady().then(async () => {
    const { registerSW } = await import('virtual:pwa-register')
    registerSW({ immediate: true })
  })
}
