# llm-rag architecture

[WycliffeAssociates/llm-rag](https://github.com/WycliffeAssociates/llm-rag) — _no GitHub description_.

1) python server.py 2) open another terminal 3) cd to wa-chat 4) npm run dev

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["llm-rag"]
    M0["data-sources"]
    M1["wa-chat"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python, Docker"]
    Lang["Primary language: TypeScript"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["llm-rag<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    D0["data-sources"]
    D1["wa-chat"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `data-sources`, `wa-chat`

**Notable files:** `.gitignore`, `config.json`, `core.py`, `database.py`, `docker-compose.yml`, `Dockerfile`, `glossary.py`, `init-database.py`, `rag-server.py`, `README.md`, `requirements.txt`, `run.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["llm-rag core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| TypeScript | 9 files |
| Python | 5 files |
| CSS | 2 files |
| YAML | 1 files |
| Shell | 1 files |
| HTML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python, Docker |
| **Default branch** | `llm-rag.walink.org` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/llm-rag](https://github.com/WycliffeAssociates/llm-rag)
- Branch analyzed: `llm-rag.walink.org`
