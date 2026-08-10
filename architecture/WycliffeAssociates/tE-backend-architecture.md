# tE-backend architecture

[WycliffeAssociates/tE-backend](https://github.com/WycliffeAssociates/tE-backend) — _no GitHub description_.

moved to https://github.com/Bible-Translation-Tools/BTT-Exchanger

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tE-backend"]
    M0["InstallationScripts"]
    M1["scripts"]
    M2["tRecorderApi"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tE-backend<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["InstallationScripts"]
    D1["scripts"]
    D2["tRecorderApi"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `InstallationScripts`, `scripts`, `tRecorderApi`

**Notable files:** `.gitignore`, `.travis.yml`, `__init__.py`, `api_spec.txt`, `postgres-setup`, `README.md`, `sonar-project.properties`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["tE-backend"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 98 files |
| Shell | 7 files |
| YAML | 5 files |
| HTML | 1 files |
| JavaScript | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tE-backend](https://github.com/WycliffeAssociates/tE-backend)
- Branch analyzed: `master`
