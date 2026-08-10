# m2m-ctl architecture

[WycliffeAssociates/m2m-ctl](https://github.com/WycliffeAssociates/m2m-ctl) — Reusable control for N:N relationships in Dynamics 365.

This project was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app).

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["m2m-ctl"]
    M0["config"]
    M1["img"]
    M2["public"]
    M3["scripts"]
    M4["src"]
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
  Root["m2m-ctl<br/>Reusable control for N:N relationships in Dynamics 365"]

  subgraph structure["Top-level layout"]
    D0["config"]
    D1["img"]
    D2["public"]
    D3["scripts"]
    D4["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `config`, `img`, `public`, `scripts`, `src`

**Notable files:** `.codecov.yml`, `.gitignore`, `.travis.yml`, `package-lock.json`, `package.json`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["m2m-ctl"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 60 files |
| HTML | 2 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/m2m-ctl](https://github.com/WycliffeAssociates/m2m-ctl)
- Branch analyzed: `master`
