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
    M3["agent-tmp"]
    M4["product-docs"]
    M5["public"]
    M6["scripts"]
    M7["src"]
    M8["tests"]
    M9["workers"]
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
  Users --> M9
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
    D3["agent-tmp"]
    D4["product-docs"]
    D5["public"]
    D6["scripts"]
    D7["src"]
    D8["tests"]
    D9["workers"]
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
  Root --> D9
```

**Directories:** `.claude`, `.github`, `.opencode`, `agent-tmp`, `product-docs`, `public`, `scripts`, `src`, `tests`, `workers`

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
| TypeScript | 732 files |
| XML | 13 files |
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
