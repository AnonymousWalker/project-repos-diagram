# js-starter-kit architecture

[WycliffeAssociates/js-starter-kit](https://github.com/WycliffeAssociates/js-starter-kit) — Basic modern JavaScript project starter kit.

- Linter/Formatter: [prettier-eslint](https://github.com/prettier/prettier-eslint) - Transpiler: [Babel](https://babeljs.io) - Testing/Coverage: [Jest](https://facebook.github.io/jest/) - Bundler: [Webpack](https://webpack.js.org/)

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["js-starter-kit"]
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
  Root["js-starter-kit<br/>Basic modern JavaScript project starter kit"]

  subgraph structure["Top-level layout"]
    D0["src"]
  end

  Root --> D0
```

**Directories:** `src`

**Notable files:** `.babelrc`, `.eslintrc.json`, `.gitignore`, `.prettierrc.json`, `package-lock.json`, `package.json`, `README.md`, `webpack.config.js`, `yarn.lock`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["js-starter-kit"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 5 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/js-starter-kit](https://github.com/WycliffeAssociates/js-starter-kit)
- Branch analyzed: `master`
