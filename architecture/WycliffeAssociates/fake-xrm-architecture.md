# fake-xrm architecture

[WycliffeAssociates/fake-xrm](https://github.com/WycliffeAssociates/fake-xrm) — Mocking framework for client-side Dynamics365.

*This project is experimental*

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["fake-xrm"]
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
  Root["fake-xrm<br/>Mocking framework for client-side Dynamics365"]

  subgraph structure["Top-level layout"]
    D0["src"]
  end

  Root --> D0
```

**Directories:** `src`

**Notable files:** `.babelrc`, `.eslintrc.json`, `.gitignore`, `.prettierrc.json`, `jest.config.js`, `package-lock.json`, `package.json`, `README.md`, `webpack.config.js`, `yarn.lock`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["fake-xrm"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 38 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/fake-xrm](https://github.com/WycliffeAssociates/fake-xrm)
- Branch analyzed: `master`
