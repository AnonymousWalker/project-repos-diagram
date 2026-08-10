# astro-live-reader architecture

[WycliffeAssociates/astro-live-reader](https://github.com/WycliffeAssociates/astro-live-reader) — _no GitHub description_.

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["astro-live-reader"]
    M0[".vscode"]
    M1["functions"]
    M2["public"]
    M3["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
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
  Root["astro-live-reader<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".vscode"]
    D1["functions"]
    D2["public"]
    D3["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.vscode`, `functions`, `public`, `src`

**Notable files:** `.dockerignore`, `.gitignore`, `.npmrc`, `astro.config.mjs`, `chinook.db`, `manifest.ts`, `package.json`, `pnpm-lock.yaml`, `README.md`, `tailwind.config.cjs`, `tsconfig.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["astro-live-reader"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 9 files |
| TypeScript | 3 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/astro-live-reader](https://github.com/WycliffeAssociates/astro-live-reader)
- Branch analyzed: `master`
