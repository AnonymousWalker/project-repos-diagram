# dot-web architecture

[WycliffeAssociates/dot-web](https://github.com/WycliffeAssociates/dot-web) — _no GitHub description_.

An astro site to consume deaf new testaments.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["dot-web"]
    M0[".github"]
    M1["public"]
    M2["src"]
    M3["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["dot-web<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["public"]
    D2["src"]
    D3["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.github`, `public`, `src`, `tests`

**Notable files:** `.eslintrc.cjs`, `.gitignore`, `AGENTS.md`, `astro.config.mjs`, `package.json`, `playwright.config.ts`, `pnpm-lock.yaml`, `README.md`, `tsconfig.json`, `uno.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["dot-web"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 40 files |
| YAML | 2 files |
| XML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/dot-web](https://github.com/WycliffeAssociates/dot-web)
- Branch analyzed: `master`
