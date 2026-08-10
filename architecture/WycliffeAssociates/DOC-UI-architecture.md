# DOC-UI architecture

[WycliffeAssociates/DOC-UI](https://github.com/WycliffeAssociates/DOC-UI) — Frontend for the DOC/IRG project.

This is UI code to provide a front end to the document python module backend.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["DOC-UI"]
    M0[".github"]
    M1["public"]
    M2["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Docker"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["DOC-UI<br/>Frontend for the DOC/IRG project"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["public"]
    D2["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `public`, `src`

**Notable files:** `.dockerignore`, `.gitignore`, `.prettierrc.js`, `Dockerfile`, `jest.config.js`, `jest.setup.js`, `nginx-backend-not-found.conf`, `nginx.conf`, `package-lock.json`, `package.json`, `README.md`, `snowpack.config.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["DOC-UI"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 4 files |
| HTML | 1 files |
| Svelte | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Docker |
| **Default branch** | `develop` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/DOC-UI](https://github.com/WycliffeAssociates/DOC-UI)
- Branch analyzed: `develop`
