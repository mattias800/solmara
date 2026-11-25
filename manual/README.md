# Solmara manual

The user manual, built with [Astro Starlight](https://starlight.astro.build) and served beside the website at `/solmara/manual/`. The Pages workflow builds it into `site/manual` on every push to `main`.

## Writing

Pages are Markdown in `src/content/docs/`, in four kinds, after the [Diátaxis](https://diataxis.fr) framework:

| Folder | Kind | For a reader who |
| --- | --- | --- |
| `learn/` | Tutorials | wants to be walked through making something |
| `guides/` | How-to guides | has a task in mind |
| `concepts/` | Explanation | wants to understand how a part works |
| `reference/` | Reference | wants to look something up |

The sidebar is set in `astro.config.mjs`. Write for musicians: plain words, second person, one idea a paragraph. Name Solmara's own devices only, never the hardware or the makers they are modelled on.

## Pictures

The pictures come from Solmara itself, so they can be made again whenever the editor changes:

```
python screenshots/shoot.py PATH/TO/BUILD
```

It builds the demo song in `screenshots/night-drive.json` with settings of its own (so nothing of your computer's shows, such as a device's nickname), takes a screenshot, and crops the pictures into `src/assets/`.

## Running it

```
npm install
npm run dev       # http://localhost:4321/solmara/manual/
npm run build     # into dist/
```
