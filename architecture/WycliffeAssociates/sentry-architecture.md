# sentry architecture

[WycliffeAssociates/sentry](https://github.com/WycliffeAssociates/sentry) — Sentry is a cross-platform crash reporting and aggregation platform..

Sentry is a cross-platform crash reporting and aggregation platform.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["sentry"]
    M0[".storybook"]
    M1[".tx"]
    M2[".vscode"]
    M3["api-docs"]
    M4["bin"]
    M5["config"]
    M6["docs"]
    M7["docs-ui"]
    M8["examples"]
    M9["scripts"]
    M10["src"]
    M11["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js, Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users --> M7
  Users --> M8
  Users --> M9
  Users --> M10
  Users --> M11
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["sentry<br/>Sentry is a cross-platform crash reporting and aggregation platform."]

  subgraph structure["Top-level layout"]
    D0[".storybook"]
    D1[".tx"]
    D2[".vscode"]
    D3["api-docs"]
    D4["bin"]
    D5["config"]
    D6["docs"]
    D7["docs-ui"]
    D8["examples"]
    D9["scripts"]
    D10["src"]
    D11["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
  Root --> D8
  Root --> D9
  Root --> D10
  Root --> D11
```

**Directories:** `.storybook`, `.tx`, `.vscode`, `api-docs`, `bin`, `config`, `docs`, `docs-ui`, `examples`, `scripts`, `src`, `tests`

**Notable files:** `.babelrc`, `.coveragerc`, `.dockerignore`, `.eslintignore`, `.eslintrc`, `.gitattributes`, `.gitignore`, `.gitmodules`, `.isort.cfg`, `.mailmap`, `.nvmrc`, `.prettierrc`, `.travis.yml`, `AUTHORS`, `Brewfile`, `CHANGES`, `codecov.yml`, `conftest.py`, `CONTRIBUTING.md`, `Dangerfile`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["sentry core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 2,032 files |
| JavaScript | 871 files |
| HTML | 164 files |
| CSS | 4 files |
| XML | 4 files |
| YAML | 1 files |
| Batch | 1 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/sentry](https://github.com/WycliffeAssociates/sentry)
- Branch analyzed: `master`
