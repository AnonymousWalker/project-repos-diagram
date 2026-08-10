# badge-cop architecture

[WycliffeAssociates/badge-cop](https://github.com/WycliffeAssociates/badge-cop) — badge generation web server.

Repository for web server that listens for webhooks from DCS and creates badges for them

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["badge-cop"]
    M0["app"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python, Docker"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["badge-cop<br/>badge generation web server"]

  subgraph structure["Top-level layout"]
    D0["app"]
  end

  Root --> D0
```

**Directories:** `app`

**Notable files:** `.dockerignore`, `.gitignore`, `docker-compose.yml`, `Dockerfile`, `LICENSE`, `README.md`, `requirements.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["badge-cop core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 3 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python, Docker |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/badge-cop](https://github.com/WycliffeAssociates/badge-cop)
- Branch analyzed: `master`
