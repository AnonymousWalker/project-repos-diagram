# read.bibletranslationtools.org architecture

[WycliffeAssociates/read.bibletranslationtools.org](https://github.com/WycliffeAssociates/read.bibletranslationtools.org) — Source for read.bibletranslationtools.org.

develop | [![Build Status](https://travis-ci.org/unfoldingWord-dev/door43.org.svg?branch=develop)](https://travis-ci.org/unfoldingWord-dev/door43.org) -->

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["read.bibletranslationtools.org"]
    M0[".devcontainer"]
    M1[".github"]
    M2["_data"]
    M3["_includes"]
    M4["_layouts"]
    M5["_plugins"]
    M6["_sass"]
    M7["css"]
    M8["fonts"]
    M9["js"]
    M10["pages"]
    M11["test"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: SCSS"]
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
  Root["read.bibletranslationtools.org<br/>Source for read.bibletranslationtools.org"]

  subgraph structure["Top-level layout"]
    D0[".devcontainer"]
    D1[".github"]
    D2["_data"]
    D3["_includes"]
    D4["_layouts"]
    D5["_plugins"]
    D6["_sass"]
    D7["css"]
    D8["fonts"]
    D9["js"]
    D10["pages"]
    D11["test"]
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

**Directories:** `.devcontainer`, `.github`, `_data`, `_includes`, `_layouts`, `_plugins`, `_sass`, `css`, `fonts`, `js`, `pages`, `test`

**Notable files:** `.gitignore`, `.travis.yml`, `404.md`, `_config.yml`, `_redirects.yml`, `build.sh`, `Gemfile`, `Gemfile.lock`, `karma.conf.intellij.js`, `karma.conf.js`, `karma_start.sh`, `karma_start_debug.sh`, `karma_stop.sh`, `LICENSE.md`, `package-lock.json`, `package.json`, `README.md`, `run_karma_tests.sh`, `temp-data.json`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["read.bibletranslationtools.org"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| SCSS | 93 files |
| JavaScript | 43 files |
| HTML | 19 files |
| YAML | 9 files |
| CSS | 8 files |
| TypeScript | 6 files |
| Shell | 5 files |
| Ruby | 4 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `develop` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/read.bibletranslationtools.org](https://github.com/WycliffeAssociates/read.bibletranslationtools.org)
- Branch analyzed: `develop`
