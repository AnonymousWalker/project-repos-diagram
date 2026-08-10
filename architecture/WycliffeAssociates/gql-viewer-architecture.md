# gql-viewer architecture

[WycliffeAssociates/gql-viewer](https://github.com/WycliffeAssociates/gql-viewer) — _no GitHub description_.

gql-viewer is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["gql-viewer"]
    M0["public"]
    M1["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["gql-viewer<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["public"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `public`, `src`

**Notable files:** `.env`, `.gitignore`, `.npmrc`, `package-lock.json`, `package.json`, `tsconfig.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["gql-viewer"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 6 files |
| HTML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/gql-viewer](https://github.com/WycliffeAssociates/gql-viewer)
- Branch analyzed: `master`
