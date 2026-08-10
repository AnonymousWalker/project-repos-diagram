# scripture-editor-proto architecture

[WycliffeAssociates/scripture-editor-proto](https://github.com/WycliffeAssociates/scripture-editor-proto) — _no GitHub description_.

A scripture editing application built with Tauri, React, and TypeScript in Vite.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["scripture-editor-proto"]
    M0[".claude"]
    M1[".github"]
    M2[".opencode"]
    M3["product-docs"]
    M4["public"]
    M5["scripts"]
    M6["src"]
    M7["tests"]
    M8["workers"]
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
  Users --> M7
  Users --> M8
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["scripture-editor-proto<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".claude"]
    D1[".github"]
    D2[".opencode"]
    D3["product-docs"]
    D4["public"]
    D5["scripts"]
    D6["src"]
    D7["tests"]
    D8["workers"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
  Root --> D8
```

**Directories:** `.claude`, `.github`, `.opencode`, `product-docs`, `public`, `scripts`, `src`, `tests`, `workers`

**Notable files:** `.browserslistrc`, `.env.example`, `.gitignore`, `.oxfmtrc.json`, `.oxlintrc.json`, `AGENTS.MD`, `index.html`, `knip.json`, `lefthook.yml`, `lingui.config.js`, `package.json`, `playwright.config.ts`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `postcss.config.cjs`, `PRODUCT.md`, `README.md`, `tsconfig.json`, `tsconfig.node.json`, `vite.tauri.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["scripture-editor-proto"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 727 files |
| XML | 11 files |
| Rust | 10 files |
| YAML | 7 files |
| Kotlin | 6 files |
| HTML | 4 files |
| JavaScript | 2 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/scripture-editor-proto](https://github.com/WycliffeAssociates/scripture-editor-proto)
- Branch analyzed: `master`
