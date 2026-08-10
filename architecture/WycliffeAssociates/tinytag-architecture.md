# tinytag architecture

[WycliffeAssociates/tinytag](https://github.com/WycliffeAssociates/tinytag) — Read music meta data and length of MP3, OGG, OPUS, MP4, M4A, FLAC, WMA and Wave files with python 2 or 3.

tinytag =======

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["tinytag"]
    M0["tinytag"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["tinytag<br/>Read music meta data and length of MP3, OGG, OPUS, MP4, M4A, FLAC, WMA and Wave "]

  subgraph structure["Top-level layout"]
    D0["tinytag"]
  end

  Root --> D0
```

**Directories:** `tinytag`

**Notable files:** `.gitignore`, `.travis.yml`, `LICENSE`, `MANIFEST.in`, `README.md`, `runtests.py`, `setup.py`


## Runtime / integration sketch

```mermaid
flowchart LR
  Entry["CLI / scripts / app"] --> Core["tinytag core"]
  Core --> IO["Files / network / subprocess"]
  Core --> Lib["Python packages"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 6 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/tinytag](https://github.com/WycliffeAssociates/tinytag)
- Branch analyzed: `master`
