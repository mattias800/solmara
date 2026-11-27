# Solmara website and manual

One [Astro](https://astro.build) project for both, served on GitHub Pages at `/solmara/`. The Pages workflow builds it on every push to `main` that touches `web/`.

- **The website** is `src/pages/`, with its layout in `src/layouts/Site.astro` and its look in `src/styles/`.
- **The manual** is [Starlight](https://starlight.astro.build), from `src/content/docs/manual/`, at `/solmara/manual/`.

## The devices

Every device page and card is made from the app itself:

```
python scripts/devices.py PATH/TO/BUILD
```

It asks Solmara for every device (its name, kind, summary and controls) and takes a fresh picture of each face, with settings of its own so nothing of your computer's shows (a device's nickname names the hardware it is modeled on). It writes `src/data/devices.json`, `src/data/controls/`, and `src/assets/devices/`. It stops if any of the app's words name a maker or a model the public site must not carry. `--only TYPE_ID,...` redoes some; `--no-faces` skips the pictures.

Laid over that by hand:

- `src/data/blurbs.json`: a device's own words for the website, by its name.
- `src/data/site.json`: devices still being built (shown with a tag), devices left off the website, the mastering suite, and the families the pages group devices in.
- `src/data/demos.json`: sound demos, by a device's page name.

## Writing the manual

Pages are Markdown, in four kinds after the [Diátaxis](https://diataxis.fr) framework:

| Folder | Kind | For a reader who |
| --- | --- | --- |
| `learn/` | Tutorials | wants to be walked through making something |
| `guides/` | How-to guides | has a task in mind |
| `concepts/` | Explanation | wants to understand how a part works |
| `reference/` | Reference | wants to look something up |

The sidebar is set in `astro.config.mjs`. Write for musicians: plain words, second person, one idea a paragraph. Name Solmara's own devices only, never the hardware or the makers they are modeled on.

The manual's pictures come from Solmara too: `python screenshots/shoot.py PATH/TO/BUILD` builds the demo song in `screenshots/night-drive.json` and crops the pictures into `src/assets/clips/`.

## Running it

```
npm install
npm run dev       # http://localhost:4321/solmara/
npm run build     # into dist/
```
