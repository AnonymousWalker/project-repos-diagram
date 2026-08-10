# WACS-docker-old architecture

[WycliffeAssociates/WACS-docker-old](https://github.com/WycliffeAssociates/WACS-docker-old) — _no GitHub description_.

This project is UI customizations for WA's Gitea instance. The files here were forked from [Gitea](https://github.com/go-gitea/gitea) and [Gogs](https://gogs.io).

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["WACS-docker-old"]
    M0["wacs-gitea"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker"]
    Lang["Primary language: JavaScript"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["WACS-docker-old<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["wacs-gitea"]
  end

  Root --> D0
```

**Directories:** `wacs-gitea`

**Notable files:** `.env`, `.gitignore`, `app.ini`, `build.sh`, `DCO`, `deploy.sh`, `docker-compose.override.yml`, `docker-compose.yml`, `LICENSE`, `makefile`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["WACS-docker-old"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| JavaScript | 176 files |
| HTML | 132 files |
| CSS | 15 files |
| YAML | 3 files |
| Shell | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker |
| **Default branch** | `dev` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/WACS-docker-old](https://github.com/WycliffeAssociates/WACS-docker-old)
- Branch analyzed: `dev`
