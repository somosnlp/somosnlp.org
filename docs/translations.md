# Translations in SomosNLP

The website uses a hybrid translation system that combines two approaches:
1. Vue i18n locales for UI elements and regular pages
2. Markdown-based translations for blog posts

## 1. Vue i18n Locales

Used for:
- UI elements (buttons, navigation, common text)
- Regular pages (landing page, about, etc.)
- Any non-blog content

Implementation:
- Translations are stored in locale files
- Default language is Spanish (`es`)
- Accessed using the `useI18n()` composable
- Example: `{{ t('not-found') }}`

## 2. Markdown-based Blog Translations

Used exclusively for blog posts under the `/blog` directory.

### File Structure
- Spanish (default): `pages/blog/post-name.md`
- English: `pages/blog/post-name.en.md`

### URL Structure
- Spanish: `/blog/post-name`
- English: `/en/blog/post-name`

### Blog List Behavior
- Spanish mode: Shows only `.md` files
- English mode: Shows `.en.md` files when available, falls back to `.md` files
- Prevents duplicate posts in the list
- Updates reactively when language changes

### Content Fallback Behavior
- If an English translation exists (`.en.md`), it will be shown when English is selected
- If no English translation exists, it falls back to Spanish content while maintaining the English UI

## Language Toggle Component

The `LocaleToggle.vue` component handles language switching:
- Updates the i18n locale for all pages
- Updates URLs only for blog posts
- Shows active language through opacity

## Implementation Details

### useLanguage Composable
Located in `src/composables/useLanguage.ts`:
- Manages the current language state
- Handles URL modifications for blog posts
- Syncs with vue-i18n locale
- Initializes language based on URL or locale

### [...all].vue Route Handler
Located in `pages/[...all].vue`:
- Handles dynamic content loading
- Manages blog post translations
- Falls back to Spanish content when needed
- Shows 404 when content is not found

### BlogList.vue Component
Located in `src/components/BlogList.vue`:
- Filters posts based on current language
- Shows appropriate translations
- Maintains proper post ordering by date
- Handles production/development differences

## Adding New Translations

### For UI Elements and Regular Pages
1. Add translations to locale files
2. Use `t('key')` in components

### For Blog Posts
1. Create the default Spanish post: `blog/post-name.md`
2. Create English translation: `blog/post-name.en.md`
3. Both files should have the same frontmatter structure with language-specific content

## Technical Notes

- The system uses TypeScript for type safety
- URL handling preserves proper routing history
- Content loading is optimized to prevent flashing
- Watch system ensures proper reactivity 
