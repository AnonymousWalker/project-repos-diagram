# tE-Base architecture

[WycliffeAssociates/tE-Base](https://github.com/WycliffeAssociates/tE-Base) — Docker and configuration files for the translationExchange environment.

moved to https://github.com/Bible-Translation-Tools/BTT-Exchanger

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tE-Base"]
    M0["ap"]
    M1["config"]
    M2["dsn"]
    M3["postgres_data"]
    M4["scripts"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: Shell"]
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
  Root["tE-Base<br/>Docker and configuration files for the translationExchange environment"]

  subgraph structure["Top-level layout"]
    D0["ap"]
    D1["config"]
    D2["dsn"]
    D3["postgres_data"]
    D4["scripts"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
```

**Directories:** `ap`, `config`, `dsn`, `postgres_data`, `scripts`

**Notable files:** `.gitignore`, `docker-compose.yml`, `Dockerfile`, `install_build.sh`, `LICENSE`, `README.md`, `restore_te_db.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["tE-Base"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Shell | 6 files |
| Python | 3 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tE-Base](https://github.com/WycliffeAssociates/tE-Base)
- Branch analyzed: `master`
