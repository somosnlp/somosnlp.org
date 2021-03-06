import { defineConfig } from 'vite-plugin-windicss'
import colors from 'windicss/colors'
import defaultTheme from 'windicss/defaultTheme'
import typography from 'windicss/plugin/typography'

export default defineConfig({
  extract: {
    include: ['pages/**/*.{md,vue}', 'src/**/*.{vue,ts,css}'],
  },
  darkMode: 'class',
  plugins: [
    typography(),
  ],
  attributify: true,
  theme: {
    fontFamily: {
      sans: ['Inter', ...defaultTheme.fontFamily.sans],
      mono: ['JetBrains Mono', ...defaultTheme.fontFamily.mono],
    },
    extend: {
      colors: {
        ...colors,
        accent: colors.yellow,
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '65ch',
            color: 'inherit',
            a: {
              'color': 'inherit',
              'opacity': 0.75,
              'fontWeight': '500',
              'textDecoration': 'underline',
              '&:hover': {
                opacity: 1,
                color: colors.yellow[600],
              },
            },
            b: { color: 'inherit' },
            strong: { color: 'inherit' },
            em: { color: 'inherit' },
            h1: { color: 'inherit' },
            h2: { color: 'inherit' },
            h3: { color: 'inherit' },
            h4: { color: 'inherit' },
            code: { color: 'inherit' },
            blockquote: { color: 'inherit' },
          },
        },
      },
    },
  },
})
