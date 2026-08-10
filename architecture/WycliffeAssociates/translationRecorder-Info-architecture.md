# translationRecorder-Info architecture

[WycliffeAssociates/translationRecorder-Info](https://github.com/WycliffeAssociates/translationRecorder-Info) — Documentation for translationRecorder.

See http://tr-info.readthedocs.io/ for the documentation, this repo is the source files.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["translationRecorder-Info"]
    M0["appendix"]
    M1["docs"]
    M2["french_files"]
    M3["images"]
    M4["MMT_Handouts"]
    M5["presentations"]
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
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["translationRecorder-Info<br/>Documentation for translationRecorder"]

  subgraph structure["Top-level layout"]
    D0["appendix"]
    D1["docs"]
    D2["french_files"]
    D3["images"]
    D4["MMT_Handouts"]
    D5["presentations"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `appendix`, `docs`, `french_files`, `images`, `MMT_Handouts`, `presentations`

**Notable files:** `.gitignore`, `EditingRecordings_MTT.pdf`, `IconsChecking.pdf`, `images.rst`, `LICENSE`, `README.md`, `translationRecorder_How_to_Guide_v0.8.pdf`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["translationRecorder-Info"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| Python | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Python |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/translationRecorder-Info](https://github.com/WycliffeAssociates/translationRecorder-Info)
- Branch analyzed: `master`
