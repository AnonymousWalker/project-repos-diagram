# read.bibleineverylanguage.org architecture

[WycliffeAssociates/read.bibleineverylanguage.org](https://github.com/WycliffeAssociates/read.bibleineverylanguage.org) — _no GitHub description_.

File/Folder tree below:

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["read.bibleineverylanguage.org"]
    M0[".astro"]
    M1[".github"]
    M2[".vscode"]
    M3["playwright"]
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
  Root["read.bibleineverylanguage.org<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".astro"]
    D1[".github"]
    D2[".vscode"]
    D3["playwright"]
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

**Directories:** `.astro`, `.github`, `.vscode`, `playwright`, `public`, `src`, `tests`

**Notable files:** `.dev.vars`, `.eslintrc.cjs`, `.gitignore`, `.npmrc`, `astro.config.ts`, `biome.jsonc`, `changelog.md`, `manifest.ts`, `package.json`, `playwright-ct.config.ts`, `playwright.config.ts`, `pnpm-lock.yaml`, `prettier.config.js`, `README.md`, `stats.html`, `tailwind.config.cjs`, `tsconfig.json`, `vitest.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["read.bibleineverylanguage.org"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 53 files |
| JavaScript | 3 files |
| HTML | 2 files |
| YAML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `read-prod` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/read.bibleineverylanguage.org](https://github.com/WycliffeAssociates/read.bibleineverylanguage.org)
- Branch analyzed: `read-prod`
