# CRMImporter architecture

[WycliffeAssociates/CRMImporter](https://github.com/WycliffeAssociates/CRMImporter) — A data import library for dynamics crm.

A data import library for dynamics crm

## System context

```mermaid
flowchart TB
  subgraph users["Users / consumers"]
    Users["Developers / translators / services"]
  end

  subgraph project["CRMImporter"]
    M0["CRMImporter"]
    M1["CRMImporterTests"]
  end

  subgraph meta["Project profile"]
    Stack["Stack: .NET / C#"]
    Lang["Primary language: C#"]
  end

  Users --> M0
  Users --> M1
  Users -.-> Stack
```

## Repository structure

```mermaid
flowchart TB
  Root["CRMImporter<br/>A data import library for dynamics crm"]

  subgraph structure["Top-level layout"]
    D0["CRMImporter"]
    D1["CRMImporterTests"]
  end

  Root --> D0
  Root --> D1
```

**Directories:** `CRMImporter`, `CRMImporterTests`

**Notable files:** `.gitignore`, `CRMImporter.sln`, `LICENSE`, `README.md`


## Runtime / integration sketch

```mermaid
flowchart LR
  Host["Host / UI"] --> App["CRMImporter"]
  App --> Lib["Libraries"]
  App --> Data["Data access"]
```

> This diagram is inferred from repository layout, languages, and README. It is a starting map, not a full design review.

## Languages

| Language | Approx. file count |
|----------|-------------------|
| C# | 21 files |

## Design notes

| Topic | Detail |
|--------|--------|
| **Stack** | .NET / C# |
| **Default branch** | `master` |
| **Org** | WycliffeAssociates |

## Related

- Source: [WycliffeAssociates/CRMImporter](https://github.com/WycliffeAssociates/CRMImporter)
- Branch analyzed: `master`
