# prototype-ephemera architecture

[WycliffeAssociates/prototype-ephemera](https://github.com/WycliffeAssociates/prototype-ephemera) — Intern project for a prototype for Ancient Greek translators resources.

Intern project for a prototype for Ancient Greek translators resources

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["prototype-ephemera"]
    M0["dummy-backend"]
    M1["public"]
    M2["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["prototype-ephemera<br/>Intern project for a prototype for Ancient Greek translators resources"]

  subgraph structure["Top-level layout"]
    D0["dummy-backend"]
    D1["public"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `dummy-backend`, `public`, `src`

**Notable files:** `.gitignore`, `biome.json`, `index.html`, `jest.config.cjs`, `LICENSE`, `package-lock.json`, `package.json`, `proskomma.d.ts`, `README.md`, `tsconfig.json`, `vite-env.d.ts`, `vite.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["prototype-ephemera"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 76 files |
| JavaScript | 4 files |
| CSS | 2 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `gwt.bibleineverylanguage.org` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/prototype-ephemera](https://github.com/WycliffeAssociates/prototype-ephemera)
- Branch analyzed: `gwt.bibleineverylanguage.org`
