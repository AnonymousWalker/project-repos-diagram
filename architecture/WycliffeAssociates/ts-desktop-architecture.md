# ts-desktop architecture

[WycliffeAssociates/ts-desktop](https://github.com/WycliffeAssociates/ts-desktop) — Bible Translation Tools Writer Application.

Repo is archived and has moved here: https://github.com/Bible-Translation-Tools/BTT-Writer-Desktop

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["ts-desktop"]
    M0[".github"]
    M1["__mocks__"]
    M2["__tests__"]
    M3["acceptance_tests"]
    M4["i18n"]
    M5["icons"]
    M6["scripts"]
    M7["src"]
    M8["unit_tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Node.js"]
    Lang["Primary language: HTML"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["ts-desktop<br/>Bible Translation Tools Writer Application"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["__mocks__"]
    D2["__tests__"]
    D3["acceptance_tests"]
    D4["i18n"]
    D5["icons"]
    D6["scripts"]
    D7["src"]
    D8["unit_tests"]
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
```

**Directories:** `.github`, `__mocks__`, `__tests__`, `acceptance_tests`, `i18n`, `icons`, `scripts`, `src`, `unit_tests`

**Notable files:** `.bowerrc`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.jscsrc`, `.jshintrc`, `.travis.yml`, `bower.json`, `config.json.enc`, `dropbox_uploader.sh`, `gogs-client-lib-request.diff`, `gulpfile.js`, `LICENSE`, `package.json`, `pioneer.json`, `private.json.enc`, `README.md`, `win64_installer.iss`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["ts-desktop"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| HTML | 85 files |
| JavaScript | 32 files |
| Shell | 10 files |
| CSS | 7 files |
| SQL | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/ts-desktop](https://github.com/WycliffeAssociates/ts-desktop)
- Branch analyzed: `master`
