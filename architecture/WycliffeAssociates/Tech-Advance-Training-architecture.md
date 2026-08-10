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
    Core["source"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Unknown"]
    Lang["Primary language: Unknown"]
  end

  Users --> Core
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["Tech-Advance-Training<br/>A mirror repo for documentation with Guru"]

  subgraph structure["Top-level layout"]
    Src["repository root"]
  end

  Root --> Src
```



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
| — | — |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Unknown |
| **Default branch** | `autosync` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/Tech-Advance-Training](https://github.com/WycliffeAssociates/Tech-Advance-Training)
- Branch analyzed: `autosync`
