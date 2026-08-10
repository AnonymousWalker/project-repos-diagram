# usfmtools-js architecture

[Bible-Translation-Tools/usfmtools-js](https://github.com/Bible-Translation-Tools/usfmtools-js) — _no GitHub description_.

A TypeScript/JavaScript parser for [USFM](https://ubsicap.github.io/usfm/) (Unified Standard Format Markers), the standard encoding format for Scripture translations.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["usfmtools-js"]
    M0["__tests__"]
    M1["dist"]
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
  Root["usfmtools-js<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["__tests__"]
    D1["dist"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `__tests__`, `dist`, `src`

**Notable files:** `.gitignore`, `.npmignore`, `jest.config.js`, `package-lock.json`, `package.json`, `README.md`, `tsconfig.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["usfmtools-js"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 327 files |
| JavaScript | 164 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `main` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/usfmtools-js](https://github.com/Bible-Translation-Tools/usfmtools-js)
- Branch analyzed: `main`
