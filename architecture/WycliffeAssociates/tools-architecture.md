# tools architecture

[WycliffeAssociates/tools](https://github.com/WycliffeAssociates/tools) — Door43 tools for rendering and exporting Door43 pages and media..

* git_wrapper.py * smartquotes.pu * update_catalog.py

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tools"]
    M0["catalog"]
    M1["general_tools"]
    M2["gogs"]
    M3["obs"]
    M4["ta"]
    M5["tn"]
    M6["tq"]
    M7["tw"]
    M8["udb-ulb"]
    M9["usfm"]
    M10["uw"]
    M11["uwb"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users --> M3
  Users --> M4
  Users --> M5
  Users --> M6
  Users --> M7
  Users --> M8
  Users --> M9
  Users --> M10
  Users --> M11
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tools<br/>Door43 tools for rendering and exporting Door43 pages and media."]

  subgraph structure["Top-level layout"]
    D0["catalog"]
    D1["general_tools"]
    D2["gogs"]
    D3["obs"]
    D4["ta"]
    D5["tn"]
    D6["tq"]
    D7["tw"]
    D8["udb-ulb"]
    D9["usfm"]
    D10["uw"]
    D11["uwb"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
  Root --> D6
  Root --> D7
  Root --> D8
  Root --> D9
  Root --> D10
  Root --> D11
```

**Directories:** `catalog`, `general_tools`, `gogs`, `obs`, `ta`, `tn`, `tq`, `tw`, `udb-ulb`, `usfm`, `uw`, `uwb`

**Notable files:** `.gitignore`, `__init__.py`, `LICENSE`, `Makefile`, `README.md`, `requirements.txt`, `tex_bootstrap.sh`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["tools core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 131 files |
| Shell | 75 files |
| HTML | 9 files |
| XSLT | 5 files |
| CSS | 4 files |
| PHP | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tools](https://github.com/WycliffeAssociates/tools)
- Branch analyzed: `master`
