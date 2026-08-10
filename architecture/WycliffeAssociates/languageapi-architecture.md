# languageapi architecture

[WycliffeAssociates/languageapi](https://github.com/WycliffeAssociates/languageapi) — monorepo for languageapi.

monorepo for languageapi

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["languageapi"]
    M0[".github"]
    M1["controller"]
    M2["explorer"]
    M3["hasura"]
    M4["langnames-server"]
    M5["langnames-sync"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: TypeScript"]
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
  Root["languageapi<br/>monorepo for languageapi"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["controller"]
    D2["explorer"]
    D3["hasura"]
    D4["langnames-server"]
    D5["langnames-sync"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `.github`, `controller`, `explorer`, `hasura`, `langnames-server`, `langnames-sync`

**Notable files:** `.env`, `.gitignore`, `docker-compose.yml`, `makefile`, `README.md`, `run-dev.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["languageapi"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 46 files |
| YAML | 40 files |
| SQL | 35 files |
| CSS | 3 files |
| HTML | 1 files |
| Shell | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `prod` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/languageapi](https://github.com/WycliffeAssociates/languageapi)
- Branch analyzed: `prod`
