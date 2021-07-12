import { useDark, useToggle } from '@vueuse/core'
import dayjs from 'dayjs'

export const isDark = useDark()
export const toggleDark = useToggle(isDark)

export function formatDate(d: string | Date, locale: string) {
    // return dayjs(d).locale(locale).format("LL")
    dayjs.locale('es')
    return dayjs(d).locale(locale).format("LL")
}
