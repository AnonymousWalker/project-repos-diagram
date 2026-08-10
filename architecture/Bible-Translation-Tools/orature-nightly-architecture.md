# orature-nightly architecture

[Bible-Translation-Tools/orature-nightly](https://github.com/Bible-Translation-Tools/orature-nightly) — Github Pages webapp for accessing Orature Builds.

Github Pages webapp for accessing Orature Builds

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["orature-nightly"]
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
  Root["orature-nightly<br/>Github Pages webapp for accessing Orature Builds"]

  subgraph structure["Top-level layout"]
    D0["public"]
    D1["src"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `public`, `src`

**Notable files:** `.gitignore`, `package-lock.json`, `package.json`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["orature-nightly"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 6 files |
| CSS | 2 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/orature-nightly](https://github.com/Bible-Translation-Tools/orature-nightly)
- Branch analyzed: `master`
