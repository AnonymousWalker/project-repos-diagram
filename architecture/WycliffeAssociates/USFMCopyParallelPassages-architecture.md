# USFMCopyParallelPassages architecture

[WycliffeAssociates/USFMCopyParallelPassages](https://github.com/WycliffeAssociates/USFMCopyParallelPassages) — Tool to generate USFM based upon parallel passages.

Tool to generate USFM based upon parallel passages

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMCopyParallelPassages"]
    M0["USFMCopyParallelPassages"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["USFMCopyParallelPassages<br/>Tool to generate USFM based upon parallel passages"]

  subgraph structure["Top-level layout"]
    D0["USFMCopyParallelPassages"]
  end

  Root --> D0
```

**Directories:** `USFMCopyParallelPassages`

**Notable files:** `.gitignore`, `LICENSE`, `USFMCopyParallelPassages.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["USFMCopyParallelPassages"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 7 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMCopyParallelPassages](https://github.com/WycliffeAssociates/USFMCopyParallelPassages)
- Branch analyzed: `master`
