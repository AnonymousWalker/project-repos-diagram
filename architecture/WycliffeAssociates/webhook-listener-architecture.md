# webhook-listener architecture

[WycliffeAssociates/webhook-listener](https://github.com/WycliffeAssociates/webhook-listener) — _no GitHub description_.

webhook-listener is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["webhook-listener"]
    M0["app"]
    M1["usfmlinter"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python, Docker"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["webhook-listener<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["app"]
    D1["usfmlinter"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `app`, `usfmlinter`

**Notable files:** `.dockerignore`, `.gitignore`, `docker-compose.yml`, `Dockerfile`, `json_file_builder.py`, `README.md`, `requirements.txt`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["webhook-listener core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 4 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python, Docker |
| **Default branch** | `dev` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/webhook-listener](https://github.com/WycliffeAssociates/webhook-listener)
- Branch analyzed: `dev`
