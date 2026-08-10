# translationExchange architecture

[WycliffeAssociates/translationExchange](https://github.com/WycliffeAssociates/translationExchange) — _no GitHub description_.

| Branch | Build Status | | --- | --- | | Master | [![Build Status](https://travis-ci.org/WycliffeAssociates/translationExchange.svg?branch=master)](https://travis-ci.org/WycliffeAssociates/translationExchange) | | Dev | [![Build Status](https://travis-ci.org/WycliffeAssociates/translationExchange.svg?branch=dev)](https://travis-ci.org/WycliffeAssociates/translationExchange) |

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["translationExchange"]
    M0[".idea"]
    M1["babel_cache"]
    M2["public"]
    M3["src"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["translationExchange<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0[".idea"]
    D1["babel_cache"]
    D2["public"]
    D3["src"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.idea`, `babel_cache`, `public`, `src`

**Notable files:** `.babelrc`, `.eslintrc`, `.gitignore`, `.travis.yml`, `cert.pem`, `extra-setup.sh`, `key.pem`, `package.json`, `Procfile`, `README.md`, `server.js`, `sonar-project.properties`, `webpack.config.js`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["translationExchange"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 279 files |
| CSS | 12 files |
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

- Source: [WycliffeAssociates/translationExchange](https://github.com/WycliffeAssociates/translationExchange)
- Branch analyzed: `master`
