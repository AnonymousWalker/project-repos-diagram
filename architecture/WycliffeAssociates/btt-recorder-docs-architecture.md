# btt-recorder-docs architecture

[WycliffeAssociates/btt-recorder-docs](https://github.com/WycliffeAssociates/btt-recorder-docs) — BTT Recorder documentation.

See https://btt-recorder.readthedocs.io/en/latest/ for the documentation, this repo is the source files.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["btt-recorder-docs"]
    M0["appendix"]
    M1["docs"]
    M2["french_files"]
    M3["images"]
    M4["las_files"]
    M5["presentations"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: HTML"]
    Lang["Primary language: HTML"]
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
  Root["btt-recorder-docs<br/>BTT Recorder documentation"]

  subgraph structure["Top-level layout"]
    D0["appendix"]
    D1["docs"]
    D2["french_files"]
    D3["images"]
    D4["las_files"]
    D5["presentations"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
  Root --> D3
  Root --> D4
  Root --> D5
```

**Directories:** `appendix`, `docs`, `french_files`, `images`, `las_files`, `presentations`

**Notable files:** `.gitignore`, `.readthedocs.yaml`, `comments.json`, `EditingRecordings_MTT.pdf`, `IconsChecking.pdf`, `LICENSE`, `README.md`, `translationRecorder_How_to_Guide_v0.8.pdf`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["btt-recorder-docs"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| HTML | 22 files |
| JavaScript | 14 files |
| CSS | 4 files |
| Python | 1 files |
| Batch | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | HTML |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/btt-recorder-docs](https://github.com/WycliffeAssociates/btt-recorder-docs)
- Branch analyzed: `master`
