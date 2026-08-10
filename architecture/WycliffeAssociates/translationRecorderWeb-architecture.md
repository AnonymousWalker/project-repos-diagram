# translationRecorderWeb architecture

[WycliffeAssociates/translationRecorderWeb](https://github.com/WycliffeAssociates/translationRecorderWeb) — Website for translationRecorder.

Website for translationRecorder

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["translationRecorderWeb"]
    M0["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["translationRecorderWeb<br/>Website for translationRecorder"]

  subgraph structure["Top-level layout"]
    D0["src"]
  end

  Root --> D0
```

**Directories:** `src`

**Notable files:** `.gitattributes`, `.gitignore`, `faviconData.json`, `gulpfile.js`, `index.html`, `package.json`, `README.md`, `sonar-project.properties`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["translationRecorderWeb"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 3 files |
| HTML | 3 files |
| CSS | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/translationRecorderWeb](https://github.com/WycliffeAssociates/translationRecorderWeb)
- Branch analyzed: `master`
