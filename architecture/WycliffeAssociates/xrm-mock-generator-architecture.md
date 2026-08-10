# xrm-mock-generator architecture

[WycliffeAssociates/xrm-mock-generator](https://github.com/WycliffeAssociates/xrm-mock-generator) — :book:  Generates a mock Xrm.Page object.  Commonly used by xrm-mock to test Dynamics 365 client-side customisations..

Generates a mock Xrm.Page object.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["xrm-mock-generator"]
    M0["src"]
    M1["test"]
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
  Root["xrm-mock-generator<br/>:book:  Generates a mock Xrm.Page object.  Commonly used by xrm-mock to test Dyn"]

  subgraph structure["Top-level layout"]
    D0["src"]
    D1["test"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `src`, `test`

**Notable files:** `.gitattributes`, `.gitignore`, `.npmignore`, `package-lock.json`, `package.json`, `README.md`, `wallaby.js`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["xrm-mock-generator"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 9 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/xrm-mock-generator](https://github.com/WycliffeAssociates/xrm-mock-generator)
- Branch analyzed: `master`
