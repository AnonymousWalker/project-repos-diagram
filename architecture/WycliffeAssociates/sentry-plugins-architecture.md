# sentry-plugins architecture

[WycliffeAssociates/sentry-plugins](https://github.com/WycliffeAssociates/sentry-plugins) — Official plugins for Sentry server.

Official plugins for Sentry server

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["sentry-plugins"]
    M0[".vscode"]
    M1["hooks"]
    M2["src"]
    M3["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Python"]
    Lang["Primary language: Python"]
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
  Root["sentry-plugins<br/>Official plugins for Sentry server"]

  subgraph structure["Top-level layout"]
    D0[".vscode"]
    D1["hooks"]
    D2["src"]
    D3["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
```

**Directories:** `.vscode`, `hooks`, `src`, `tests`

**Notable files:** `.babelrc`, `.gitattributes`, `.gitignore`, `.travis.yml`, `CHANGES`, `codecov.yml`, `conftest.py`, `Dangerfile`, `Gemfile`, `LICENSE`, `Makefile`, `MANIFEST.in`, `package.json`, `README.rst`, `setup.cfg`, `setup.py`, `webpack.config.js`, `yarn.lock`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["sentry-plugins core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 155 files |
| HTML | 13 files |
| JavaScript | 10 files |
| YAML | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/sentry-plugins](https://github.com/WycliffeAssociates/sentry-plugins)
- Branch analyzed: `master`
