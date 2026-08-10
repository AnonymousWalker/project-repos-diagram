# biel-frontend architecture

[WycliffeAssociates/biel-frontend](https://github.com/WycliffeAssociates/biel-frontend) — _no GitHub description_.

https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs?ck_subscriber_id=1931241069

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["biel-frontend"]
    M0[".github"]
    M1[".vscode"]
    M2["dev-dist"]
    M3["docs"]
    M4["public"]
    M5["src"]
    M6["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["biel-frontend<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1[".vscode"]
    D2["dev-dist"]
    D3["docs"]
    D4["public"]
    D5["src"]
    D6["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
```

**Directories:** `.github`, `.vscode`, `dev-dist`, `docs`, `public`, `src`, `tests`

**Notable files:** `.gitignore`, `.prettierignore`, `astro.config.ts`, `biome.jsonc`, `bun.lock`, `makePageFindIndex.ts`, `manifest.ts`, `package.json`, `playwright.config.ts`, `purge.js`, `README.md`, `tsconfig.json`, `uno.config.ts`, `worker-configuration.d.ts`, `wrangler.jsonc`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["biel-frontend"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 56 files |
| JavaScript | 4 files |
| SCSS | 3 files |
| HTML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `prod` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/biel-frontend](https://github.com/WycliffeAssociates/biel-frontend)
- Branch analyzed: `prod`
