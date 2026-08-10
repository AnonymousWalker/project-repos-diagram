# CRMSolutionImporter architecture

[WycliffeAssociates/CRMSolutionImporter](https://github.com/WycliffeAssociates/CRMSolutionImporter) — A utitlity to import solutions into CRM.

A utility to import solutions into CRM

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMSolutionImporter"]
    M0["CRMSolutionImporter"]
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
  Root["CRMSolutionImporter<br/>A utitlity to import solutions into CRM"]

  subgraph structure["Top-level layout"]
    D0["CRMSolutionImporter"]
  end

  Root --> D0
```

**Directories:** `CRMSolutionImporter`

**Notable files:** `.gitignore`, `CRMSolutionImporter.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMSolutionImporter"]
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

- Source: [WycliffeAssociates/CRMSolutionImporter](https://github.com/WycliffeAssociates/CRMSolutionImporter)
- Branch analyzed: `master`
