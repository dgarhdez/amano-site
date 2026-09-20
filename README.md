# Amano public website

Static marketing, Terms, Privacy and Support pages for https://getamano.app.
No app source or document data.

Published by GitHub Pages from `main` at the repository root.

## Editing

`build.py` generates every HTML page, `sitemap.xml` and `robots.txt` from the
copy in its `S` dictionary, one entry per locale (en, es, fr, de, it, pt, tr).
**Do not edit the generated HTML by hand** — the next build overwrites it.
Change the copy in `build.py`, then:

```
python3 build.py
```

and commit both the generator and the regenerated pages.

## App Store links

Acquisition links carry Apple Search Ads campaign attribution built from
`APP_ID` and `PROVIDER_TOKEN`, with a per-locale `ct` (`web-en`, `web-es`, …)
so App Store Connect reports each language page separately.

The "write a review" link is deliberately **untagged**: it is aimed at people
who already installed, and tagging it would count them as new installs.

## Claims that must match the app

The free-tier document count and the price appear in the pricing table. They
are also recorded in the app repository at `docs/product-facts.json`, generated
from `VaultLimits.freeDocuments`. If that file and this site disagree, the site
is wrong.
