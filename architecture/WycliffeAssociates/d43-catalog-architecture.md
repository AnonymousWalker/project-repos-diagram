# d43-catalog architecture

[WycliffeAssociates/d43-catalog](https://github.com/WycliffeAssociates/d43-catalog) — Lambda functions for the Door43 Catalog..

master:

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["d43-catalog"]
    M0[".devcontainer"]
    M1["aws_configuration"]
    M2["functions"]
    M3["libraries"]
    M4["tests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python, Docker"]
    Lang["Primary language: Python"]
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
  Root["d43-catalog<br/>Lambda functions for the Door43 Catalog."]

  subgraph structure["Top-level layout"]
    D0[".devcontainer"]
    D1["aws_configuration"]
    D2["functions"]
    D3["libraries"]
    D4["tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `.devcontainer`, `aws_configuration`, `functions`, `libraries`, `tests`

**Notable files:** `.coveragerc`, `.gitignore`, `.travis.yml`, `Dockerfile`, `entrypoint-test.sh`, `execute.py`, `install-apex.sh`, `jenkins-wa.sh`, `makefile`, `project.develop.json`, `project.json`, `project.poc.json`, `project.prod.json`, `README.md`, `requirements.txt`, `setup.py`, `test-setup.py`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["d43-catalog core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 97 files |
| YAML | 6 files |
| XML | 5 files |
| Shell | 3 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python, Docker |
| **Default branch** | `develop` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/d43-catalog](https://github.com/WycliffeAssociates/d43-catalog)
- Branch analyzed: `develop`
