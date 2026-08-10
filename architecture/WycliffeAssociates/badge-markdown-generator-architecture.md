# badge-markdown-generator architecture

[WycliffeAssociates/badge-markdown-generator](https://github.com/WycliffeAssociates/badge-markdown-generator) — _no GitHub description_.

This project was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app).

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["badge-markdown-generator"]
    M0["public"]
    M1["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["badge-markdown-generator<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["public"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `public`, `src`

**Notable files:** `.gitignore`, `package.json`, `README.md`, `yarn.lock`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["badge-markdown-generator"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 3 files |
| CSS | 2 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/badge-markdown-generator](https://github.com/WycliffeAssociates/badge-markdown-generator)
- Branch analyzed: `master`
