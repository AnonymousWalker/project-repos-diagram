# LatexToPDF architecture

[WycliffeAssociates/LatexToPDF](https://github.com/WycliffeAssociates/LatexToPDF) — Small converter shim around pdflatex.

Small converter shim around pdflatex

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["LatexToPDF"]
    M0[".vscode"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: Docker, .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["LatexToPDF<br/>Small converter shim around pdflatex"]

  subgraph structure["Top-level layout"]
    D0[".vscode"]
  end

  Root --> D0
```

**Directories:** `.vscode`

**Notable files:** `.dockerignore`, `.gitignore`, `Convert.cs`, `Dockerfile`, `host.json`, `LatexToPdf.csproj`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["LatexToPDF"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 1 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | Docker, .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/LatexToPDF](https://github.com/WycliffeAssociates/LatexToPDF)
- Branch analyzed: `master`
