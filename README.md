[![Netlify Status](https://api.netlify.com/api/v1/badges/a1a287d2-c2b8-4a1f-991d-0c1c73d2aa72/deploy-status)](https://app.netlify.com/sites/nlp-en-es/deploys)

# Página Web

<p align='center'>
  <img src='https://raw.githubusercontent.com/nlp-en-es/design/main/logo.svg' />
</p>

## Usage

### Development

First, install the dependencies with
```bash
pnpm install
```

Then just run
```bash
pnpm dev
```
and visit http://localhost:3333.

### Build

To build the website run
```bash
pnpm build
```
This will generate files in `dist` that are ready to be served.

### Deploy on Netlify

The page is automatically deployed by [Netlify](https://app.netlify.com/start) everytime you push to the `main` branch. All other branches will be depoyed to a preview URL (the link is visible in the corresponding Pull Request).

## License
[MIT License](https://github.com/nlp-en-es/pagina-web/blob/main/LICENSE)
