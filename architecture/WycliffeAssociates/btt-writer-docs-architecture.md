# btt-writer-docs architecture

[WycliffeAssociates/btt-writer-docs](https://github.com/WycliffeAssociates/btt-writer-docs) — Documentation for BTT Writer.

This is a repository for documentation for BTT Writer. See https://btt-writer-docs.readthedocs.io/en/latest/ for the documentation, this repo is the source files.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["btt-writer-docs"]
    M0["docs"]
    M1["french_appendices"]
    M2["images"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["btt-writer-docs<br/>Documentation for BTT Writer"]

  subgraph structure["Top-level layout"]
    D0["docs"]
    D1["french_appendices"]
    D2["images"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `docs`, `french_appendices`, `images`

**Notable files:** `.readthedocs.yaml`, `DFootnote.pdf`, `DFootnote.pptx`, `LICENSE`, `README.md`, `readme.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["btt-writer-docs"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 2 files |
| Batch | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/btt-writer-docs](https://github.com/WycliffeAssociates/btt-writer-docs)
- Branch analyzed: `master`
