# auto-irg-experimental architecture

[WycliffeAssociates/auto-irg-experimental](https://github.com/WycliffeAssociates/auto-irg-experimental) — _no GitHub description_.

auto-irg-experimental is a public repository under WycliffeAssociates.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["auto-irg-experimental"]
    F0[".env"]
    F1[".gitignore"]
    F2["books.json"]
    F3["docker-compose.yml"]
    F4["Dockerfile"]
    F5["languages.json"]
    F6["main.py"]
    F7["PDF.py"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python, Docker"]
    Lang["Primary language: Python"]
  end

  Users --> F0
  Users --> F1
  Users --> F2
  Users --> F3
  Users --> F4
  Users --> F5
  Users --> F6
  Users --> F7
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["auto-irg-experimental<br/>No description on GitHub"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `.env`, `.gitignore`, `books.json`, `docker-compose.yml`, `Dockerfile`, `languages.json`, `main.py`, `PDF.py`, `README.md`, `requirements.txt`, `Resources.py`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["auto-irg-experimental core"]
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
| **Default branch** | `dev` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/auto-irg-experimental](https://github.com/WycliffeAssociates/auto-irg-experimental)
- Branch analyzed: `dev`
