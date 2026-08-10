# FontIndexer architecture

[WycliffeAssociates/FontIndexer](https://github.com/WycliffeAssociates/FontIndexer) — An indexer for mapping unicode to fonts.

An indexer for mapping unicode to fonts

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["FontIndexer"]
    M0["FontIndexer"]
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
  Root["FontIndexer<br/>An indexer for mapping unicode to fonts"]

  subgraph structure["Top-level layout"]
    D0["FontIndexer"]
  end

  Root --> D0
```

**Directories:** `FontIndexer`

**Notable files:** `.gitignore`, `FontIndexer.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["FontIndexer"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 2 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/FontIndexer](https://github.com/WycliffeAssociates/FontIndexer)
- Branch analyzed: `master`
