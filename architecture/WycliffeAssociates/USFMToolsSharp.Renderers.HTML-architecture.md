# USFMToolsSharp.Renderers.HTML architecture

[WycliffeAssociates/USFMToolsSharp.Renderers.HTML](https://github.com/WycliffeAssociates/USFMToolsSharp.Renderers.HTML) — HTML Renderer for USFM.

A .net HTML rendering tool for USFM.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMToolsSharp.Renderers.HTML"]
    M0[".github"]
    M1["USFMToolsSharp.Renderers.HTML"]
    M2["USFMToolsSharp.Renderers.HTML.Tests"]
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
  Root["USFMToolsSharp.Renderers.HTML<br/>HTML Renderer for USFM"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["USFMToolsSharp.Renderers.HTML"]
    D2["USFMToolsSharp.Renderers.HTML.Tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `USFMToolsSharp.Renderers.HTML`, `USFMToolsSharp.Renderers.HTML.Tests`

**Notable files:** `.gitignore`, `LICENSE`, `README.md`, `style.css`, `USFMToolsSharp.Renderers.HTML.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["USFMToolsSharp.Renderers.HTML"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 3 files |
| CSS | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMToolsSharp.Renderers.HTML](https://github.com/WycliffeAssociates/USFMToolsSharp.Renderers.HTML)
- Branch analyzed: `master`
