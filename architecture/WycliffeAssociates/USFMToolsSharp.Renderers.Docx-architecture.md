# USFMToolsSharp.Renderers.Docx architecture

[WycliffeAssociates/USFMToolsSharp.Renderers.Docx](https://github.com/WycliffeAssociates/USFMToolsSharp.Renderers.Docx) — Docx Renderer for USFM.

A .net Docx rendering tool for USFM.

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["USFMToolsSharp.Renderers.Docx"]
    M0[".github"]
    M1["USFMToolsSharp.Renderers.Docx"]
    M2["USFMToolsSharp.Renderers.Docx.Tests"]
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
  Root["USFMToolsSharp.Renderers.Docx<br/>Docx Renderer for USFM"]

  subgraph structure["Top-level layout"]
    D0[".github"]
    D1["USFMToolsSharp.Renderers.Docx"]
    D2["USFMToolsSharp.Renderers.Docx.Tests"]
  end

  Root --> D0
  Root --> D1
  Root --> D2
```

**Directories:** `.github`, `USFMToolsSharp.Renderers.Docx`, `USFMToolsSharp.Renderers.Docx.Tests`

**Notable files:** `.gitattributes`, `.gitignore`, `.travis.yml`, `LICENSE`, `README.md`, `USFMToolsSharp.Renderers.Docx.sln`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["USFMToolsSharp.Renderers.Docx"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 11 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `develop` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/USFMToolsSharp.Renderers.Docx](https://github.com/WycliffeAssociates/USFMToolsSharp.Renderers.Docx)
- Branch analyzed: `develop`
