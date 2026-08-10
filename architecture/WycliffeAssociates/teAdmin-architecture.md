# teAdmin architecture

[WycliffeAssociates/teAdmin](https://github.com/WycliffeAssociates/teAdmin) — Admin app for translationExchange.

moved to https://github.com/Bible-Translation-Tools/BTT-Exchanger

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["teAdmin"]
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
  Root["teAdmin<br/>Admin app for translationExchange"]

  subgraph structure["Top-level layout"]
    D0["public"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `public`, `src`

**Notable files:** `.gitignore`, `.travis.yml`, `extra-setup.sh`, `package.json`, `Procfile`, `README.md`, `sonar-project.properties`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["teAdmin"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 66 files |
| CSS | 4 files |
| Shell | 3 files |
| YAML | 2 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/teAdmin](https://github.com/WycliffeAssociates/teAdmin)
- Branch analyzed: `master`
