# USFMToolsSharp architecture

[WycliffeAssociates/USFMToolsSharp](https://github.com/WycliffeAssociates/USFMToolsSharp) — A USFM parser for c#.

A .net parser and rendering toolkit for USFM.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMToolsSharp"]
    M0[".github"]
    M1["USFMToolsSharp"]
    M2["USFMToolsSharpTest"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users --> M2
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["USFMToolsSharp<br/>A USFM parser for c#"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["USFMToolsSharp"]
    D2["USFMToolsSharpTest"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `USFMToolsSharp`, `USFMToolsSharpTest`

**Notable files:** `.gitignore`, `.travis.yml`, `LICENSE`, `README.md`, `USFMToolsSharp.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["USFMToolsSharp"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 168 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMToolsSharp](https://github.com/WycliffeAssociates/USFMToolsSharp)
- Branch analyzed: `master`
