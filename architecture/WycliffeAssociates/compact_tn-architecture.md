# compact_tn architecture

[WycliffeAssociates/compact_tn](https://github.com/WycliffeAssociates/compact_tn) — Script to generate a compact tN..

1. `git pull` source repo in e.g. .../en_tn_lite 2. `source default_env.sh` to set common env vars 3. Update config.yaml: - Set `tn_dir` to the directory where the tN repo is. - set `book_ids` to contain the books you want to convert, or empty for all books. 4. `make run` 5. This directory should now contain the `*.md.pdf` files.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["compact_tn"]
    F0[".gitignore"]
    F1["books.json"]
    F2["config.yaml"]
    F3["default_env.sh"]
    F4["main.py"]
    F5["makefile"]
    F6["README.md"]
    F7["requirements.txt"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: YAML"]
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
  Root["compact_tn<br/>Script to generate a compact tN."]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```

**Notable files:** `.gitignore`, `books.json`, `config.yaml`, `default_env.sh`, `main.py`, `makefile`, `README.md`, `requirements.txt`, `style.css`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["compact_tn core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| YAML | 1 files |
| Shell | 1 files |
| Python | 1 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `main` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/compact_tn](https://github.com/WycliffeAssociates/compact_tn)
- Branch analyzed: `main`
