# Amano public website

Static marketing, Terms, Privacy and Support pages for https://getamano.app.
No app source or document data.

Published by GitHub Pages from `main` at the repository root.

## Editing

`build.py` generates the seven localized home pages, `sitemap.xml` and
`robots.txt` from its `S` and `STORY` dictionaries. Privacy, Terms and Support
pages are edited directly.
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

The 7-day trial and one-time lifetime price must match the app's StoreKit
configuration and App Store Connect listing. €7.99 is the Spain price; the app
shows each customer's local price before purchase. The phone scenes follow
the current listing metadata in the app repository at
`docs/localization/app-store-metadata.json`.
