# Go 101 Vietnamese translation rules

This file is the required working guide for people and agents translating this repository. Read it and `translations/vi/PROGRESS.md` before translating or changing translation tooling.

## 1. Project layout and source of truth

- Upstream project: [go101/go101](https://github.com/go101/go101), default branch `master`.
- English source files and the Go 101 application live in upstream-owned paths such as `pages/`, `web/`, and the root Go files. Treat them as read-only.
- Vietnamese work lives only under `translations/vi/`. Keep each translated page at the same relative path as its English source, for example:
  - `pages/fundamentals/introduction.tmd` → `translations/vi/pages/fundamentals/introduction.tmd`
  - `pages/website/index.html` → `translations/vi/pages/website/index.html`
- `translations/vi/PROGRESS.md` records the queue and translation state. `translations/vi/GLOSSARY.md` records decisions about terminology.
- The English source remains the source of truth. Do not overwrite or replace it with a translation.
- The upstream [`LICENSE`](https://github.com/go101/go101/blob/master/LICENSE) reserves rights to the English and Chinese versions. It permits redistribution of other language translations when each translated page visibly links to `https://go101.org`, `https://www.tapirgames.com`, and `https://x.com/TapirLiu`. The static builder adds these links to every Vietnamese page.

## 2. Non-negotiable translation rules

1. Never edit, remove, rename, or move upstream-owned English files to add translations. Keep changes in `translations/vi/`, `scripts/`, and translation-specific GitHub workflows.
2. Translate the complete page. Do not summarize, omit examples, invent explanations, or add translator commentary that is absent from the source.
3. Keep the Vietnamese concise and faithful to the original meaning. Do not make a translation longer just to sound more formal.
4. Preserve Go identifiers, keywords, API names, command output, file paths, URLs, and configuration keys exactly. Translate prose and comments; translate user-facing strings only when doing so does not change the executable example.
5. Keep source structure: headings, order, lists, tables, links, images, code fences, HTML blocks, and TapirMD (`.tmd`) directives. Translate image alt text and visible labels, not asset URLs.
6. Do not leave unexplained non-English source text in the translation. Preserve a non-Vietnamese string only when it is a literal the reader must type or an identifier/URL that must remain exact; add a short Vietnamese gloss when needed.
7. Never edit generated output in the English `pages/` tree as a way of placing a translation. Keep the Vietnamese source and its rendered output under `translations/vi/`.

## 3. Page format and links

- `.tmd` pages use TapirMD, not plain Markdown. Preserve its heading, link, inline-formatting, HTML-block, and directive syntax. Do not normalize a page to another markup format.
- `.html` pages are HTML fragments rendered inside the existing Go 101 page template. Keep the fragment structure and classes; do not paste a complete `<!doctype html>` document into a fragment.
- Preserve existing Go 101 internal route names. Links to another translated page should resolve to its `/vi/` counterpart; if that page has not been translated, link to the English page.
- Preserve external URLs and asset paths. Use source assets unless a translated page has its own image under the matching `translations/vi/pages/.../res/` directory.
- The static build renders `.tmd` translation files with the pinned `go101.org/tmd.go` v0.0.8 renderer (Go 1.21+) and places the resulting Vietnamese page under `/vi/`. It must never copy a Vietnamese page into the English source tree.

## 4. Vietnamese style and terminology

- Write direct, natural technical Vietnamese. Address the reader as “bạn” when needed; avoid adding “chúng ta” or “tôi” unless the source uses first person.
- Translate meaning, not word order. Keep sentences clear and compact.
- Prefer English-first terminology when an English term is the normal Go/developer term. Do not force a Vietnamese equivalent that makes the sentence less accurate or less natural.
- Keep one term consistent within a page. Add new decisions to `translations/vi/GLOSSARY.md`.
- Go terminology to keep in English when used as technical concepts includes: `goroutine`, `channel`, `slice`, `map`, `interface`, `method set`, `type parameter`, `type constraint`, `zero value`, `nil`, `defer`, `panic`, `recover`, `garbage collection (GC)`, `runtime`, `Go toolchain`, `data race`, `memory model`, and `happens-before`.
- Translate ordinary prose even when it contains English technical terms. Do not translate identifiers or add a parenthetical Vietnamese translation after every term.
- In Vietnamese text, use normal Vietnamese punctuation and put spaces between Vietnamese prose and English terms where appropriate.

## 5. Required workflow for each translation session

1. Read this file, `translations/vi/PROGRESS.md`, and the English source page.
2. Choose the next page from the learning order in `PROGRESS.md`; translate the page in full to the matching path under `translations/vi/pages/`.
3. Review code blocks, comments, links, image alt text, tables, inline HTML, and TapirMD syntax against the source.
4. Run `python3 scripts/translation_status.py` and `python3 scripts/build_pages.py --check-only` before proposing a batch. Mark a source revision reviewed only after the translation has been checked:

   ```sh
   python3 scripts/translation_status.py --mark-reviewed pages/fundamentals/introduction.tmd
   ```

5. Update `translations/vi/PROGRESS.md` and add any settled terms to `translations/vi/GLOSSARY.md`.
6. When an upstream page changes, re-read the changed English source and update its Vietnamese counterpart. Do not overwrite a translation blindly.

## 6. Progress and upstream drift

`scripts/translation_status.py` compares translated page paths with `pages/` and checks the recorded source blob SHA in `translations/vi/.sync-state.json`.

- **Missing**: English page has no Vietnamese source.
- **Stale**: source SHA changed after the translation was last reviewed.
- **Orphan**: Vietnamese source has no matching English page; check whether upstream renamed or removed the page.
- **Current**: translated source exists and its recorded English source SHA matches.

Never update `.sync-state.json` automatically as part of an upstream merge. A translator must review the new source before recording it as current.

## 7. Zero-conflict upstream architecture

- Keep upstream English paths unchanged; translation files, scripts, and workflows are fork-owned additions.
- The daily/manual upstream workflow fetches `go101/go101:master`, merges it into a dedicated sync branch, and opens or updates a pull request. It does not push upstream content directly to `master`.
- Resolve a conflict only after inspecting both sides. If a conflict touches an upstream-owned page, retain the upstream source and keep translation edits under `translations/vi/`.
- After merging upstream changes, run the translation status checker. Changed English sources will become stale until reviewed and re-marked.

## 8. Language switching and GitHub Pages

- `/` is a language portal. `/vi/` contains the Vietnamese landing page and translated routes. EN links point to the matching page on the official `go101.org` site; English pages are not republished by this Pages build.
- The language switch appears on every Vietnamese page. English source pages stay untouched in the repository. The official Go 101 site is independently operated, so its own pages are not modified to add a VI switch.
- Stale or unreviewed Vietnamese pages are omitted from the deployment. If the home translation is stale, the build publishes a Vietnamese status page there so upstream sync can still be reviewed and merged.
- GitHub Pages output is built into `_site/`. Generated output is not committed. Do not change upstream Go templates or source files to add the switcher.
- Build locally with `python3 scripts/build_pages.py`. Use `python3 scripts/build_pages.py --check-only` for a quick validation. The Pages workflow builds on pull requests and deploys only from `master` or a manual dispatch.
