# 8woc architecture

[WycliffeAssociates/8woc](https://github.com/WycliffeAssociates/8woc) — Repository for the 8-weeks-of-code internship program.

Repository for the 8-weeks-of-code internship program

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["8woc"]
    M0["data"]
    M1["images"]
    M2["modules"]
    M3["src"]
    M4["styles"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
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
  Root["8woc<br/>Repository for the 8-weeks-of-code internship program"]

  subgraph structure["Top-level layout"]
    D0["data"]
    D1["images"]
    D2["modules"]
    D3["src"]
    D4["styles"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `data`, `images`, `modules`, `src`, `styles`

**Notable files:** `.babelrc`, `.gitignore`, `API_Doc.md`, `index.html`, `main.js`, `package.json`, `README.md`, `requirements.js`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["8woc"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 119 files |
| CSS | 4 files |
| HTML | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `develop` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/8woc](https://github.com/WycliffeAssociates/8woc)
- Branch analyzed: `develop`
