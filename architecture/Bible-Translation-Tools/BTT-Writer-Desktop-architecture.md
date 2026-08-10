# BTT-Writer-Desktop architecture

[Bible-Translation-Tools/BTT-Writer-Desktop](https://github.com/Bible-Translation-Tools/BTT-Writer-Desktop) — Bible Translation Tools Writer Application.

BTT-Writer Desktop --

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["BTT-Writer-Desktop"]
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
    Stack["Stack: Node.js, Docker"]
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
  Root["BTT-Writer-Desktop<br/>Bible Translation Tools Writer Application"]

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

**Notable files:** `.bowerrc`, `.dockerignore`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.jscsrc`, `.jshintrc`, `bower.json`, `CHANGELOG.md`, `config.json.enc`, `crowdin.yml`, `Dockerfile`, `dropbox_uploader.sh`, `gogs-client-lib-request.diff`, `gulpfile.js`, `LICENSE`, `makefile`, `package.json`, `pioneer.json`, `private.json.gpg`


## Runtime / integration sketch

```mermaid
flowchart LR
  Client["Browser / client"] --> App["BTT-Writer-Desktop"]
  App --> API["Routes / handlers"]
  API --> Services["Services"]
  Services --> Store["DB / files / remote APIs"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| HTML | 80 files |
| JavaScript | 69 files |
| Shell | 5 files |
| CSS | 5 files |
| YAML | 1 files |
| SQL | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Node.js, Docker |
| **Default branch** | `master` |
| **Org** | Bible-Translation-Tools |

## Related

- Source: [Bible-Translation-Tools/BTT-Writer-Desktop](https://github.com/Bible-Translation-Tools/BTT-Writer-Desktop)
- Branch analyzed: `master`
