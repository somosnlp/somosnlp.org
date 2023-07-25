#!/bin/bash

# Install Node.js if not already installed
if ! command -v node &>/dev/null; then
  curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
  sudo apt-get install -y nodejs
fi

# Install required Node.js packages
npm install @octokit/rest @octokit/auth-token

# Extract PR details
REPO=$(jq -r ".repository.full_name" $GITHUB_EVENT_PATH)
PR_NUMBER=$(jq -r ".pull_request.number" $GITHUB_EVENT_PATH)

# Check if the 'ofertas.ts' file was changed in the PR
FILE_CHANGED=$(git diff --name-only HEAD^ HEAD | grep -c "./pages/empleo/ofertas.ts")

# Comment template
COMMENT="""
Muchas gracias por contar con nuestra bolsa de empleo para darle más visibilidad a vuestra oferta.

La oferta X ya está publicada en somosnlp.org/empleo.

Te deseo mucha suerte en la búsqueda de talento.

Un saludo,

---

📣 Nueva oferta en la bolsa de empleo de #NLP

X @Y

También hay ofertas de empleo e investigación de ... 

⬇️ Revisa todas las ofertas o publica una nueva ⬇️

https://www.somosnlp.org/empleo
"""

if [ $FILE_CHANGED -gt 0 ]; then
  # Comment on the PR
  npx github-comment "$REPO#$PR_NUMBER" "$COMMENT" --token $GITHUB_TOKEN
fi
