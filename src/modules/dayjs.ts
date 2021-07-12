import dayjs from 'dayjs'
import LocalizedFormat from 'dayjs/plugin/localizedFormat'
import locale_es from 'dayjs/locale/es'
import { UserModule } from '~/types'

export const install: UserModule = () => {
    locale_es // <- hack to avoid locale_es getting tree-shaked
    dayjs.locale('es')
    dayjs.extend(LocalizedFormat)
}
