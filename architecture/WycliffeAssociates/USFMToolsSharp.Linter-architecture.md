# USFMToolsSharp.Linter architecture

[WycliffeAssociates/USFMToolsSharp.Linter](https://github.com/WycliffeAssociates/USFMToolsSharp.Linter) — A linter for USFM that uses USFMToolsSharp.

A linter for USFM that uses USFMToolsSharp

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMToolsSharp.Linter"]
    M0["USFMToolsSharp.Linter"]
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
  Root["USFMToolsSharp.Linter<br/>A linter for USFM that uses USFMToolsSharp"]

  subgraph structure["Top-level layout"]
    D0["USFMToolsSharp.Linter"]
  end

  Root --> D0
```

**Directories:** `USFMToolsSharp.Linter`

**Notable files:** `.gitignore`, `LICENSE`, `README.md`, `USFMToolsSharp.Linter.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["USFMToolsSharp.Linter"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 8 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMToolsSharp.Linter](https://github.com/WycliffeAssociates/USFMToolsSharp.Linter)
- Branch analyzed: `master`
