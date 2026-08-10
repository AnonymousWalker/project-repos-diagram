# Tech-Advance-Training architecture

[WycliffeAssociates/Tech-Advance-Training](https://github.com/WycliffeAssociates/Tech-Advance-Training) — A mirror repo for documentation with Guru.

A mirror repo for documentation with Guru

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["Tech-Advance-Training"]
    M0[".github"]
    M1["docs"]
    M2["images"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: HTML"]
    Lang["Primary language: HTML"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Tech-Advance-Training<br/>A mirror repo for documentation with Guru"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["docs"]
    D2["images"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `docs`, `images`

**Notable files:** `.gitignore`, `comments.json`, `README.md`, `readthedocs.yaml`


## Runtime / integration sketch

```mermaid
flowchart LR
  Consumer["Consumer"] --> Repo["Tech-Advance-Training"]
  Repo --> Artifacts["Libraries / tools / content"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| HTML | 82 files |
| JavaScript | 11 files |
| CSS | 4 files |
| Python | 1 files |
| Batch | 1 files |
| YAML | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | HTML |
| **Default branch** | `autosync` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/Tech-Advance-Training](https://github.com/WycliffeAssociates/Tech-Advance-Training)
- Branch analyzed: `autosync`
