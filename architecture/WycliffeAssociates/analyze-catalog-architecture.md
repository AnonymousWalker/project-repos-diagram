# analyze-catalog architecture

[WycliffeAssociates/analyze-catalog](https://github.com/WycliffeAssociates/analyze-catalog) — Browse and process two unfoldingWord catalog datasets..

Browse and process two unfoldingWord catalog datasets.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["analyze-catalog"]
    M0["__test__"]
    M1["data"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Docker"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["analyze-catalog<br/>Browse and process two unfoldingWord catalog datasets."]

  subgraph structure["Top-level layout"]
    D0["__test__"]
    D1["data"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `__test__`, `data`

**Notable files:** `.dockerignore`, `.eslintrc.js`, `.gitignore`, `compare.js`, `Dockerfile`, `entrypoint.sh`, `functions.js`, `helpers.js`, `index.js`, `makefile`, `package-lock.json`, `package.json`, `readme.MD`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["analyze-catalog"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 6 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/analyze-catalog](https://github.com/WycliffeAssociates/analyze-catalog)
- Branch analyzed: `master`
