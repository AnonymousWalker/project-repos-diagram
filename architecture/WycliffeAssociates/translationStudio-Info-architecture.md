# translationStudio-Info architecture

[WycliffeAssociates/translationStudio-Info](https://github.com/WycliffeAssociates/translationStudio-Info) — Source files for translationStudio Documentation.

See https://translationstudio-info.readthedocs.io/en/latest/ for the documentation, this repo is the source files.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["translationStudio-Info"]
    M0["docs"]
    M1["images"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Python"]
    Lang["Primary language: Python"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["translationStudio-Info<br/>Source files for translationStudio Documentation"]

  subgraph structure["Top-level layout"]
    D0["docs"]
    D1["images"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `docs`, `images`

**Notable files:** `.gitignore`, `AtS_Navigation_Handout.pdf`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["translationStudio-Info"]
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

- Source: [WycliffeAssociates/translationStudio-Info](https://github.com/WycliffeAssociates/translationStudio-Info)
- Branch analyzed: `master`
