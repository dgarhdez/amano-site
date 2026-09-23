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

## Matte phone images

The site's background is `#F4F6F9` in `build.py`. Render phone stills from the
app's current screenshot captures with `goldie/make-store-shot.py --still`.
Do not use that script's default H.264 video-to-frame export for the website:
it changes the background from `#F4F6F9` to a darker, nonuniform color. The
direct Matte PNG capture preserves the exact background and phone shadow.

For each locale and scene, run the renderer from the app repository with the
same Matte arguments as the existing images:

```sh
python3 goldie/make-store-shot.py --raw RAW.png --headline '.' \
  --out /tmp/amano-phone.png --background '#F4F6F9' --width 1200 --height 1600 \
  --frame-color glacier --device-scale 0.95 --device-offset-y 0 \
  --rotation-x 3 --rotation-y -7 --still
```

Then, from this website repository:

```sh
magick /tmp/amano-phone.png -define webp:lossless=true assets/phones/en/folders.webp
sh scripts/check-phone-background.sh
```

Use each scene's matching output path, rather than the example `en/folders.webp`.
Lossless WebP matters here: lossy encoding can shift the edge pixels by a
point even when the PNG is correct. The check verifies all 42 images against
the current `--paper` color.
