import path from 'path'
import fs from 'fs-extra'
import { defineConfig } from 'vite'
import Vue from '@vitejs/plugin-vue'
import Pages from 'vite-plugin-pages'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import Components from 'unplugin-vue-components/vite'
import Markdown from 'unplugin-vue-markdown/vite'
import WindiCSS from 'vite-plugin-windicss'
import Prism from 'markdown-it-prism'
import yaml from 'js-yaml'
import matter from 'gray-matter'
// @ts-expect-error missing types
import LinkAttributes from 'markdown-it-link-attributes'

// Supported locales for co-located page translations
// Convention: page.en.md, page.pt.vue → locale suffix before extension
// Files without suffix default to the DEFAULT_LOCALE
const LOCALES = ['es', 'en', 'pt']
const DEFAULT_LOCALE = 'es'
const NON_DEFAULT_LOCALES = LOCALES.filter(l => l !== DEFAULT_LOCALE)

export default defineConfig({
  resolve: {
    alias: {
      '~/': `${path.resolve(__dirname, 'src')}/`,
    },
  },
  plugins: [
    Vue({
      include: [/\.vue$/, /\.md$/],
      template: {
        transformAssetUrls: false,
      },
    }),

    // https://github.com/hannoeru/vite-plugin-pages
    Pages({
      extensions: ['vue', 'md'],
      dirs: 'pages',
      extendRoute(route) {
        const componentPath = path.resolve(__dirname, route.component.slice(1))

        // 1. Detect locale from filename suffix (e.g., page.en.vue, post.pt.md)
        const fileLocaleMatch = route.component.match(/\.([a-z]{2})\.(vue|md)$/)
        const fileLocale = fileLocaleMatch && LOCALES.includes(fileLocaleMatch[1])
          ? fileLocaleMatch[1]
          : null

        // 2. Detect locale from directory prefix (e.g., /en/hackathon, /pt/blog)
        const dirLocaleMatch = route.path.match(/^\/(en|pt)(?:\/|$)/)
        const dirLocale = dirLocaleMatch ? dirLocaleMatch[1] : null

        // 3. Effective locale: file suffix takes priority, then directory, then default
        const locale = fileLocale || dirLocale || DEFAULT_LOCALE

        // 4. Transform route path for file-locale suffixed pages
        if (fileLocale) {
          // Remove locale suffix: /blog/post.en → /blog/post
          let cleanPath = route.path.replace(new RegExp(`\\.${fileLocale}$`), '')
          // Normalize /index at end: /dir/index → /dir
          cleanPath = cleanPath.replace(/\/index$/, '') || '/'

          if (fileLocale !== DEFAULT_LOCALE) {
            route.path = `/${fileLocale}${cleanPath === '/' ? '' : cleanPath}`
          } else {
            route.path = cleanPath
          }

          // Update route name to avoid conflicts
          route.name = route.path === '/'
            ? `index-${fileLocale}`
            : route.path.slice(1).replace(/\//g, '-')
        }

        // 5. Compute basePath: canonical path without locale prefix (for translation matching)
        let basePath = route.path
        for (const loc of NON_DEFAULT_LOCALES) {
          if (basePath.startsWith(`/${loc}/`)) {
            basePath = basePath.slice(loc.length + 1)
            break
          }
          if (basePath === `/${loc}`) {
            basePath = '/'
            break
          }
        }

        // 6. Read frontmatter for markdown files
        if (componentPath.endsWith('.md')) {
          const md = fs.readFileSync(componentPath, 'utf-8')
          const { data } = matter(md)
          route.meta = Object.assign(route.meta || {}, { frontmatter: data })
        }

        // 7. Add locale metadata for translation detection
        route.meta = Object.assign(route.meta || {}, { locale, basePath })

        return route
      },
    }),

    // https://github.com/antfu/vite-plugin-vue-markdown
    Markdown({
      wrapperComponent: 'BlogPost',
      headEnabled: false,
      markdownItSetup(md) {
        // https://prismjs.com/
        md.use(Prism)
        md.use(LinkAttributes, {
          pattern: /^https?:\/\//,
          attrs: {
            target: '_blank',
            rel: 'noopener',
          },
        })
      },
    }),

    // https://github.com/antfu/unplugin-vue-components
    Components({
      // allow auto load markdown components under `./src/components/`
      extensions: ['vue', 'md'],

      // allow auto import and register components used in markdown
      include: [/\.vue$/, /\.vue\?vue/, /\.md$/],

      dts: 'components.d.ts',

      // auto import icons
      resolvers: [
        // https://github.com/antfu/unplugin-icons
        IconsResolver({
          prefix: '',
          // enabledCollections: ['carbon']
        }),
      ],
    }),

    // https://github.com/antfu/unplugin-icons
    Icons({ scale: 1.25 }),

    // https://github.com/antfu/vite-plugin-windicss
    WindiCSS({
      safelist: 'prose prose-sm m-auto text-left',
    }),

    // Inline YAML loader for i18n locale files
    {
      name: 'yaml-loader',
      transform(code, id) {
        if (!/\.ya?ml$/.test(id)) return
        const data = yaml.load(code)
        return {
          code: `export default ${JSON.stringify(data)}`,
          map: null,
        }
      },
    },
  ],
  // https://github.com/antfu/vite-ssg
  ssgOptions: {
    script: 'async',
    formatting: 'minify',
  },

  build: {
    rollupOptions: {
      plugins: [
        {
          name: 'stub-public-images',
          resolveId(id: string) {
            if (id.startsWith('/images/') || (/\.(png|jpe?g|gif|svg|bmp|webp)$/i.test(id) && id.startsWith('/'))) {
              return '\0stub-public:' + id
            }
          },
          load(id: string) {
            if (id.startsWith('\0stub-public:')) {
              const path = id.slice('\0stub-public:'.length)
              return `export default ${JSON.stringify(path)}`
            }
          },
        },
      ],
    },
  },

  optimizeDeps: {
    include: [
      'vue',
      'vue-router',
      '@vueuse/core',
    ],
    exclude: [
      'vue-demi',
    ],
  },
})
