# TS-biel-files-playground architecture

[WycliffeAssociates/TS-biel-files-playground](https://github.com/WycliffeAssociates/TS-biel-files-playground) — Playground for external app to manage TS files;.

Playground for external app to manage TS files;

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["TS-biel-files-playground"]
    M0[".github"]
    M1["actions"]
    M2["en"]
    M3["supplemental"]
    M4["training"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: HTML"]
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
  Root["TS-biel-files-playground<br/>Playground for external app to manage TS files;"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["actions"]
    D2["en"]
    D3["supplemental"]
    D4["training"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `.github`, `actions`, `en`, `supplemental`, `training`

**Notable files:** `.gitignore`, `localizations.json`, `metadata.json`, `package-lock.json`, `package.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["TS-biel-files-playground"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| HTML | 6 files |
| YAML | 2 files |
| JavaScript | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/TS-biel-files-playground](https://github.com/WycliffeAssociates/TS-biel-files-playground)
- Branch analyzed: `master`
