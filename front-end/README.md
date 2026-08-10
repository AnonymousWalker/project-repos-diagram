# Architecture viewer

Vite + React app that renders the repo’s architecture markdown with a Mermaid renderer tuned for large diagrams (pan/zoom, no forced width squashing).

## Run

From this folder:

```bash
pnpm install
pnpm dev
```

Open http://localhost:5173

## Build

```bash
pnpm build
pnpm preview
```

Markdown is loaded from the parent repo via Vite (`architecture/**`, hand-authored Orature/Fetcher docs, and the index). After regenerating diagrams, restart or refresh the dev server if new files were added.
