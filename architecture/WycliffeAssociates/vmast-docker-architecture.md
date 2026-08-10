# vmast-docker architecture

[WycliffeAssociates/vmast-docker](https://github.com/WycliffeAssociates/vmast-docker) — _no GitHub description_.

A docker setup for web app with custom configuration

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["vmast-docker"]
    M0["db"]
    M1["htdocs"]
    M2["node"]
    M3["php"]
    M4["scripts"]
    M5["ssl"]
    M6["web"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: PHP"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["vmast-docker<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["db"]
    D1["htdocs"]
    D2["node"]
    D3["php"]
    D4["scripts"]
    D5["ssl"]
    D6["web"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
```

**Directories:** `db`, `htdocs`, `node`, `php`, `scripts`, `ssl`, `web`

**Notable files:** `.env.example`, `.gitignore`, `.jshintrc`, `DbDockerfile`, `docker-compose.yml`, `Dockerfile`, `LICENSE`, `node_start.sh`, `NodeDockerfile`, `php_start.sh`, `PhpDockerfile`, `README.md`, `start.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["vmast-docker"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| PHP | 937 files |
| JavaScript | 83 files |
| CSS | 13 files |
| Shell | 7 files |
| SQL | 6 files |
| YAML | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `main` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/vmast-docker](https://github.com/WycliffeAssociates/vmast-docker)
- Branch analyzed: `main`
