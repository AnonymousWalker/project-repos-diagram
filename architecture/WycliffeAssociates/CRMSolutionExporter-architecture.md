# CRMSolutionExporter architecture

[WycliffeAssociates/CRMSolutionExporter](https://github.com/WycliffeAssociates/CRMSolutionExporter) — A utility to export solution files from dynamics crm.

A utility to export solution files from dynamics crm

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMSolutionExporter"]
    M0["CRMSolutionExporter"]
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
  Root["CRMSolutionExporter<br/>A utility to export solution files from dynamics crm"]

  subgraph structure["Top-level layout"]
    D0["CRMSolutionExporter"]
  end

  Root --> D0
```

**Directories:** `CRMSolutionExporter`

**Notable files:** `.gitignore`, `CRMSolutionExporter.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMSolutionExporter"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 3 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/CRMSolutionExporter](https://github.com/WycliffeAssociates/CRMSolutionExporter)
- Branch analyzed: `master`
