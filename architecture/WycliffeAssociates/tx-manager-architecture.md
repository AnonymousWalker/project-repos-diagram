# tx-manager architecture

[WycliffeAssociates/tx-manager](https://github.com/WycliffeAssociates/tx-manager) — Codebase for translationConvertor (tX).

Codebase for translationConvertor (tX)

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tx-manager"]
    M0[".devcontainer"]
    M1["docs"]
    M2["functions"]
    M3["libraries"]
    M4["scripts"]
    M5["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tx-manager<br/>Codebase for translationConvertor (tX)"]

  subgraph structure["Top-level layout"]
    D0[".devcontainer"]
    D1["docs"]
    D2["functions"]
    D3["libraries"]
    D4["scripts"]
    D5["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.devcontainer`, `docs`, `functions`, `libraries`, `scripts`, `tests`

**Notable files:** `.coveragerc`, `.gitignore`, `.travis.yml`, `LICENSE`, `project.develop.json`, `project.master.json`, `project.poc.json`, `project.test.json`, `README.rst`, `requirements.txt`, `setup.py`, `test-setup.py`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["tx-manager core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 226 files |
| Shell | 5 files |
| HTML | 2 files |
| YAML | 2 files |
| Batch | 1 files |
| JavaScript | 1 files |
| PHP | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `develop` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tx-manager](https://github.com/WycliffeAssociates/tx-manager)
- Branch analyzed: `develop`
