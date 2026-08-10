# Dot-Tools architecture

[WycliffeAssociates/Dot-Tools](https://github.com/WycliffeAssociates/Dot-Tools) — Utilities and Tools for the dot ecosystem.

Utilities and Tools for the dot ecosystem

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Dot-Tools"]
    M0[".github"]
    M1["DotOcrApp"]
    M2["DotPlaylistCache"]
    M3["DotVttEditor"]
    M4["packages"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Dot-Tools<br/>Utilities and Tools for the dot ecosystem"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["DotOcrApp"]
    D2["DotPlaylistCache"]
    D3["DotVttEditor"]
    D4["packages"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `.github`, `DotOcrApp`, `DotPlaylistCache`, `DotVttEditor`, `packages`

**Notable files:** `.gitignore`, `.oxfmtrc.json`, `.oxlintrc.json`, `mise.toml`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `README.md`, `tsconfig.base.json`, `vitest.workspace.ts`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["Dot-Tools"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 78 files |
| YAML | 4 files |
| XML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/Dot-Tools](https://github.com/WycliffeAssociates/Dot-Tools)
- Branch analyzed: `master`
