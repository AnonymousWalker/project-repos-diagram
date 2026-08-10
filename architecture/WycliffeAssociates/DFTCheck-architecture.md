# DFTCheck architecture

[WycliffeAssociates/DFTCheck](https://github.com/WycliffeAssociates/DFTCheck) — _no GitHub description_.

DFTCheck is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["DFTCheck"]
    M0["dft_data"]
    M1["frontend"]
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
  Root["DFTCheck<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["dft_data"]
    D1["frontend"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `dft_data`, `frontend`, `src`

**Notable files:** `.gitattributes`, `.gitignore`, `LICENSE`, `package-lock.json`, `package.json`, `pnpm-lock.yaml`, `README.md`, `tsconfig.json`, `tsconfig.node.json`, `vite.config.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["DFTCheck"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 5 files |
| Python | 3 files |
| HTML | 1 files |
| CSS | 1 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `main` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/DFTCheck](https://github.com/WycliffeAssociates/DFTCheck)
- Branch analyzed: `main`
